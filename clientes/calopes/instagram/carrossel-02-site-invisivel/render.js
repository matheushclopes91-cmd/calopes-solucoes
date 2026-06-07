const playwright = require('playwright');
const path = require('path');
const fs = require('fs');

(async () => {
  const browser = await playwright.chromium.launch();
  const page = await browser.newPage({
    viewport: { width: 1080, height: 1350 }
  });

  const htmlPath = path.join(__dirname, 'carrossel.html');
  await page.goto(`file://${htmlPath}`, { waitUntil: 'networkidle' });

  // Criar pasta instagram se não existir
  const instagramDir = path.join(__dirname, 'instagram');
  if (!fs.existsSync(instagramDir)) {
    fs.mkdirSync(instagramDir, { recursive: true });
  }

  // Renderizar cada slide
  const slides = await page.$$('.slide');
  console.log(`Encontrados ${slides.length} slides. Renderizando...`);

  for (let i = 0; i < slides.length; i++) {
    const slide = slides[i];
    const slideNum = String(i + 1).padStart(2, '0');
    const outputPath = path.join(instagramDir, `slide-${slideNum}.png`);

    await slide.screenshot({ path: outputPath });
    console.log(`✓ Slide ${slideNum} salvo: ${outputPath}`);
  }

  await browser.close();
  console.log(`\n✅ Todos os ${slides.length} slides foram renderizados com sucesso!`);
  console.log(`Pasta: ${instagramDir}`);
})();
