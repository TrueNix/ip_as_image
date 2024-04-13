from flask import Flask, request, send_file
from PIL import Image, ImageDraw, ImageFont
from io import BytesIO

app = Flask(__name__)

def generate_image(ip):
    img = Image.new('RGB', (200, 100), color=(255, 255, 255))
    d = ImageDraw.Draw(img)
    font = ImageFont.load_default()
    d.text((10, 40), ip, fill=(0, 0, 0), font=font)
    img_io = BytesIO()
    img.save(img_io, 'PNG')
    img_io.seek(0)
    return img_io

@app.route('/')
def home():
    # Try to get the visitor's real IP from the 'X-Forwarded-For' header
    ip = request.headers.get('X-Forwarded-For', request.remote_addr)
    img_io = generate_image(ip)
    return send_file(img_io, mimetype='image/png', as_attachment=False)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)), debug=True)
