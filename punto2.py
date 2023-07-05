class Superheroe:
    def __init__(self, superheroe, personaje, grupo, anio_aparicion):
        self.superheroe = superheroe
        self.personaje = personaje
        self.grupo = grupo
        self.anio_aparicion = anio_aparicion


class ListaAvengers:
    def __init__(self):
        self.superheroes = []

    def agregar_superheroe(self, superheroe):
        self.superheroes.append(superheroe)

    def capitana_marvel(self):
        for superhero in self.superheroes:
            if superhero.nombre_superheroe == "Capitana Marvel":
                return superhero.nombre_personaje
        return None

    def superheroes_guardianes_galaxia(self):
        cola_guardianes_galaxia = []
        for superhero in self.superheroes:
            if superhero.grupo == "Guardianes de la galaxia":
                cola_guardianes_galaxia.append(superhero)
        return cola_guardianes_galaxia

    def superheroes_grupo_descendente(self, grupos):
        superheroes_descendentes = []
        for grupo in grupos:
            for superhero in reversed(self.superheroes):
                if superhero.grupo == grupo:
                    superheroes_descendentes.append(superhero)
        return superheroes_descendentes

    def superheroes_nombre_personaje_posterior_1960(self):
        superheroes_posterior_1960 = []
        for superhero in self.superheroes:
            if superhero.nombre_personaje != "" and superhero.anio_aparicion > 1960:
                superheroes_posterior_1960.append(superhero)
        return superheroes_posterior_1960

    def corregir_nombre_black_widow(self):
        for superhero in self.superheroes:
            if superhero.nombre_superheroe == "Black Widow" and superhero.nombre_personaje == "Vlanck Widow":
                superhero.nombre_personaje = "Black Widow"
                break

    def agregar_personajes_auxiliares(self, personajes_auxiliares):
        for personaje in personajes_auxiliares:
            encontrado = False
            for superhero in self.superheroes:
                if superhero.nombre_superheroe == personaje[0]:
                    encontrado = True
                    break
            if not encontrado:
                self.superheroes.append(Superheroe(personaje[0], personaje[1], personaje[2], personaje[3]))

    def mostrar_personajes_inicio_cps(self):
        personajes_inicio_cps = []
        for superhero in self.superheroes:
            if superhero.nombre_personaje != "" and superhero.nombre_personaje[0] in ["C", "P", "S"]:
                personajes_inicio_cps.append(superhero)
        return personajes_inicio_cps


# Crear la lista de Avengers
lista_avengers = ListaAvengers()

# Cargar los superhéroes existentes
lista_avengers.agregar_superheroe(Superheroe("Capitana Marvel", "", "", 1976))
lista_avengers.agregar_superheroe(Superheroe("Star Lord", "Peter Quill", "Guardianes de la galaxia", 1976))
lista_avengers.agregar_superheroe(Superheroe("Black Widow", "Vlanck Widow", "", 1964))

# Determinar si "Capitana Marvel" está en la lista y mostrar su nombre de personaje
nombre_personaje_capitana_marvel = lista_avengers.buscar_capitana_marvel()
if nombre_personaje_capitana_marvel:
    print(f"El nombre de personaje de Capitana Marvel es: {nombre_personaje_capitana_marvel}")
else:
    print("Capitana Marvel no se encuentra en la lista.")

# Almacenar los superhéroes que pertenezcan al grupo "Guardianes de la galaxia" en una cola e indicar cuántos son
cola_guardianes_galaxia = lista_avengers.superheroes_guardianes_galaxia()
print(f"Hay {len(cola_guardianes_galaxia)} superhéroes en el grupo Guardianes de la galaxia.")

# Mostrar de manera descendente los superhéroes que pertenecen al grupo "Los cuatro fantásticos" y "Guardianes de la galaxia"
grupos_descendentes = ["Los cuatro fantásticos", "Guardianes de la galaxia"]
superheroes_grupo_descendente = lista_avengers.superheroes_grupo_descendente(grupos_descendentes)
print("Superhéroes de Los cuatro fantásticos y Guardianes de la galaxia en orden descendente:")
for superhero in superheroes_grupo_descendente:
    print(superhero.nombre_superheroe)

# Listar los superhéroes que tengan nombre de personajes cuyo año de aparición sea posterior a 1960
superheroes_posterior_1960 = lista_avengers.superheroes_nombre_personaje_posterior_1960()
print("Superhéroes con nombre de personaje posterior a 1960:")
for superhero in superheroes_posterior_1960:
    print(superhero.nombre_superheroe)

# Corregir el nombre de "Vlanck Widow" a "Black Widow"
lista_avengers.corregir_nombre_black_widow()
print("Se corrigió el nombre 'Vlanck Widow' a 'Black Widow'.")

# Agregar personajes auxiliares a la lista principal en caso de no estar cargados
personajes_auxiliares = [
    ("Black Cat", "", "", 1962),
    ("Hulk", "", "", 1958),
    ("Rocket Racoonn", "", "", 1982),
    ("Loki", "", "", 1978)
]
lista_avengers.agregar_personajes_auxiliares(personajes_auxiliares)
print("Se agregaron los personajes auxiliares a la lista principal.")

# Mostrar todos los personajes que comienzan con C, P o S
personajes_inicio_cps = lista_avengers.mostrar_personajes_inicio_cps()
print("Personajes que comienzan con C, P o S:")
for superhero in personajes_inicio_cps:
    print(superhero.nombre_personaje)

# Cargar al menos 20 superhéroes a la lista
superheroes_carga = [
    Superheroe("Spider-Man", "Peter Parker", "", 1962),
    Superheroe("Iron Man", "Tony Stark", "", 1963),
    Superheroe("Thor", "", "Avengers", 1962),
    Superheroe("Hulk", "Bruce Banner", "Avengers", 1962),
    Superheroe("Captain America", "Steve Rogers", "Avengers", 1941),
    Superheroe("Black Widow", "Natasha Romanoff", "Avengers", 1964),
    Superheroe("Hawkeye", "Clint Barton", "Avengers", 1964),
    Superheroe("Doctor Strange", "", "", 1963),
    Superheroe("Black Panther", "", "", 1966),
    Superheroe("Ant-Man", "", "", 1962),
    Superheroe("Wasp", "", "", 1963),
    Superheroe("Scarlet Witch", "", "", 1964),
    Superheroe("Vision", "", "", 1968),
    Superheroe("Falcon", "", "", 1969),
    Superheroe("Winter Soldier", "", "", 2005),
    Superheroe("War Machine", "", "", 1979),
    Superheroe("Spider-Woman", "", "", 1977),
    Superheroe("Ms. Marvel", "", "", 1977),
    Superheroe("Captain Marvel", "", "", 1968),
    Superheroe("Star-Lord", "Peter Quill", "Guardianes de la galaxia", 1976),
]

for superhero in superheroes_carga:
    lista_avengers.agregar_superheroe(superhero)

print("Se cargaron 20 superhéroes adicionales a la lista principal.")
print("/nLista de superheroes:")
for superhero in lista_avengers.superheroes:
    print(f"Superheroe: {superhero.nombre_superheroe}, Personaje: {superhero.nombre_personaje}, "f"Grupo: {superhero.grupo}, Anio de aparicion: {superhero.anio_aparicion}")