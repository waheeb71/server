from flask import Flask, request, send_file
from weasyprint import HTML, CSS
import io
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/generate-pdf', methods=['POST'])
def generate_pdf():
    try:
        data = request.json
        html_content = data.get('html', '<h1>Empty</h1>')

        # أضف العلامة المائية مباشرة في HTML باستخدام div
        watermark_html = '''
        <div style="
            position: fixed;
            top: 50%;
            left: 50%;
            width: 300px;
            height: 300px;
            margin-left: -150px;
            margin-top: -150px;
            background-image: url('https://raw.githubusercontent.com/waheeb71/server/main/watermark.png');
            background-size: contain;
            background-repeat: no-repeat;
            opacity: 0.1;
            z-index: -1000;
        "></div>
        '''

        final_html = watermark_html + html_content

        pdf_file = io.BytesIO()
        HTML(string=final_html).write_pdf(pdf_file)
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
