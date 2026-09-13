import re

custom_css_path = r"c:\Users\mikaa\Documents\antigravity\gallant-lovelace\site-recanto-dos-sonhos\assets\css\custom.css"
index_html_path = r"c:\Users\mikaa\Documents\antigravity\gallant-lovelace\site-recanto-dos-sonhos\index.html"
mountain_html_path = r"c:\Users\mikaa\Documents\antigravity\gallant-lovelace\site-recanto-dos-sonhos\mountain.html"

# 1. Update custom.css with dynamic theme variable mappings
theme_css_rules = """
/*==================================================*/
/* VARIÁVEIS DINÂMICAS DE TESTE DE TEMA & CORES     */
/*==================================================*/
:root {
  --theme-btn-accent: #c09763;
  --theme-btn-hover: #000000;
  --theme-btn-text: #ffffff;
  --theme-header-bg: #0a0a0a;
  --theme-footer-bg: #0a0a0a;
  --theme-booking-bg: #101114;
}

/* Botões do Topo, Hero, Barra de Reserva, Facilities, Quartos e Praia */
.header-btn .theme-btn,
.theme-btn.btn-style-two,
.booking-section-one .booking-button button,
.facilities-btn.defult-btn a,
.defult-btn a,
.room-btn.defult-btn a,
.explore-btn,
.subscribe-btn,
.hero-button a.theme-btn {
  background: var(--theme-btn-accent) !important;
  color: var(--theme-btn-text) !important;
  border-color: var(--theme-btn-accent) !important;
  transition: all 0.3s ease !important;
}

.booking-section-one .booking-button button {
  box-shadow: 0 8px 22px rgba(0, 0, 0, 0.5) !important;
}

/* Detalhes de Destaque / Dourado */
.title-gold,
.date-field-label,
.date-field-label i,
.sec-title .title-gold,
.rooms-title span.rooms-sub-title,
.about-section-three .section-sub-title .sub-title,
.facilities-content h1,
.footer-menu a:hover,
.footer-social a:hover,
.room-price a {
  color: var(--theme-btn-accent) !important;
}

/* Cabeçalho */
.hotelio-header-area,
.hotelio-header-area.sticky {
  background-color: var(--theme-header-bg) !important;
  transition: background-color 0.3s ease !important;
}

/* Rodapé */
.main-footer-one,
.main-footer-section {
  background-color: var(--theme-footer-bg) !important;
  transition: background-color 0.3s ease !important;
}

/* Barra de Reserva */
.booking-section-one .add-bg {
  background-color: var(--theme-booking-bg) !important;
  border-color: var(--theme-btn-accent) !important;
  transition: background-color 0.3s ease, border-color 0.3s ease !important;
}

/* Estilos do Widget Seletor de Cores Flutuante */
#theme-tester-toggle {
  position: fixed;
  right: 20px;
  bottom: 85px;
  z-index: 99999;
  background: #111418;
  color: #fff;
  border: 1px solid #c09763;
  padding: 10px 16px;
  border-radius: 30px;
  font-size: 13px;
  font-weight: 700;
  cursor: pointer;
  box-shadow: 0 8px 25px rgba(0, 0, 0, 0.6), 0 0 15px rgba(192, 151, 99, 0.3);
  display: flex;
  align-items: center;
  gap: 8px;
  transition: all 0.3s ease;
  font-family: inherit;
}

#theme-tester-toggle:hover {
  transform: translateY(-3px) scale(1.04);
  background: #c09763;
  color: #000;
}

#theme-tester-panel {
  position: fixed;
  right: 20px;
  bottom: 140px;
  width: 320px;
  background: rgba(14, 16, 20, 0.96);
  backdrop-filter: blur(20px);
  -webkit-backdrop-filter: blur(20px);
  border: 1px solid rgba(192, 151, 99, 0.4);
  border-radius: 16px;
  padding: 20px;
  z-index: 99999;
  box-shadow: 0 20px 50px rgba(0,0,0,0.8);
  display: none;
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
  color: #fff;
  animation: testerFadeIn 0.25s ease;
}

@keyframes testerFadeIn {
  from { opacity: 0; transform: translateY(10px); }
  to { opacity: 1; transform: translateY(0); }
}

#theme-tester-panel.active {
  display: block;
}

.tester-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 15px;
  padding-bottom: 10px;
  border-bottom: 1px solid rgba(255,255,255,0.1);
}

.tester-header h4 {
  font-size: 14px;
  font-weight: 700;
  margin: 0;
  color: #fff;
  display: flex;
  align-items: center;
  gap: 6px;
}

.tester-header button.close-btn {
  background: transparent;
  border: none;
  color: #888;
  font-size: 18px;
  cursor: pointer;
  line-height: 1;
}

.tester-header button.close-btn:hover {
  color: #fff;
}

.tester-row {
  margin-bottom: 12px;
  display: flex;
  align-items: center;
  justify-content: space-between;
}

.tester-row label {
  font-size: 12px;
  font-weight: 500;
  color: #d1d5db;
  margin: 0;
}

.tester-color-wrap {
  display: flex;
  align-items: center;
  gap: 8px;
}

.tester-color-wrap input[type="color"] {
  -webkit-appearance: none;
  border: none;
  width: 32px;
  height: 32px;
  border-radius: 8px;
  cursor: pointer;
  background: transparent;
}

.tester-color-wrap input[type="color"]::-webkit-color-swatch-wrapper {
  padding: 0;
}

.tester-color-wrap input[type="color"]::-webkit-color-swatch {
  border: 1px solid rgba(255,255,255,0.3);
  border-radius: 8px;
}

.tester-hex {
  font-size: 11px;
  font-family: monospace;
  color: #9ca3af;
  min-width: 55px;
}

.tester-presets {
  margin-top: 15px;
  padding-top: 12px;
  border-top: 1px solid rgba(255,255,255,0.1);
}

.tester-presets-title {
  font-size: 11px;
  font-weight: 700;
  color: #9ca3af;
  text-transform: uppercase;
  letter-spacing: 0.5px;
  margin-bottom: 8px;
}

.tester-chips {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 6px;
}

.tester-chip {
  background: rgba(255,255,255,0.06);
  border: 1px solid rgba(255,255,255,0.12);
  color: #e5e7eb;
  padding: 6px 8px;
  border-radius: 6px;
  font-size: 11px;
  font-weight: 600;
  cursor: pointer;
  text-align: left;
  display: flex;
  align-items: center;
  gap: 6px;
  transition: all 0.2s;
}

.tester-chip:hover {
  background: rgba(255,255,255,0.14);
  border-color: #c09763;
}

.tester-chip-dot {
  width: 10px;
  height: 10px;
  border-radius: 50%;
  flex-shrink: 0;
}

.tester-actions {
  margin-top: 14px;
  display: flex;
  gap: 8px;
}

.tester-actions button {
  flex: 1;
  padding: 8px 10px;
  border-radius: 6px;
  font-size: 11px;
  font-weight: 700;
  cursor: pointer;
  transition: all 0.2s;
}

.tester-btn-copy {
  background: #c09763;
  color: #000;
  border: none;
}

.tester-btn-copy:hover {
  background: #dfb37c;
}

.tester-btn-reset {
  background: transparent;
  color: #9ca3af;
  border: 1px solid rgba(255,255,255,0.15);
}

.tester-btn-reset:hover {
  color: #fff;
  border-color: #fff;
}
"""

