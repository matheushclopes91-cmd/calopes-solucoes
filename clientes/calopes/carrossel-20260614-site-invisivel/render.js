const { chromium } = require('playwright');
const fs = require('fs');
const path = require('path');

async function renderCarrossel() {
  const browser = await chromium.launch();
  const page = await browser.newPage();

  // Usar caminho relativo ao script
  const htmlPath = path.join(__dirname, 'carrossel.html');
  const fileUrl = `file://${htmlPath.replace(/\\/g, '/')}`;

  await page.goto(fileUrl, { waitUntil: 'networkidle' });

  // Selecionar todos os slides
  const slides = await page.locator('.slide').all();
  const slideCount = slides.length;

  // Criar pasta instagram se não existir
  const instagramDir = path.join(__dirname, 'instagram');
  if (!fs.existsSync(instagramDir)) {
    fs.mkdirSync(instagramDir, { recursive: true });
  }

  // Renderizar cada slide
  for (let i = 0; i < slideCount; i++) {
    const slide = slides[i];
    const slideNumber = String(i + 1).padStart(2, '0');
    const outputPath = path.join(instagramDir, `slide-${slideNumber}.png`);

    // Scroll para o slide
    await slide.scrollIntoViewIfNeeded();

    // Screenshot
    await slide.screenshot({ path: outputPath });
    console.log(`✓ Renderizado: slide-${slideNumber}.png`);
  }

  await browser.close();
  console.log(`\n✓ Carrossel completo! ${slideCount} slides renderizados em instagram/`);
}

renderCarrossel().catch(console.error);
