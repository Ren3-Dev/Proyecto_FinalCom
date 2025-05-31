from flask import Flask, request, jsonify
import subprocess
import os
import uuid

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

    resultado = subprocess.run(['./Poyecto_FinalCom', ruta], capture_output=True, text=True)
    return resultado.stdout + resultado.stderr

@app.route('/guardar_y_compilar', methods=['POST'])
def guardar_y_compilar():
    datos = request.get_json()
    contenido = datos.get('codigo', '')
    nombre_archivo = f"uploads/temp_{uuid.uuid4().hex}.ml"
    with open(nombre_archivo, 'w') as f:
        f.write(contenido)

    resultado = subprocess.run(['./Poyecto_FinalCom', nombre_archivo], capture_output=True, text=True)
    salida = resultado.stdout + resultado.stderr

    asm = traducir_a_ensamblador(resultado.stdout)
    return f"--- SALIDA COMPILADOR ---\n{salida}\n\n--- ENSAMBLADOR GENERADO ---\n{asm}"

def traducir_a_ensamblador(codigo_tres_direcciones):
    instrucciones = codigo_tres_direcciones.strip().split('\n')
    ensamblador = []

    for linea in instrucciones:
        if "=" in linea:
            partes = linea.split("=")
            izquierda = partes[0].strip()
            derecha = partes[1].strip()

            if "+" in derecha:
                op1, op2 = map(str.strip, derecha.split("+"))
                ensamblador.append(f"MOV AX, [{op1}]")
                ensamblador.append(f"ADD AX, [{op2}]")
                ensamblador.append(f"MOV [{izquierda}], AX")

            elif "-" in derecha:
                op1, op2 = map(str.strip, derecha.split("-"))
                ensamblador.append(f"MOV AX, [{op1}]")
                ensamblador.append(f"SUB AX, [{op2}]")
                ensamblador.append(f"MOV [{izquierda}], AX")

            elif "*" in derecha:
                op1, op2 = map(str.strip, derecha.split("*"))
                ensamblador.append(f"MOV AX, [{op1}]")
                ensamblador.append(f"MOV BX, [{op2}]")
                ensamblador.append(f"MUL BX")
                ensamblador.append(f"MOV [{izquierda}], AX")

            elif "/" in derecha:
                op1, op2 = map(str.strip, derecha.split("/"))
                ensamblador.append(f"MOV AX, [{op1}]")
                ensamblador.append(f"MOV BX, [{op2}]")
                ensamblador.append(f"DIV BX")
                ensamblador.append(f"MOV [{izquierda}], AX")

            else:
                ensamblador.append(f"MOV [{izquierda}], [{derecha}]")

        elif linea.startswith("call input"):
            ensamblador.append("; llamada a input")

        elif linea.startswith("call output"):
            ensamblador.append("; llamada a output")

        else:
            ensamblador.append(f"; {linea}")

    return "\n".join(ensamblador)

if __name__ == '__main__':
    app.run(debug=True)