with open(custom_css_path, "r", encoding="utf-8") as f:
    css_content = f.read()

if "/* VARIÁVEIS DINÂMICAS DE TESTE DE TEMA & CORES */" not in css_content:
    css_content += "\n" + theme_css_rules
    with open(custom_css_path, "w", encoding="utf-8") as f:
        f.write(css_content)
    print("Updated custom.css with dynamic theme variables!")

# 2. Component HTML & JS for the Live Color Selector
widget_html = """
    <!-- ============================================== -->
    <!-- WIDGET FLUTUANTE: SELETOR DE CORES & TESTE     -->
    <!-- ============================================== -->
    <button id="theme-tester-toggle" aria-label="Abrir Seletor de Cores">
      <i class="bi bi-palette-fill" style="color: #c09763;"></i> Testar Cores
    </button>

    <div id="theme-tester-panel">
      <div class="tester-header">
        <h4><i class="bi bi-palette"></i> Testador de Cores</h4>
        <button class="close-btn" id="tester-close-btn" title="Fechar">&times;</button>
      </div>

      <div class="tester-row">
        <label for="color-accent">Botões & Detalhes</label>
        <div class="tester-color-wrap">
          <input type="color" id="color-accent" value="#c09763">
          <span class="tester-hex" id="hex-accent">#c09763</span>
        </div>
      </div>

      <div class="tester-row">
        <label for="color-header">Fundo do Header</label>
        <div class="tester-color-wrap">
          <input type="color" id="color-header" value="#0a0a0a">
          <span class="tester-hex" id="hex-header">#0a0a0a</span>
        </div>
      </div>

      <div class="tester-row">
        <label for="color-footer">Fundo do Footer</label>
        <div class="tester-color-wrap">
          <input type="color" id="color-footer" value="#0a0a0a">
          <span class="tester-hex" id="hex-footer">#0a0a0a</span>
        </div>
      </div>

      <div class="tester-row">
        <label for="color-booking">Barra de Reservas</label>
        <div class="tester-color-wrap">
          <input type="color" id="color-booking" value="#101114">
          <span class="tester-hex" id="hex-booking">#101114</span>
        </div>
      </div>

      <div class="tester-presets">
        <div class="tester-presets-title">Paletas Rápidas (1 Clique)</div>
        <div class="tester-chips">
          <button class="tester-chip" data-accent="#c09763" data-header="#0a0a0a" data-footer="#0a0a0a" data-booking="#101114">
            <span class="tester-chip-dot" style="background:#c09763;"></span> Dourado
          </button>
          <button class="tester-chip" data-accent="#0284c7" data-header="#071526" data-footer="#050f1d" data-booking="#0c1e36">
            <span class="tester-chip-dot" style="background:#0284c7;"></span> Azul Rio
          </button>
          <button class="tester-chip" data-accent="#16a34a" data-header="#0a1a10" data-footer="#07140c" data-booking="#0f2617">
            <span class="tester-chip-dot" style="background:#16a34a;"></span> Verde Eco
          </button>
          <button class="tester-chip" data-accent="#ea580c" data-header="#1c0e07" data-footer="#140a05" data-booking="#261209">
            <span class="tester-chip-dot" style="background:#ea580c;"></span> Pôr do Sol
          </button>
        </div>
      </div>

      <div class="tester-actions">
        <button class="tester-btn-copy" id="tester-copy-btn">Copiar HEX</button>
        <button class="tester-btn-reset" id="tester-reset-btn">Padrão</button>
      </div>
    </div>

    <script>
      (function() {
        const toggleBtn = document.getElementById('theme-tester-toggle');
        const panel = document.getElementById('theme-tester-panel');
        const closeBtn = document.getElementById('tester-close-btn');
        const copyBtn = document.getElementById('tester-copy-btn');
        const resetBtn = document.getElementById('tester-reset-btn');

        const inputAccent = document.getElementById('color-accent');
        const inputHeader = document.getElementById('color-header');
        const inputFooter = document.getElementById('color-footer');
        const inputBooking = document.getElementById('color-booking');

        const hexAccent = document.getElementById('hex-accent');
        const hexHeader = document.getElementById('hex-header');
        const hexFooter = document.getElementById('hex-footer');
        const hexBooking = document.getElementById('hex-booking');

        const defaults = {
          accent: '#c09763',
          header: '#0a0a0a',
          footer: '#0a0a0a',
          booking: '#101114'
        };

        function applyTheme(accent, header, footer, booking, save = true) {
          document.documentElement.style.setProperty('--theme-btn-accent', accent);
          document.documentElement.style.setProperty('--theme-header-bg', header);
          document.documentElement.style.setProperty('--theme-footer-bg', footer);
          document.documentElement.style.setProperty('--theme-booking-bg', booking);

          inputAccent.value = accent;
          inputHeader.value = header;
          inputFooter.value = footer;
          inputBooking.value = booking;

          hexAccent.textContent = accent;
          hexHeader.textContent = header;
          hexFooter.textContent = footer;
          hexBooking.textContent = booking;

          if (save) {
            localStorage.setItem('rancho_theme_test', JSON.stringify({ accent, header, footer, booking }));
          }
        }

        toggleBtn.addEventListener('click', () => {
          panel.classList.toggle('active');
        });

        closeBtn.addEventListener('click', () => {
          panel.classList.remove('active');
        });

        inputAccent.addEventListener('input', (e) => applyTheme(e.target.value, inputHeader.value, inputFooter.value, inputBooking.value));
        inputHeader.addEventListener('input', (e) => applyTheme(inputAccent.value, e.target.value, inputFooter.value, inputBooking.value));
        inputFooter.addEventListener('input', (e) => applyTheme(inputAccent.value, inputHeader.value, e.target.value, inputBooking.value));
        inputBooking.addEventListener('input', (e) => applyTheme(inputAccent.value, inputHeader.value, inputFooter.value, e.target.value));

        document.querySelectorAll('.tester-chip').forEach(chip => {
          chip.addEventListener('click', () => {
            applyTheme(
              chip.getAttribute('data-accent'),
              chip.getAttribute('data-header'),
              chip.getAttribute('data-footer'),
              chip.getAttribute('data-booking')
            );
          });
        });

        resetBtn.addEventListener('click', () => {
          applyTheme(defaults.accent, defaults.header, defaults.footer, defaults.booking);
          localStorage.removeItem('rancho_theme_test');
        });

        copyBtn.addEventListener('click', () => {
          const text = `Cores Escolhidas para o Rancho:\\n- Botões/Destaque: ${inputAccent.value}\\n- Header: ${inputHeader.value}\\n- Footer: ${inputFooter.value}\\n- Barra de Reserva: ${inputBooking.value}`;
          navigator.clipboard.writeText(text).then(() => {
            const orig = copyBtn.textContent;
            copyBtn.textContent = 'Copiado! ✓';
            setTimeout(() => { copyBtn.textContent = orig; }, 1800);
          });
        });

        // Load saved state on page open
        try {
          const saved = JSON.parse(localStorage.getItem('rancho_theme_test'));
          if (saved) {
            applyTheme(saved.accent, saved.header, saved.footer, saved.booking, false);
          }
        } catch (e) {}
      })();
    </script>
"""

for path in [index_html_path, mountain_html_path]:
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    if "theme-tester-toggle" not in content:
        content = content.replace("</body>", widget_html + "\n  </body>")
        with open(path, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Injected color tester into {path}")

print("SUCCESS: Live color picker & theme tester injected into index.html and mountain.html!")
