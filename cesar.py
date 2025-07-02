def cesar(mensaje, desplazamiento):
    resultado = ""

    # Recorrer cada carácter en el mensaje
    for i in range(len(mensaje)):
        char = mensaje[i]

        # Verificar si el carácter es una letra mayúscula
        if char.isupper():
            resultado += chr((ord(char) + desplazamiento - 65) % 26 + 65)
        # Verificar si el carácter es una letra minúscula
        elif char.islower():
            resultado += chr((ord(char) + desplazamiento - 97) % 26 + 97)
        else:
            resultado += char

    return resultado

mensage = "mensaje"
desplazamiento = 3
resultado = cesar(mensage, desplazamiento)
print(f"Mensaje original: {mensage}")
print(f"Mensaje cifrado: {resultado}")
mensage = "Mensaje con espacios y signos de puntuación!"