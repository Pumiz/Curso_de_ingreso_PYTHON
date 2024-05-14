#Caso investigacion criminal

adn_sospechosos = [
    ["Juan Perez", "CGGGGCTAAAATTTTTTACGATCG"],
    ["Maria Rodriguez", "AACGTTTAATGTTCTAAGCTGCG"],
    ["Carlos Sanchez", "CGGGGCTAAAATTTTTTACGATCG"]
]

adn_escena_crimen = "CGTTTAATG"

def comprobar_combinacion(adn_sospechosos: str, adn_victima: str):
    # _descripcion_
    #
    #    Argumento:
    #      parametro [tipoDeDato] -> _description_
    #    Retorna:
    #      retorna -> _description_
    culpable = "Ninguno de los sospechosos"

    for i in range(len(adn_sospechosos)):
        if adn_victima in adn_sospechosos[i][1]:
            culpable = adn_sospechosos[i][0]

    return culpable

resultado = comprobar_combinacion(adn_sospechosos, adn_escena_crimen)

print(f"El resultado del estudio resulto que: {resultado} es el culpable")
