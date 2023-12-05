import re

# Texto inicial
texto_inicial = """
        1 malwmrllpl lallalwgpd paaafvnqhl cgshlvealy lvcgergffy tpktrreaed
       61 lqvgqvelgg gpgagslqpl alegslqkrg iveqcctsic slyqlenycn
//"""

# Eliminar ORIGIN, números, barras diagonales, espacios y saltos de línea
texto_limpiado = re.sub(r'ORIGIN|\d+|//|\s', '', texto_inicial)

# Confirmar que el texto tiene 110 caracteres
if len(texto_limpiado) == 110:
    print("Texto limpiado con éxito:")
    print(texto_limpiado)
else:
    print("La longitud del texto limpiado no es 110 caracteres.")
