import os
from flask import Flask, request, send_file
from PIL import Image, ImageDraw, ImageFont
from io import BytesIO

app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
app = Flask(__name__)

def generate_image(ip):
    # Create an image with white background
    img = Image.new('RGB', (200, 100), color = (255, 255, 255))
    d = ImageDraw.Draw(img)
    
    # Load a font (standard PIL fonts or load from file)
    font = ImageFont.load_default()
    
    # Insert the IP address in the image
    d.text((10,40), ip, fill=(0, 0, 0), font=font)
    
    # Save the image to a BytesIO object
    img_io = BytesIO()
    img.save(img_io, 'PNG')
    img_io.seek(0)  # Move to the beginning of the stream
    
    return img_io

@app.route('/')
def home():
    ip = request.remote_addr  # Get visitor's IP address
    img_io = generate_image(ip)  # Generate an image from the IP address
    return send_file(img_io, mimetype='image/png', as_attachment=False)

if __name__ == '__main__':
    app.run(debug=True)
