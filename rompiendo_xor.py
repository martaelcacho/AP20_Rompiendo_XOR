import ast


def obtener_clave(texto_cifrado, texto_conocido):

    clave_parcial = ""

    for indice in range(len(texto_conocido)):

        num_cifrado = texto_cifrado[indice]
        num_plano = ord(texto_conocido[indice])

        # XOR para descubrir la clave
        num_clave = num_cifrado ^ num_plano

        letra_clave = chr(num_clave)

        clave_parcial += letra_clave

    return clave_parcial


def encontrar_patron(clave_parcial):

    for longitud in range(1, len(clave_parcial) + 1):

        patron = clave_parcial[:longitud]

        coincide = True

        for indice in range(len(clave_parcial)):

            if clave_parcial[indice] != patron[indice % longitud]:
                coincide = False
                break

        if coincide:
            return patron

    return clave_parcial


def descifrar_xor(texto_cifrado, clave):

    texto_plano = ""

    for indice in range(len(texto_cifrado)):

        num_cifrado = texto_cifrado[indice]

        letra_clave = clave[indice % len(clave)]
        num_clave = ord(letra_clave)

        # XOR para descifrar
        num_descifrado = num_cifrado ^ num_clave

        letra_descifrada = chr(num_descifrado)

        texto_plano += letra_descifrada

    return texto_plano


if __name__ == "__main__":

    entrada = input(
        "Introduce el texto cifrado: "
    )

    texto_cifrado = ast.literal_eval(entrada)

    texto_conocido = input(
        "Introduce el inicio conocido del mensaje : "
    )

    clave_parcial = obtener_clave(
        texto_cifrado,
        texto_conocido
    )

    print("\nClave parcial encontrada:", repr(clave_parcial))

    clave = encontrar_patron(clave_parcial)

    print("Posible clave:", repr(clave))

    texto_plano = descifrar_xor(
        texto_cifrado,
        clave
    )

    print("\nTexto plano:", texto_plano)