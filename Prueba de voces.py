import pyttsx3

engine = pyttsx3.init()

# Obtener todas las voces disponibles
voices = engine.getProperty('voices')

# Buscar una voz en español
spanish_voices = [voice for voice in voices if "spanish" in voice.languages]
if spanish_voices:
    # Configurar la primera voz en español encontrada
    engine.setProperty('voice', spanish_voices[0].id)
else:
    print("No se encontraron voces en español")

# Establecer la velocidad de habla
engine.setProperty('rate', 125)

# Función para hablar
def hablar(texto):
    engine.say(texto)
    engine.runAndWait()

# Ejemplo de uso
texto_a_decir = "Hola, ¿cómo estás?"
hablar(texto_a_decir)

