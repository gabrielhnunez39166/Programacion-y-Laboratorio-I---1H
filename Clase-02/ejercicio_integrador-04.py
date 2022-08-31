'''
Hugo Gabriel Nunez

Ejercicio Integrador 04

Preparando todo para reclutar héroes y heroínas para la liga de la justicia, el departamento de HR dispone de una larga lista de justicieros pero solo tiene información detallada de algunos de ellos.
Es por eso que te piden que desarrolles un pequeño programa el cual basado en la lista 'heroes_para_reclutar' busque en el diccionario 'heroes_info' los que coincidan y los guarde en un nuevo diccionario para luego imprimir por consola todos sus datos. (id, origen, etc)
TIP: Las habilidades están repetidas, busca la manera de que en el resultado final no existan duplicados, que usarías para eso?


Ejemplo de la profe

#creo uno vacio
mi_diccionario = {}

#creo definiendo sus claves y valores
mi_diccionario_dos = {"Clave":"valor", "diccionario":heroes_info["Shazam"]["ID"],"habiliades":heroes_info["Shazam"]["Habilidades"]}

#agrego una clave y su valor a un diccionario vacio
mi_diccionario["id"] = 25

mi_diccionario_dos["pepe"] = heroes_info["Shazam"]
mi_diccionario_dos["ID"] =heroes_info["Shazam"]["ID"]
mi_diccionario_dos["Habilidades"] =heroes_info["Shazam"]["Habilidades"]

'''

heroes_para_reclutar = [
    "Batman", "BatWoman", "BatGirl",
    "Wonder Woman", "Aquaman", "Shazam",
    "Superman", "Super Girl", "Power Girl"
]
 
heroes_info = {
    "Super Girl": {
        "ID": 1,
        "Origen": "Krypton",
        "Habilidades": ["Volar", "Fuerza", "Velocidad", "Volar", "Fuerza", "Velocidad"],
        "Identidad": "Kara Zor-El"
    },
    "Shazam": {
        "ID": 25,
        "Origen": "Tierra",
        "Habilidades": ["Volar", "Fuerza", "Velocidad", "Magia", "Fuerza", "Velocidad"],
        "Identidad": "Billy Batson"
    },
    "Power Girl": {
        "ID": 14,
        "Origen": "Krypton",
        "Habilidades": ["Volar", "Fuerza", "Congelar", "Congelar", "Congelar"],
        "Identidad": "Karen Starr"
    },
    "Wonder Woman": {
        "ID": 29,
        "Origen": "Amazonia",
        "Habilidades": ["Agilidad", "Fuerza", "Lazo de la verdad", "Escudo"],
        "Identidad": "Diana Prince"
    }
}

#print(heroes_para_reclutar)
#print(heroes_info)

for heroe in heroes_info:
    for nombre in heroes_para_reclutar:
        if (heroe == nombre):
            caracteristicas_reclutado = {
            "ID": heroes_info[nombre]["ID"],
            "Origen": heroes_info[nombre]["Origen"],
            "Habilidades": heroes_info[nombre]["Habilidades"],
            "Identidad": heroes_info[nombre]["Identidad"],
            }

print(caracteristicas_reclutado)