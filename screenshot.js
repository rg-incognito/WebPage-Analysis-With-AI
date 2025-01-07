const puppeteer = require('puppeteer-extra');
const StealthPlugin = require('puppeteer-extra-plugin-stealth');
puppeteer.use(StealthPlugin());

const url = process.argv[2];
const timeout = 10000;

(async () => {
    const browser = await puppeteer.launch( {
        headless: "new",
    } );

    const page = await browser.newPage();

    await page.setViewport( {
        width: 800,
        height: 1200,
        deviceScaleFactor: 2,
    } );

    await page.goto( url, {
        waitUntil: 'domcontentloaded',
        timeout: timeout,
    } );
    await new Promise(resolve => setTimeout(resolve, timeout));

    await page.screenshot( {
        path: "screenshot.jpg",
        fullPage: true,
        quality: 100,
    } );

    await browser.close();
})();