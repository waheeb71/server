# PDF Quote Generator Backend

This repository contains the **backend** for a simple web application that generates PDF reports from quote data. The backend is responsible for converting HTML content received from the frontend into downloadable PDF files.

## Overview

- Receive HTML content from the frontend.
- Convert HTML into professional PDF reports using **WeasyPrint**.
- Return the PDF file for download.
- Supports custom styles, Base64 images, and proper formatting.

## Live Demo

The backend is hosted on **Render** (free tier). It exposes an endpoint that accepts HTML and returns a PDF:  

**Endpoint:** `https://server-bd2c.onrender.com/generate-pdf`  

## Frontend Integration

The frontend (hosted on **Netlify**, free tier) sends HTML content to this backend.  
For example, the React app constructs the quote HTML and sends it as JSON to the backend endpoint:

```javascript
await fetch("https://server-bd2c.onrender.com/generate-pdf", {
  method: "POST",
  headers: { "Content-Type": "application/json" },
  body: JSON.stringify({ html: htmlContent }),
});

---
##  Contact:
For questions or support, contact me via:
- Telegram: [@SyberSc71](https://t.me/SyberSc71)
- Telegram: [@WAT4F](https://t.me/WAT4F)
- GitHub: [waheeb71](https://github.com/waheeb71)
- GitHub2: [cyberlangdev](https://github.com/cyberlangdev)
- **Location:** I am from Yemen, Taiz.
- **YouTube Channel:** [Cyber Code](https://www.youtube.com/@cyber_code1)
- **X (formerly Twitter):** [@wa__cys](https://x.com/wa__cys)

---
## Author / المطور

**English:** Waheeb Mahyoob Al-Sharabi (Waheeb Al-Sharabi)  
**العربية:** هيب مهيوب الشرعبي (هيب الشرعبي)
