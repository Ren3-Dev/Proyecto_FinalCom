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
            ensamblador.append("; llamada a input - código manual aquí")

        elif linea.startswith("call output"):
            ensamblador.append("; llamada a output - código manual aquí")

        else:
            ensamblador.append(f"; instrucción no reconocida: {linea}")

    return "\n".join(ensamblador)
