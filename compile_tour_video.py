import cv2
import os
import glob
import sys

FRAMES_DIR = os.path.join(os.path.dirname(__file__), "tour_frames")
OUTPUT_VIDEO = os.path.join(os.path.dirname(__file__), "recanto_dos_sonhos_demo.mp4")

def main():
    frame_files = sorted(glob.glob(os.path.join(FRAMES_DIR, "frame_*.jpg")))
    if not frame_files:
        print("Nenhum frame encontrado em:", FRAMES_DIR)
        sys.exit(1)

    print(f"Compilando {len(frame_files)} frames em {OUTPUT_VIDEO}...")
    
    first_frame = cv2.imread(frame_files[0])
    height, width, layers = first_frame.shape

    # Codec MP4V para máxima compatibilidade no Windows e Web
    fourcc = cv2.VideoWriter_fourcc(*"mp4v")
    fps = 24.0
    out = cv2.VideoWriter(OUTPUT_VIDEO, fourcc, fps, (width, height))

    for idx, fpath in enumerate(frame_files):
        img = cv2.imread(fpath)
        out.write(img)
        if (idx + 1) % 50 == 0 or idx == len(frame_files) - 1:
            print(f"Processado: {idx + 1}/{len(frame_files)} frames...")

    out.release()
    print(f"Vídeo gerado com sucesso: {OUTPUT_VIDEO} ({os.path.getsize(OUTPUT_VIDEO) / 1024 / 1024:.2f} MB)")

if __name__ == "__main__":
    main()
