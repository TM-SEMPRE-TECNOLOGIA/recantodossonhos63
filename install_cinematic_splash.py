import re

custom_css_path = r"c:\Users\mikaa\Documents\antigravity\gallant-lovelace\site-recanto-dos-sonhos\assets\css\custom.css"
index_html_path = r"c:\Users\mikaa\Documents\antigravity\gallant-lovelace\site-recanto-dos-sonhos\index.html"
mountain_html_path = r"c:\Users\mikaa\Documents\antigravity\gallant-lovelace\site-recanto-dos-sonhos\mountain.html"

splash_css = """
/*==========================================================================
   MÓDULO DE ENTRADA SPLASH CINEMATOGRÁFICO • RECANTO DOS SONHOS 63
   ========================================================================== */
.preloader, .loader {
  display: none !important;
}

#splash-screen {
  position: fixed;
  top: 0;
  left: 0;
  width: 100vw;
  height: 100vh;
  background-color: #0E1A14 !important; /* Verde Cerrado Nobre */
  z-index: 9999999 !important;
  display: flex !important;
  flex-direction: column !important;
  align-items: center !important;
  justify-content: center !important;
  opacity: 1 !important;
  visibility: visible !important;
  transition: opacity 0.85s cubic-bezier(0.4, 0, 0.2, 1), 
              visibility 0.85s cubic-bezier(0.4, 0, 0.2, 1),
              transform 0.85s cubic-bezier(0.4, 0, 0.2, 1) !important;
  will-change: opacity, transform;
}

#splash-screen.splash-fade-out {
  opacity: 0 !important;
  visibility: hidden !important;
  transform: scale(1.04) !important;
  pointer-events: none !important;
}

.splash-halo {
  position: absolute;
  width: 480px;
  height: 480px;
  border-radius: 50%;
  background: radial-gradient(circle, rgba(212, 175, 55, 0.22) 0%, transparent 70%);
  pointer-events: none;
  animation: pulseHalo 2.5s ease-in-out infinite alternate;
}

@keyframes pulseHalo {
  0% { transform: scale(0.9); opacity: 0.3; }
  100% { transform: scale(1.15); opacity: 0.8; }
}

.splash-content {
  position: relative;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  z-index: 2;
  opacity: 0;
  transform: scale(0.86) translateY(14px);
  animation: logoEntrance 0.9s cubic-bezier(0.16, 1, 0.3, 1) 0.15s forwards;
}

@keyframes logoEntrance {
  0% {
    opacity: 0;
    transform: scale(0.86) translateY(14px);
    filter: blur(8px);
  }
  100% {
    opacity: 1;
    transform: scale(1) translateY(0);
    filter: blur(0px);
  }
}

.splash-logo-img {
  max-width: 310px;
  width: 80vw;
  height: auto;
  filter: drop-shadow(0 16px 36px rgba(0, 0, 0, 0.65)) 
          drop-shadow(0 0 25px rgba(212, 175, 55, 0.35));
  display: block;
}

.splash-shine {
  position: absolute;
  top: 0;
  left: -120%;
  width: 100%;
  height: 100%;
  background: linear-gradient(
    120deg,
    transparent 0%,
    rgba(255, 255, 255, 0.45) 50%,
    rgba(255, 215, 0, 0.35) 55%,
    transparent 70%
  );
  transform: skewX(-25deg);
  pointer-events: none;
  animation: sweepShine 1.1s cubic-bezier(0.4, 0, 0.2, 1) 0.5s forwards;
}

@keyframes sweepShine {
  0% { left: -120%; opacity: 0; }
  30% { opacity: 0.9; }
  70% { opacity: 0.9; }
  100% { left: 180%; opacity: 0; }
}

.splash-tagline {
  margin-top: 22px;
  display: flex;
  align-items: center;
  gap: 14px;
  opacity: 0;
  animation: taglineEntrance 0.7s ease 0.45s forwards;
}

@keyframes taglineEntrance {
  to { opacity: 1; transform: translateY(0); }
}

.splash-line {
  height: 1px;
  width: 40px;
  background: linear-gradient(90deg, transparent, #c09763, transparent);
}

.splash-tagline-text {
  font-family: 'JetBrains Mono', monospace;
  font-size: 11px;
  letter-spacing: 3px;
  text-transform: uppercase;
  color: #c09763;
  font-weight: 700;
  white-space: nowrap;
  text-shadow: 0 0 10px rgba(192, 151, 99, 0.4);
}

.splash-progress-track {
  position: absolute;
  bottom: 36px;
  width: 160px;
  height: 2px;
  background: rgba(255, 255, 255, 0.08);
  border-radius: 2px;
  overflow: hidden;
}

.splash-progress-fill {
  width: 0%;
  height: 100%;
  background: linear-gradient(90deg, #c09763, #f7dca3);
  animation: progressFill 1.5s cubic-bezier(0.16, 1, 0.3, 1) 0.3s forwards;
  box-shadow: 0 0 8px #c09763;
}

@keyframes progressFill {
  to { width: 100%; }
}
"""

