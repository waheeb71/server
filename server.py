from flask import Flask, request, send_file
from weasyprint import HTML, CSS
import io
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # للسماح بالطلبات من React

@app.route('/generate-pdf', methods=['POST'])
def generate_pdf():
    try:
        data = request.json
        html_content = data.get('html', '<h1>Empty</h1>')

        # CSS لإضافة العلامة المائية في منتصف الصفحة
        watermark_css = CSS(string='''
            @page {
                size: A4;
            }
            body::after {
                content: "";
                position: fixed;
                top: 50%;
                left: 50%;
                width: 300px;  /* حجم العلامة المائية */
                height: 300px;
                margin-left: -150px;  /* نصف العرض */
                margin-top: -150px;   /* نصف الطول */
                background-image: url('https://quotes553.netlify.app/watermark.png');
                background-repeat: no-repeat;
                background-position: center;
                background-size: contain;
                opacity: 0.1;  /* شفافية العلامة المائية */
                z-index: -1;
            }
        ''')

        # تحويل HTML إلى PDF بحجم A4 مع العلامة المائية
        pdf_file = io.BytesIO()
        HTML(string=html_content).write_pdf(pdf_file, stylesheets=[watermark_css])
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
