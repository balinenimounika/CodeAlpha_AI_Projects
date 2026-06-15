import glob
import pickle
from music21 import converter, instrument, note, chord

notes = []

print("Reading MIDI files...")

for file in glob.glob("data/midi_files/*.mid"):
    print("Processing:", file)

    midi = converter.parse(file)

    try:
        parts = instrument.partitionByInstrument(midi)
        notes_to_parse = parts.parts[0].recurse()

    except:
        notes_to_parse = midi.flat.notes

    for element in notes_to_parse:

        if isinstance(element, note.Note):
            notes.append(str(element.pitch))

        elif isinstance(element, chord.Chord):
            notes.append('.'.join(str(n) for n in element.normalOrder))

with open("data/notes.pkl", "wb") as f:
    pickle.dump(notes, f)

print(f"Total Notes Extracted: {len(notes)}")