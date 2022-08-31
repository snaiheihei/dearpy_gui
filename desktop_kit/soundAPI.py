from playsound2 import playsound
import threading
import os 
from pygame import mixer



def audio_effectsDispatcher(file_name):
    # 异步执行，主线程结束立刻结束
    play_audio_thread = threading.Thread(name="play_audio", target=play_audio, args=(file_name,), daemon=True)
    play_audio_thread.start()


def play_audio(file_name):
    folder = os.path.dirname(os.path.abspath("__file__"))
    playsound(os.path.join(folder, "sound", file_name))
    
def music_effectsDispatcher(file_name):
    # 异步执行，主线程结束立刻结束
    play_audio_thread = threading.Thread(name="play_music", target=play_music, args=(file_name,), daemon=True)
    play_audio_thread.start()


def play_music(file_name):
    folder = os.path.dirname(os.path.abspath("__file__"))
    mixer.init()
    mixer.music.set_volume(0.4)
    mixer.music.load(os.path.join(folder, "sound", file_name))
    mixer.music.play()

if __name__ == "__main__" :
    play_audio("theme.mp3")