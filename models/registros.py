from .persona import Persona

class Registros(object):
    personas = []

    def crearPersona(personaCrear):
        personaCrear.id = len(registros.personas) + 1
        registros.personas.append(personaCrear);
        return

    def getPersonas():
        return registros.personas

registros = Registros();