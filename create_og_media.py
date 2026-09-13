import os
from PIL import Image, ImageDraw, ImageFilter, ImageEnhance

# Caminhos dos arquivos
BG_IMAGE_PATH = r"C:\Users\mikaa\.gemini\antigravity-ide\brain\ddbf4aee-d707-4b76-85db-b04896aca68f\araguaia_og_background_1789266560505.jpg"
LOGO_PATH = r"C:\Users\mikaa\Documents\antigravity\gallant-lovelace\site-recanto-dos-sonhos\assets\images\logo-recanto-cropped.png"
OUTPUT_DIR = r"C:\Users\mikaa\Documents\antigravity\gallant-lovelace\site-recanto-dos-sonhos\assets\images"
OUTPUT_JPG = os.path.join(OUTPUT_DIR, "og-recanto-dos-sonhos-araguaia.jpg")
OUTPUT_PNG = os.path.join(OUTPUT_DIR, "og-recanto-dos-sonhos-araguaia.png")

# Dimensões padrão Open Graph (WhatsApp, Facebook, Twitter, LinkedIn)
TARGET_WIDTH = 1200
TARGET_HEIGHT = 630

def create_og_banner():
    print("Carregando imagem de fundo do Araguaia...")
    bg = Image.open(BG_IMAGE_PATH).convert("RGBA")
    
    # Redimensiona e corta para 1200x630 com corte centralizado
    bg_ratio = bg.width / bg.height
    target_ratio = TARGET_WIDTH / TARGET_HEIGHT
    
    if bg_ratio > target_ratio:
        new_height = TARGET_HEIGHT
        new_width = int(TARGET_HEIGHT * bg_ratio)
    else:
        new_width = TARGET_WIDTH
        new_height = int(TARGET_WIDTH / bg_ratio)
        
    bg = bg.resize((new_width, new_height), Image.Resampling.LANCZOS)
    
    left = (new_width - TARGET_WIDTH) // 2
    top = (new_height - TARGET_HEIGHT) // 2
    bg = bg.crop((left, top, left + TARGET_WIDTH, top + TARGET_HEIGHT))
    
    # Camada de escurecimento e vinheta suave para dar contraste nobre à logo
    overlay = Image.new("RGBA", (TARGET_WIDTH, TARGET_HEIGHT), (0, 0, 0, 0))
    draw = ImageDraw.Draw(overlay)
    
    # Gradiente central escuro translúcido com destaque no meio
    for y in range(TARGET_HEIGHT):
        # Gradiente suave de cima e baixo
        norm_y = abs(y - TARGET_HEIGHT / 2) / (TARGET_HEIGHT / 2)
        alpha = int(70 + norm_y * 110) # 70 no centro, 180 nas bordas
        draw.line([(0, y), (TARGET_WIDTH, y)], fill=(10, 10, 10, alpha))
        
    # Círculo radial sutil no centro para abrigar a logo com pureza
    center_glow = Image.new("RGBA", (TARGET_WIDTH, TARGET_HEIGHT), (0, 0, 0, 0))
    glow_draw = ImageDraw.Draw(center_glow)
    glow_draw.ellipse(
        [(TARGET_WIDTH//2 - 320, TARGET_HEIGHT//2 - 220), 
         (TARGET_WIDTH//2 + 320, TARGET_HEIGHT//2 + 220)], 
        fill=(0, 0, 0, 140)
    )
    center_glow = center_glow.filter(ImageFilter.GaussianBlur(50))
    
    # Combina fundo + vinheta + glow escuro
    composed = Image.alpha_composite(bg, overlay)
    composed = Image.alpha_composite(composed, center_glow)
    
    # Carrega e redimensiona a logo oficial
    print("Aplicando logo oficial...")
    logo = Image.open(LOGO_PATH).convert("RGBA")
    
    # Altura da logo proporcional (~310px de altura para destaque imponente)
    logo_target_height = 290
    logo_scale = logo_target_height / logo.height
    logo_target_width = int(logo.width * logo_scale)
    logo = logo.resize((logo_target_width, logo_target_height), Image.Resampling.LANCZOS)
    
    # Sombra da logo (Drop Shadow elegante)
    shadow = Image.new("RGBA", (TARGET_WIDTH, TARGET_HEIGHT), (0, 0, 0, 0))
    logo_x = (TARGET_WIDTH - logo_target_width) // 2
    logo_y = (TARGET_HEIGHT - logo_target_height) // 2 - 25 # Ligeiramente para cima para dar espaço ao selo inferior
    
    # Cria máscara preta da logo para sombra
    shadow_mask = Image.new("RGBA", logo.size, (0, 0, 0, 220))
    shadow_mask.putalpha(logo.split()[3])
    
    # Cola a sombra com offset e blur
    shadow.paste(shadow_mask, (logo_x, logo_y + 8))
    shadow = shadow.filter(ImageFilter.GaussianBlur(18))
    
    # Sobrepõe sombra e logo
    composed = Image.alpha_composite(composed, shadow)
    composed.paste(logo, (logo_x, logo_y), logo)
    
    # Adiciona detalhes gráficos: Borda dourada sutil em volta de todo o banner
    border_draw = ImageDraw.Draw(composed)
    border_color = (192, 151, 99, 160) # #C09763 semi-translúcido
    border_draw.rectangle([(20, 20), (TARGET_WIDTH - 21, TARGET_HEIGHT - 21)], outline=border_color, width=2)
    border_draw.rectangle([(26, 26), (TARGET_WIDTH - 27, TARGET_HEIGHT - 27)], outline=(192, 151, 99, 60), width=1)
    
    # Salva as duas versões (JPG otimizado para WhatsApp/OpenGraph e PNG de máxima qualidade)
    print(f"Salvando versão JPG: {OUTPUT_JPG}...")
    final_rgb = composed.convert("RGB")
    final_rgb.save(OUTPUT_JPG, "JPEG", quality=95, optimize=True)
    
    print(f"Salvando versão PNG: {OUTPUT_PNG}...")
    composed.save(OUTPUT_PNG, "PNG")
    
    print("Mídia de compartilhamento criada com sucesso!")

if __name__ == "__main__":
    create_og_banner()