# Append to custom.css
with open(custom_css_path, "r", encoding="utf-8") as f:
    css_content = f.read()

if "#splash-screen" not in css_content:
    css_content += "\n" + splash_css
    with open(custom_css_path, "w", encoding="utf-8") as f:
        f.write(css_content)
    print("Added splash screen CSS to custom.css!")

splash_html = """    <!-- ========================================================================= -->
    <!-- TELA DE ENTRADA CINEMATOGRÁFICA (SPLASH SCREEN • RECANTO DOS SONHOS 63)   -->
    <!-- ========================================================================= -->
    <div id="splash-screen">
      <!-- Halo dourado pulsante -->
      <div class="splash-halo"></div>

      <!-- Container da Logo e Animações -->
      <div class="splash-content">
        <div style="position: relative; overflow: hidden; border-radius: 12px;">
          <img
            src="assets/images/logo-recanto-cropped.png?v=3"
            alt="Rancho Recanto dos Sonhos 63"
            class="splash-logo-img"
          />
          <div class="splash-shine"></div>
        </div>

        <div class="splash-tagline">
          <div class="splash-line"></div>
          <span class="splash-tagline-text">Peixe • Tocantins | À Beira do Araguaia</span>
          <div class="splash-line"></div>
        </div>
      </div>

      <!-- Barra de progresso dourada sutil -->
      <div class="splash-progress-track">
        <div class="splash-progress-fill"></div>
      </div>
    </div>

    <script>
      (function() {
        function hideSplashScreen() {
          const splash = document.getElementById('splash-screen');
          if (splash && !splash.classList.contains('splash-fade-out')) {
            splash.classList.add('splash-fade-out');
            setTimeout(() => {
              splash.style.display = 'none';
            }, 900);
          }
        }

        let hidden = false;
        const triggerExit = () => {
          if (!hidden) {
            hidden = true;
            hideSplashScreen();
          }
        };

        window.addEventListener('load', () => {
          setTimeout(triggerExit, 1200);
        });

        // Fallback safety timeout (1.9 seconds max)
        setTimeout(triggerExit, 1900);
      })();
    </script>"""

# Replace in index.html and mountain.html
for path in [index_html_path, mountain_html_path]:
    with open(path, "r", encoding="utf-8") as f:
        html = f.read()

    # Replace old preloader
    old_preloader_pattern = r'<!--\s*========= Prealoader ==============-->[\s\S]+?<!--========= End Prealoader ============== -->\s*'
    if re.search(old_preloader_pattern, html):
        html = re.sub(old_preloader_pattern, splash_html + "\n\n", html)
    elif "id=\"splash-screen\"" not in html:
        html = html.replace("<body>", "<body>\n" + splash_html)

    # Bump custom.css version to ?v=5
    html = re.sub(r'assets/css/custom\.css\?v=\d+', 'assets/css/custom.css?v=5', html)

    with open(path, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"Installed cinematic splash screen in {path}!")

print("SUCCESS: Cinematic splash screen entrance fully integrated!")
