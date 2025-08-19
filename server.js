// server.js
import express from "express";
import puppeteer from "puppeteer";
import cors from "cors";

const app = express();
app.use(cors());
app.use(express.json());

app.post("/generate-pdf", async (req, res) => {
  try {
    const { html } = req.body;
    if (!html) throw new Error("لا يوجد HTML");
    
    const browser = await puppeteer.launch({ args: ["--no-sandbox"] });
    const page = await browser.newPage();
    await page.setContent(html, { waitUntil: "networkidle0" });
    const pdfBuffer = await page.pdf({ format: "A4" });
    await browser.close();

    res.set({
      "Content-Type": "application/pdf",
      "Content-Disposition": `attachment; filename="quote.pdf"`
    });
    res.send(pdfBuffer);
  } catch (err) {
    console.error("❌ Puppeteer error:", err);
    res.status(500).send("خطأ في السيرفر");
  }
});


app.listen(4000, () => console.log("🚀 Server running on http://localhost:4000"));
