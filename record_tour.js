const puppeteer = require('puppeteer-core');
const fs = require('fs');
const path = require('path');

const CHROME_PATH = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe";
const FRAMES_DIR = path.join(__dirname, 'tour_frames');

if (!fs.existsSync(FRAMES_DIR)) {
  fs.mkdirSync(FRAMES_DIR, { recursive: true });
}

// Limpa frames antigos
fs.readdirSync(FRAMES_DIR).forEach(f => fs.unlinkSync(path.join(FRAMES_DIR, f)));

async function run() {
  console.log('Iniciando gravação de tour interativo...');
  const browser = await puppeteer.launch({
    executablePath: CHROME_PATH,
    headless: true,
    args: [
      '--no-sandbox',
      '--disable-setuid-sandbox',
      '--disable-dev-shm-usage',
      '--disable-gpu',
      '--window-size=1366,768'
    ],
    defaultViewport: {
      width: 1366,
      height: 768,
      deviceScaleFactor: 1
    }
  });

  const page = await browser.newPage();
  await page.goto('http://localhost:3000/index.html', { waitUntil: 'networkidle2' });

  // Injeta cursor do mouse interativo e animado
  await page.evaluate(() => {
    const cursor = document.createElement('div');
    cursor.id = 'interactive-cursor';
    cursor.innerHTML = `
      <svg width="28" height="28" viewBox="0 0 28 28" fill="none" xmlns="http://www.w3.org/2000/svg" style="filter: drop-shadow(0 2px 5px rgba(0,0,0,0.6));">
        <path d="M4 2L22 14L13 16L9 25L4 2Z" fill="#C09763" stroke="#FFFFFF" stroke-width="2" stroke-linejoin="round"/>
      </svg>
      <div id="cursor-ripple" style="position: absolute; top: 0; left: 0; width: 10px; height: 10px; border-radius: 50%; background: rgba(192, 151, 99, 0.6); pointer-events: none; opacity: 0; transform: translate(-50%, -50%) scale(0); transition: transform 0.4s ease-out, opacity 0.4s ease-out;"></div>
    `;
    cursor.style.position = 'fixed';
    cursor.style.top = '100px';
    cursor.style.left = '100px';
    cursor.style.zIndex = '9999999';
    cursor.style.pointerEvents = 'none';
    cursor.style.transition = 'top 0.1s linear, left 0.1s linear';
    document.body.appendChild(cursor);

    window.moveCursor = (x, y) => {
      cursor.style.top = `${y}px`;
      cursor.style.left = `${x}px`;
    };

    window.triggerClick = () => {
      const ripple = document.getElementById('cursor-ripple');
      if (ripple) {
        ripple.style.transition = 'none';
        ripple.style.transform = 'translate(-50%, -50%) scale(0)';
        ripple.style.opacity = '1';
        setTimeout(() => {
          ripple.style.transition = 'transform 0.4s ease-out, opacity 0.4s ease-out';
          ripple.style.transform = 'translate(-50%, -50%) scale(4)';
          ripple.style.opacity = '0';
        }, 20);
      }
    };
  });

  let frameCount = 0;
  async function captureFrame() {
    frameCount++;
    const framePath = path.join(FRAMES_DIR, `frame_${String(frameCount).padStart(5, '0')}.jpg`);
    await page.screenshot({ path: framePath, type: 'jpeg', quality: 85 });
  }

  async function animateTo(targetX, targetY, steps = 15, delay = 35) {
    const currentPos = await page.evaluate(() => {
      const c = document.getElementById('interactive-cursor');
      return { x: parseFloat(c.style.left) || 100, y: parseFloat(c.style.top) || 100 };
    });

    for (let i = 1; i <= steps; i++) {
      const t = i / steps;
      // Interpolação cúbica ease-in-out
      const ease = t < 0.5 ? 4 * t * t * t : 1 - Math.pow(-2 * t + 2, 3) / 2;
      const x = currentPos.x + (targetX - currentPos.x) * ease;
      const y = currentPos.y + (targetY - currentPos.y) * ease;

      await page.evaluate((cx, cy) => window.moveCursor(cx, cy), Math.round(x), Math.round(y));
      await captureFrame();
      await new Promise(r => setTimeout(r, delay));
    }
  }

  async function clickAt(x, y) {
    await animateTo(x, y, 10);
    await page.evaluate(() => window.triggerClick());
    await captureFrame();
    await captureFrame();
  }

  async function smoothScroll(deltaY, steps = 20) {
    for (let i = 1; i <= steps; i++) {
      await page.evaluate((dy) => window.scrollBy(0, dy), deltaY / steps);
      await captureFrame();
      await new Promise(r => setTimeout(r, 25));
    }
    await new Promise(r => setTimeout(r, 200));
  }

  // 1. Início na página inicial (espera carregar e faz introdução)
  console.log('Gravando cena 1: Header e Apresentação...');
  for (let i = 0; i < 15; i++) await captureFrame();

  // 2. Cursor vai até a Logo centralizada
  console.log('Gravando cena 2: Destaque na logo...');
  await animateTo(680, 50, 18);
  for (let i = 0; i < 10; i++) await captureFrame();

  // 3. Cursor vai até o botão Menu Hambúrguer dourado e clica
  console.log('Gravando cena 3: Abrindo menu hambúrguer...');
  await clickAt(80, 50);
  await page.click('.navSidebar-button a');
  for (let i = 0; i < 18; i++) await captureFrame();

  // 4. Cursor navega dentro da gaveta lateral pelos links
  console.log('Gravando cena 4: Navegando na gaveta lateral...');
  await animateTo(1150, 320, 14);
  for (let i = 0; i < 8; i++) await captureFrame();
  await animateTo(1150, 420, 14);
  for (let i = 0; i < 8; i++) await captureFrame();
  
  // Destaque no botão de Reservar do WhatsApp dentro da sidebar
  await animateTo(1150, 560, 15);
  for (let i = 0; i < 12; i++) await captureFrame();

  // 5. Fecha a gaveta
  await clickAt(1310, 35);
  await page.click('.close-side-widget');
  for (let i = 0; i < 15; i++) await captureFrame();

  // 6. Move até o botão RESERVAR AGORA no header
  console.log('Gravando cena 5: Botão Reservar no header...');
  await animateTo(1260, 50, 16);
  for (let i = 0; i < 10; i++) await captureFrame();

  // 7. Rola suavemente pelo Hero até a Barra de Reservas
  console.log('Gravando cena 6: Barra de Reservas...');
  await animateTo(680, 400, 15);
  await smoothScroll(380, 22);
  for (let i = 0; i < 12; i++) await captureFrame();

  // 8. Rola até Acomodações
  console.log('Gravando cena 7: Seção Acomodações...');
  await smoothScroll(750, 25);
  await animateTo(400, 450, 14);
  for (let i = 0; i < 10; i++) await captureFrame();
  await animateTo(850, 450, 14);
  for (let i = 0; i < 10; i++) await captureFrame();

  // 9. Rola até a Seção 10: Condições Exclusivas (Novo botão do WhatsApp)
  console.log('Gravando cena 8: Condições Exclusivas e WhatsApp CTA...');
  await smoothScroll(1100, 28);
  await animateTo(1050, 420, 16);
  await page.evaluate(() => window.triggerClick());
  for (let i = 0; i < 20; i++) await captureFrame();

  // 10. Rola até o Rodapé
  console.log('Gravando cena 9: Rodapé...');
  await smoothScroll(600, 20);
  for (let i = 0; i < 15; i++) await captureFrame();

  console.log(`Gravação finalizada com sucesso! Total de frames capturados: ${frameCount}`);
  await browser.close();
}

run().catch(err => {
  console.error('Erro na gravação:', err);
  process.exit(1);
});
