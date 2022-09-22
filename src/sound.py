import os
import random

os.chdir("C:\shihan-work\Python Projects\PerfectPitchTrainer\Assets\sounds\piano")

notes = [
    'A2', 'A3', 'A4', 'A5', 'A6', 'A7',
    'B2', 'B3', 'B4', 'B5', 'B6', 'B7',
    'C2', 'C3', 'C4', 'C5', 'C6', 'C7',
    'D2', 'D3', 'D4', 'D5', 'D6', 'D7',
    'E2', 'E3', 'E4', 'E5', 'E6', 'E7',
    'F2', 'F3', 'F4', 'F5', 'F6', 'F7',
    'G2', 'G3', 'G4', 'G5', 'G6', 'G7',
    'A#2', 'A#3', 'A#4', 'A#5', 'A#6', 'A#7',
    'C#2', 'C#3', 'C#4', 'C#5', 'C#6', 'C#7',
    'D#2', 'D#3', 'D#4', 'D#5', 'D#6', 'D#7',
    'F#2', 'F#3', 'F#4', 'F#5', 'F#6', 'F#7',
    'G#2', 'G#3', 'G#4', 'G#5', 'G#6', 'G#7',

]

def pick_random_easy(current_note, current_instrument):
    note_index = random.randint(12, 41)
    note_prefix = notes[note_index]
    current_note = note_prefix + ".mp3"
    return current_note

def pick_random_medium(current_note):
    note_index = random.randint(0, 41)
    note_prefix = notes[note_index]
    current_note = note_prefix + ".mp3"
    return current_note

def pick_random_hard(current_note):
    note_index = random.randint(0, 71)
    note_prefix = notes[note_index]
    current_note = note_prefix + ".mp3"
    return current_note
