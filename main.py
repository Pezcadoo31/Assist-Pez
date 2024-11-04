from modules.talk import Talker
from modules.listen import Listener
from modules.Spotify import SpotifyPlayer
import datetime
from tkinter import * 
import pywhatkit
import openai
import pygame

pygame.init()
pygame.mixer.init()


prompt_setup = """Simula ser un asistente de voz que se llama Pez. 
Puedes reproducir musica, decir el dia, la hora y buscar en google, ademas de tener conversaciones con el usuario.
No es necesario que te presentes cada que hables.
Esto fue lo que te dijo el usuario: """

talker = Talker()
listener = Listener()
spotify_player = SpotifyPlayer(
    client_id='', 
    client_secret='', 
    redirect_uri='http://localhost:3036',
    scope='user-read-playback-state,user-modify-playback-state,streaming')

# Funcion principal
def run():
    try:
            sonido_fondo = pygame.mixer.Sound("placeholder.wav")
            pygame.mixer.Sound.play(sonido_fondo)
            response = listener.listen()
            response = response.upper()
            if ('REPRODUCE' in response):
                play_music(response)
            elif ('BUSCA' in response):
                 search_on_google(response)
            elif ('QUÉ HORA ES' in response):
                hora()
            elif ('QUÉ DÍA ES HOY' in response):
                fecha()
            elif ('SPOTIFY' in response):
                play_music_on_spotify(response.replace('SPOTIFY', '').strip(), spotify_player)
            elif ('HASTA LUEGO' in response):
                quit()
            elif ('TEST' in response):
                talker.talk("Este es un Test")
            else:
                chat(response)
    except Exception as e:
            print(f"Error: {e}")

# Funciones del Asistente
def play_music(res):
    music = res.replace('REPRODUCE', '')
    print("Reproduciendo" + music.lower())
    talker.talk("Reproduciendo " + music)
    pywhatkit.playonyt(music)

def search_on_google(res):
    pywhatkit.search(res)

def chat(res):
    completionChoices = completion = openai.ChatCompletion.create(
  model="gpt-3.5-turbo", 
  messages=[{"role": "user", "content": prompt_setup+res}]
).choices[0]
    completion=completionChoices['message']
    print(completion['content'])
    talker.talk(completion['content'])

def hora():
    hora = datetime.datetime.now().strftime("%H:%M")
    print("Son las " + hora)
    talker.talk("Son las " + hora)

def fecha():
    fecha = datetime.datetime.now().strftime("%d/%m/%Y")
    print("Hoy es " + fecha)
    talker.talk("Hoy es " + fecha)

# Funciones Extra

# Función para reproducir música en Spotify
def play_music_on_spotify(query, spotify_player):
    results = spotify_player.sp.search(q=query, limit=1)
    if results['tracks']['items']:
        track = results['tracks']['items'][0]
        spotify_player.sp.start_playback(uris=[track['uri']])
        talker.talk(f"Reproduciendo {track['name']} de {track['artists'][0]['name']}")
    else:
        talker.talk("No se encontró la canción en Spotify")

# GUI
root = Tk()
root.title("Pez")
root.geometry("700x800")
root.resizable(0,0)
root.configure(bg="#343140")
#root.attributes('-fullscreen', True) #Fullscreen, desactivar o activar segun conveniencia

# Titulo

label = Label(root, text="Pez", font=("Consolas", 70), bg="#343140", fg="white")
label.pack()


# Imagen de Pez
"""framesNum = 20 # Numero de frames que tiene el gif, si no lo conoces ir haciendo tentativos.
archivo = "pez.gif" """

# Imagen de Pez
archivo = "PEZ.png"  # Cambia este nombre al nombre de tu archivo PNG
frame = PhotoImage(file=archivo)

# Lista de todas las imagenes del gif
"""frames = [PhotoImage(file=archivo, format='gif -index %i' %(i)) for i in range(framesNum)]

def update(ind):
    """" Actualiza la imagen gif """"
    frame = frames[ind]
    ind += 1
    if ind == framesNum:
        ind = 0
    canvas.create_image(0, 0, image=frame, anchor=NW)
    root.after(80, update, ind) # Numero que regula la velocidad del gif 

canvas = Canvas(width=600, height=338, bg='#343140', highlightthickness=0) # Modificar segun el tamaño de la imagen
canvas.pack(pady=100)
root.after(0, update, 0) """

canvas = Canvas(width=600, height=338, bg='#343140', highlightthickness=0) # Modificar según el tamaño de la imagen
canvas.pack(pady=100)
canvas.create_image(0, 0, image=frame, anchor=NW)

# Escuchar
btnRun=Button(root,text="Escuchar", font=("Consolas", 30), bg='#f77e06', command=run)
btnRun.pack()

# Run
root.mainloop()
