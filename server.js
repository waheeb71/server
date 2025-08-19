import express from "express";
import puppeteer from "puppeteer";
import cors from "cors";

const app = express();
app.use(cors());
app.use(express.json());

app.post("/generate-pdf", async (req, res) => {
  try {
    const { html } = req.body;

    // 🟢 فتح المتصفح
    const browser = await puppeteer.launch({
      headless: "new",
      args: [
        "--no-sandbox",
        "--disable-setuid-sandbox",
        "--disable-dev-shm-usage",
        "--single-process",
        "--no-zygote",
      ],
      executablePath: process.env.PUPPETEER_EXECUTABLE_PATH || puppeteer.executablePath(),
    });

    const page = await browser.newPage();

    // 🟢 تحميل المحتوى مع DOMContentLoaded لتجنب مشاكل الشبكة
    await page.setContent(html, { waitUntil: "domcontentloaded" });

    // 🟢 توليد PDF
    const pdfBuffer = await page.pdf({ format: "A4" });

    await browser.close();

    res.set({
      "Content-Type": "application/pdf",
      "Content-Disposition": "attachment; filename=quote.pdf",
    });
    res.send(pdfBuffer);

  } catch (err) {
    // 🟢 طباعة الخطأ الكامل في logs
    console.error("❌ PDF generation error:", err);
    res.status(500).send(`Error generating PDF: ${err.message}`);
  }
});

// Render يعطي PORT
const PORT = process.env.PORT || 4000;
app.listen(PORT, () =>
  console.log(`🚀 Server running on http://localhost:${PORT}`)
);
