from flask import Flask, request, send_file
from weasyprint import HTML
import io
from flask_cors import CORS

import io
app = Flask(__name__)
CORS(app)  # للسماح بالطلبات من React

# ضع هنا Base64 للعلامة المائية

WATERMARK_PATH = os.path.join(app.root_path,'watermark.png')
@app.route('/generate-pdf', methods=['POST'])
def generate_pdf():
    try:
        data = request.json
        html_content = data.get('html', '<h1>Empty</h1>')

        # إضافة العلامة المائية
        html_with_watermark = f"""
        <div style="position: relative;">
            <img src="{WATERMARK_PATH}" 
                 style="position: absolute; top: 30%; left: 25%; width: 50%; opacity: 0.15; z-index: -1;" />
            {html_content}
        </div>
        """

        # تحويل HTML إلى PDF بحجم A4
        pdf_file = io.BytesIO()
        HTML(string=html_with_watermark).write_pdf(pdf_file)
        pdf_file.seek(0)

        return send_file(
            pdf_file,
            mimetype='application/pdf',
            as_attachment=True,
            download_name='quote.pdf'
        )
    except Exception as e:
        return {'error': str(e)}, 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
