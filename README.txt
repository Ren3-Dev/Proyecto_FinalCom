# Proyecto Final de Compiladores – BMLang

Compilador para el lenguaje **BMLang** desarrollado en Flex, Bison y C. Incluye una interfaz web con Flask para subir archivos `.ml` y ver el código de tres direcciones generado.

## 🧠 Requisitos

- Ubuntu / WSL
- `make`, `flex`, `bison`, `gcc`
- Python 3 + Flask

### Instalar dependencias (si aún no están):

```bash
sudo apt update
sudo apt install flex bison gcc make python3-venv

🚀 Cómo ejecutar el proyecto

1. Clonar el repositorio
git clone https://github.com/tu-usuario/Proyecto_FinalCom.git
cd Proyecto_FinalCom

2. Crear y activar el entorno virtual
python3 -m venv venv
source venv/bin/activate

3. Instalar Flask
pip install flask

4. Compilar el compilador
make

5. Ejecutar el servidor web
python server.py

Abrir navegador en: http://localhost:5000



📂 Estructura del proyecto
lexer.l – Analizador léxico

parser.y – Analizador sintáctico y generador de código intermedio

main.c – Enlace entre parser y archivo fuente

server.py – Interfaz Flask

public/index.html – Interfaz web

uploads/ – Archivos temporales

README.md – Este documento


Proyecto_FinalCom/   
├── lexer.l
├── parser.y
├── main.c
├── Makefile
├── server.py
├── public/
│   ├── index.html
│   └── style.css
├── uploads/
├── ejemplo.ml
├── README.md  👈
└── venv/ (NO se sube, se ignora con .gitignore)


Agradecimientos al gato de Augusto que lo acompaño en todo el desrollo
