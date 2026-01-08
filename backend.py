from flask import Flask, send_from_directory, render_template, jsonify
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/<filename>')
def serve_file(filename):
    allowed_files = ['Sevgilim.mp3', 'yağmur.mp3']
    if filename in allowed_files:
        return send_from_directory('.', filename)
    else:
        return "Dosya bulunamadı", 404

@app.route('/health')
def health_check():
    """Render için health check endpoint"""
    return jsonify({"status": "healthy"}), 200

# Render için önemli: debug modu kapalı olmalı
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)
