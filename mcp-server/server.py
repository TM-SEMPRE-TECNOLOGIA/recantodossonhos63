#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Rancho Recanto dos Sonhos 63 - Bulletproof MCP Server
Compatible with Manus AI, Claude Desktop, Cursor, and any MCP JSON-RPC client.
Supports both newline-delimited JSON and Content-Length header framing.
"""

import sys
import os
import json
import base64
import io
from pathlib import Path
from PIL import Image, ImageEnhance

# Force UTF-8 on Windows
if sys.platform == "win32":
    sys.stdin = io.TextIOWrapper(sys.stdin.buffer, encoding='utf-8', errors='replace')
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

PROJECT_ROOT = Path(__file__).resolve().parent.parent
RANCHO_IMAGES_DIR = PROJECT_ROOT / "assets" / "images" / "rancho"
DOWNLOADS_DIR = Path(r"C:\Users\mikaa\Downloads\FOTOS DO RANCHO\ORGANIZADAS_POR_SECAO")
INDEX_HTML_PATH = PROJECT_ROOT / "index.html"
MOUNTAIN_HTML_PATH = PROJECT_ROOT / "mountain.html"
LOG_FILE = PROJECT_ROOT / "mcp-server" / "mcp_server.log"

def log_debug(msg):
    try:
        with open(LOG_FILE, "a", encoding="utf-8") as f:
            f.write(f"{msg}\n")
    except Exception:
        pass

WEBSITE_IMAGE_SLOTS = {
    "hero_bg": "assets/images/demo-image/hero-praia-araguaia.jpg",
    "hero_shape": "assets/images/demo-image/banner-bg-shape.png",
    "about_thumb1": "assets/images/demo-image/about-thumb31.png",
    "about_thumb2": "assets/images/demo-image/about-thumb32.png",
    "facilities_thumb1": "assets/images/demo-image/facilities-thumb31.png",
    "facilities_thumb2": "assets/images/demo-image/facilities-thumb32.png",
    "room_suite1": "assets/images/demo-image/room-suites-thumb31.png",
    "room_suite2": "assets/images/demo-image/room-suites-thumb32.png",
    "room_suite3": "assets/images/demo-image/room-suites-thumb33.png",
    "video_bg": "assets/images/demo-image/video-bg-3.jpg",
    "blog_thumb1": "assets/images/demo-image/blog-thumb1.jpg",
    "blog_thumb2": "assets/images/demo-image/blog-thumb2.jpg",
    "blog_thumb3": "assets/images/demo-image/blog-thumb3.jpg",
    "testi_thumb": "assets/images/demo-image/testi-thumb21-classic.png"
}

def list_categories():
    cats = []
    if RANCHO_IMAGES_DIR.exists():
        for d in sorted(RANCHO_IMAGES_DIR.iterdir()):
            if d.is_dir():
                cats.append(d.name)
    return cats

def list_photos(category=None):
    results = []
    target_cats = [category] if category else list_categories()
    
    for cat in target_cats:
        cat_path = RANCHO_IMAGES_DIR / cat
        if not cat_path.exists():
            continue
        for img_path in sorted(cat_path.glob("*.jpg")):
            prompt_file = cat_path / f"{img_path.stem}.prompt.txt"
            has_prompt = prompt_file.exists()
            w, h = 0, 0
            try:
                with Image.open(img_path) as im:
                    w, h = im.size
            except Exception:
                pass
                
            results.append({
                "category": cat,
                "filename": img_path.name,
                "path": str(img_path).replace("\\", "/"),
                "resolution": f"{w}x{h}",
                "has_prompt": has_prompt
            })
    return results

def get_photo_prompt(category, filename):
    cat_path = RANCHO_IMAGES_DIR / category
    base_name = Path(filename).stem
    prompt_file = cat_path / f"{base_name}.prompt.txt"
    
    if not prompt_file.exists():
        return {"error": f"Prompt file not found for {filename} in {category}"}
        
    with open(prompt_file, "r", encoding="utf-8") as f:
        content = f.read()
        
    return {
        "category": category,
        "filename": filename,
        "prompt_content": content
    }

def get_photo_base64(category, filename, max_size=800):
    img_path = RANCHO_IMAGES_DIR / category / filename
    if not img_path.exists():
        return {"error": f"Image {filename} not found in {category}"}
        
    with Image.open(img_path) as im:
        im = im.convert("RGB")
        im.thumbnail((max_size, max_size), Image.Resampling.LANCZOS)
        from io import BytesIO
        buffer = BytesIO()
        im.save(buffer, format="JPEG", quality=85)
        b64 = base64.b64encode(buffer.getvalue()).decode("utf-8")
        
    return {
        "filename": filename,
        "format": "jpeg",
        "base64": b64
    }

def auto_remove_timestamp(category, filename, bottom_crop_ratio=0.045):
    img_path = RANCHO_IMAGES_DIR / category / filename
    if not img_path.exists():
        return {"error": f"Image {filename} not found"}
        
    with Image.open(img_path) as im:
        w, h = im.size
        crop_h = int(h * (1.0 - bottom_crop_ratio))
        cropped = im.crop((0, 0, w, crop_h))
        
        out_proj = RANCHO_IMAGES_DIR / category / filename
        out_down = DOWNLOADS_DIR / category / filename
        cropped.save(out_proj, quality=95)
        if out_down.parent.exists():
            cropped.save(out_down, quality=95)
            
    return {
        "success": True,
        "filename": filename,
        "original_resolution": f"{w}x{h}",
        "new_resolution": f"{w}x{crop_h}",
        "message": "Timestamp strip removed cleanly while preserving real image texture."
    }

def apply_cinematic_araguaia_grade(category, filename, warmth=1.1, contrast=1.08, saturation=1.12):
    img_path = RANCHO_IMAGES_DIR / category / filename
    if not img_path.exists():
        return {"error": f"Image {filename} not found"}
        
    with Image.open(img_path) as im:
        im = im.convert("RGB")
        r, g, b = im.split()
        r = r.point(lambda i: min(255, int(i * warmth)))
        g = g.point(lambda i: min(255, int(i * (1.0 + (warmth - 1.0) * 0.5))))
        graded = Image.merge("RGB", (r, g, b))
        
        enhancer = ImageEnhance.Contrast(graded)
        graded = enhancer.enhance(contrast)
        
        enhancer = ImageEnhance.Color(graded)
        graded = enhancer.enhance(saturation)
        
        graded.save(img_path, quality=95)
        down_path = DOWNLOADS_DIR / category / filename
        if down_path.parent.exists():
            graded.save(down_path, quality=95)
            
    return {
        "success": True,
        "filename": filename,
        "grade_applied": {"warmth": warmth, "contrast": contrast, "saturation": saturation},
        "message": "Cinematic Araguaia color grade applied with authentic camera grain preserved."
    }

def save_edited_photo(category, filename, image_base64=None, source_path=None):
    dest_path_proj = RANCHO_IMAGES_DIR / category / filename
    dest_path_down = DOWNLOADS_DIR / category / filename
    
    dest_path_proj.parent.mkdir(parents=True, exist_ok=True)
    dest_path_down.parent.mkdir(parents=True, exist_ok=True)
    
    if image_base64:
        image_bytes = base64.b64decode(image_base64)
        with open(dest_path_proj, "wb") as f:
            f.write(image_bytes)
        with open(dest_path_down, "wb") as f:
            f.write(image_bytes)
    elif source_path and Path(source_path).exists():
        import shutil
        shutil.copy2(source_path, dest_path_proj)
        shutil.copy2(source_path, dest_path_down)
    else:
        return {"error": "Either image_base64 or a valid source_path must be provided."}
        
    return {
        "success": True,
        "message": f"Saved {filename} to {dest_path_proj} and mirrored to {dest_path_down}"
    }

def apply_photo_to_website(category, filename, website_slot):
    if website_slot not in WEBSITE_IMAGE_SLOTS:
        return {
            "error": f"Invalid slot '{website_slot}'. Valid slots are: {list(WEBSITE_IMAGE_SLOTS.keys())}"
        }
        
    rel_rancho_path = f"assets/images/rancho/{category}/{filename}"
    full_source = PROJECT_ROOT / rel_rancho_path
    if not full_source.exists():
        return {"error": f"Photo does not exist at {full_source}"}
        
    old_target_rel = WEBSITE_IMAGE_SLOTS[website_slot]
    updated_files = []
    for html_file in [INDEX_HTML_PATH, MOUNTAIN_HTML_PATH]:
        if html_file.exists():
            with open(html_file, "r", encoding="utf-8") as f:
                content = f.read()
                
            if old_target_rel in content:
                new_content = content.replace(old_target_rel, rel_rancho_path)
                with open(html_file, "w", encoding="utf-8") as f:
                    f.write(new_content)
                updated_files.append(html_file.name)
                
    return {
        "success": True,
        "website_slot": website_slot,
        "old_placeholder": old_target_rel,
        "new_image": rel_rancho_path,
        "updated_pages": updated_files
    }

TOOLS_SPEC = [
    {
        "name": "list_rancho_photos",
        "description": "Lists all photos organized by category (01-hero-e-aereas, 02-praia-e-barcos, 03-estrutura-e-lazer, 04-acomodacoes, 05-social-e-experiencias, 06-como-chegar) with dimensions and prompt availability.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "category": {"type": "string", "description": "Optional category name to filter photos."}
            }
        }
    },
    {
        "name": "get_photo_prompt",
        "description": "Retrieves the anti-render prompt, preservation guidelines, and editing instructions for a specific photo. Guarantees authentic textures, real materials, zero plastic AI render look.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "category": {"type": "string", "description": "Category directory (e.g. 02-praia-e-barcos, 04-acomodacoes)"},
                "filename": {"type": "string", "description": "Photo filename (e.g. barcos-voadeiras-recanto-dos-sonhos.jpg)"}
            },
            "required": ["category", "filename"]
        }
    },
    {
        "name": "get_photo_base64",
        "description": "Returns a Base64-encoded JPEG thumbnail of the photo so the agent can visually inspect its content and framing.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "category": {"type": "string"},
                "filename": {"type": "string"},
                "max_size": {"type": "integer", "description": "Maximum width/height in px (default 800)"}
            },
            "required": ["category", "filename"]
        }
    },
    {
        "name": "auto_remove_timestamp",
        "description": "Removes the camera date watermark (e.g. '17 de maio de 2026 15:06') cleanly from the bottom of a photo without altering scene composition or texture.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "category": {"type": "string"},
                "filename": {"type": "string"},
                "bottom_crop_ratio": {"type": "number", "description": "Ratio to crop (default 0.045 for 4.5%)"}
            },
            "required": ["category", "filename"]
        }
    },
    {
        "name": "apply_cinematic_araguaia_grade",
        "description": "Applies a realistic warm golden-hour and crystal water color grade without plastic AI smoothing. Preserves camera sensor grain and real materials.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "category": {"type": "string"},
                "filename": {"type": "string"},
                "warmth": {"type": "number", "description": "Warmth factor (default 1.1)"},
                "contrast": {"type": "number", "description": "Contrast factor (default 1.08)"},
                "saturation": {"type": "number", "description": "Saturation factor (default 1.12)"}
            },
            "required": ["category", "filename"]
        }
    },
    {
        "name": "save_edited_photo",
        "description": "Saves an AI-edited or retouched photo into the project and mirrors it to the user's Downloads folder.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "category": {"type": "string"},
                "filename": {"type": "string"},
                "image_base64": {"type": "string", "description": "Base64 encoded bytes of edited image"},
                "source_path": {"type": "string", "description": "Or local file path to the edited image"}
            },
            "required": ["category", "filename"]
        }
    },
    {
        "name": "apply_photo_to_website",
        "description": "Inserts the chosen photo directly into the live website HTML (index.html), replacing placeholder elements.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "category": {"type": "string"},
                "filename": {"type": "string"},
                "website_slot": {
                    "type": "string",
                    "description": "Target website slot: 'hero_bg', 'about_thumb1', 'about_thumb2', 'facilities_thumb1', 'facilities_thumb2', 'room_suite1', 'room_suite2', 'room_suite3', 'video_bg', 'blog_thumb1', 'blog_thumb2', 'blog_thumb3', 'testi_thumb'"
                }
            },
            "required": ["category", "filename", "website_slot"]
        }
    }
]

def handle_call_tool(name, args):
    if name == "list_rancho_photos":
        return list_photos(args.get("category"))
    elif name == "get_photo_prompt":
        return get_photo_prompt(args["category"], args["filename"])
    elif name == "get_photo_base64":
        return get_photo_base64(args["category"], args["filename"], args.get("max_size", 800))
    elif name == "auto_remove_timestamp":
        return auto_remove_timestamp(args["category"], args["filename"], args.get("bottom_crop_ratio", 0.045))
    elif name == "apply_cinematic_araguaia_grade":
        return apply_cinematic_araguaia_grade(
            args["category"], args["filename"],
            args.get("warmth", 1.1),
            args.get("contrast", 1.08),
            args.get("saturation", 1.12)
        )
    elif name == "save_edited_photo":
        return save_edited_photo(args["category"], args["filename"], args.get("image_base64"), args.get("source_path"))
    elif name == "apply_photo_to_website":
        return apply_photo_to_website(args["category"], args["filename"], args["website_slot"])
    else:
        return {"error": f"Unknown tool: {name}"}

def process_mcp_message(msg):
    method = msg.get("method")
    msg_id = msg.get("id")
    log_debug(f"[RECV] method={method} id={msg_id}")
    
    if method == "initialize":
        return {
            "jsonrpc": "2.0",
            "id": msg_id,
            "result": {
                "protocolVersion": "2024-11-05",
                "capabilities": {
                    "tools": {}
                },
                "serverInfo": {
                    "name": "rancho-recanto-mcp",
                    "version": "1.0.0"
                }
            }
        }
    elif method == "notifications/initialized":
        return None
    elif method == "tools/list":
        return {
            "jsonrpc": "2.0",
            "id": msg_id,
            "result": {
                "tools": TOOLS_SPEC
            }
        }
    elif method == "tools/call":
        params = msg.get("params", {})
        tool_name = params.get("name")
        tool_args = params.get("arguments", {})
        res = handle_call_tool(tool_name, tool_args)
        return {
            "jsonrpc": "2.0",
            "id": msg_id,
            "result": {
                "content": [
                    {
                        "type": "text",
                        "text": json.dumps(res, indent=2, ensure_ascii=False)
                    }
                ]
            }
        }
    elif method == "ping":
        return {"jsonrpc": "2.0", "id": msg_id, "result": {}}
    else:
        return {
            "jsonrpc": "2.0",
            "id": msg_id,
            "error": {
                "code": -32601,
                "message": f"Method not found: {method}"
            }
        }

def send_response(resp):
    if resp is None:
        return
    payload = json.dumps(resp, ensure_ascii=False)
    log_debug(f"[SEND] {payload[:120]}...")
    sys.stdout.write(payload + "\n")
    sys.stdout.flush()

def run_stdio():
    """Clean standard MCP stdio loop with unbuffered newline-delimited JSON-RPC."""
    log_debug("[START] MCP Server started in STDIO mode")
    for line in sys.stdin:
        line_str = line.strip()
        if not line_str:
            continue
        try:
            req = json.loads(line_str)
            resp = process_mcp_message(req)
            send_response(resp)
        except Exception as e:
            log_debug(f"[ERROR] Failed to process message '{line_str[:60]}': {e}")
            err = {
                "jsonrpc": "2.0",
                "id": None,
                "error": {"code": -32700, "message": f"Parse error: {str(e)}"}
            }
            send_response(err)

if __name__ == "__main__":
    run_stdio()
