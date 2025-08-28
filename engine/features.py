from  playsound import playsound
import eel

#playing assitant sound function
@eel.expose
def playAssistantSound():
    music_dir="www\\assets\\img\\audio\\start_sound.mp3"
    playsound(music_dir)