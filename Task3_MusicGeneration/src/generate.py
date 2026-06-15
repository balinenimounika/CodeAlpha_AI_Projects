import pickle
import random
import torch
import torch.nn as nn

from music21 import note
from music21 import chord
from music21 import stream

SEQUENCE_LENGTH = 50
HIDDEN_SIZE = 256

checkpoint = torch.load(
    "models/music_model.pth"
)

pitchnames = checkpoint["pitchnames"]

note_to_int = checkpoint["note_to_int"]

int_to_note = {
    v: k for k, v in note_to_int.items()
}

VOCAB_SIZE = len(pitchnames)

class MusicLSTM(nn.Module):

    def __init__(self, vocab_size):

        super().__init__()

        self.embedding = nn.Embedding(
            vocab_size,
            128
        )

        self.lstm = nn.LSTM(
            128,
            HIDDEN_SIZE,
            num_layers=2,
            batch_first=True
        )

        self.fc = nn.Linear(
            HIDDEN_SIZE,
            vocab_size
        )

    def forward(self, x):

        x = self.embedding(x)

        out, _ = self.lstm(x)

        out = self.fc(out[:, -1, :])

        return out

model = MusicLSTM(VOCAB_SIZE)

model.load_state_dict(
    checkpoint["model_state_dict"]
)

model.eval()

with open("data/notes.pkl", "rb") as f:
    notes = pickle.load(f)

start = random.randint(
    0,
    len(notes) - SEQUENCE_LENGTH - 1
)

pattern = notes[
    start:start + SEQUENCE_LENGTH
]

prediction_output = []

print("Generating Music...")

for _ in range(500):

    input_seq = [
        note_to_int[n]
        for n in pattern
    ]

    input_tensor = torch.tensor(
        [input_seq],
        dtype=torch.long
    )

    with torch.no_grad():

        prediction = model(input_tensor)

        index = torch.argmax(
            prediction
        ).item()

    result = int_to_note[index]

    prediction_output.append(result)

    pattern.append(result)

    pattern = pattern[1:]

offset = 0
output_notes = []

for pattern in prediction_output:

    if '.' in pattern or pattern.isdigit():

        notes_in_chord = pattern.split('.')

        chord_notes = []

        for current_note in notes_in_chord:

            new_note = note.Note(
                int(current_note)
            )

            chord_notes.append(
                new_note
            )

        new_chord = chord.Chord(
            chord_notes
        )

        new_chord.offset = offset

        output_notes.append(
            new_chord
        )

    else:

        new_note = note.Note(
            pattern
        )

        new_note.offset = offset

        output_notes.append(
            new_note
        )

    offset += 0.5

midi_stream = stream.Stream(
    output_notes
)

import time

filename = f"generated_music/output_{int(time.time())}.mid"

midi_stream.write(
    "midi",
    fp=filename
)

print("Music Generated Successfully!")
print("Saved:", filename)