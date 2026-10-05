# https://pynput.readthedocs.io/en/latest/keyboard-usage.html

from pynput import keyboard
import winsound

# Plays when the hotkey combination is activated
def on_activate():
    winsound.PlaySound("sound.wav", winsound.SND_ASYNC)

def for_canonical(f):
    return lambda k: f(l.canonical(k))

# Listens for hotkey combination
hotkey = keyboard.HotKey(
    keyboard.HotKey.parse('<ctrl>+h'),
    on_activate)
with keyboard.Listener(
        on_press=for_canonical(hotkey.press),
        on_release=for_canonical(hotkey.release)) as l:
    l.join()