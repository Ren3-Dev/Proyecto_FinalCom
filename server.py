from flask import Flask, request, send_from_directory
import subprocess
import os

app = Flask(__name__, static_folder="public")
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/')
def index():
    return app.send_static_file('index.html')

@app.route('/style.css')
def style():
    return app.send_static_file('style.css')

@app.route('/compilar', methods=['POST'])
def compilar():
    archivo = request.files['archivo']
    ruta = os.path.join(UPLOAD_FOLDER, archivo.filename)
    archivo.save(ruta)

    # Ejecutar el compilador
    resultado = subprocess.run(['./Poyecto_FinalCom', ruta], capture_output=True, text=True)
    return resultado.stdout + resultado.stderr

if __name__ == '__main__':
    app.run(debug=True)
