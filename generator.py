import random

notes = {
    0: "C",
    1: "C#",
    2: "D",
    3: "Eb",
    4: "E",
    5: "F",
    6: "F#",
    7: "G",
    8: "G#",
    9: "A",
    10: "Bb",
    11: "B"
}

chords = {}

for i in range(12):
    chords["[{}, {}, {}]".format(i, (i+4) % 12, (i+7) % 12)] = notes[i]
    chords["[{}, {}, {}]".format(i, (i+3) % 12, (i+7) % 12)] = notes[i] + "m"
    chords["[{}, {}, {}, {}]".format(i, (i+4) % 12, (i+7) % 12, (i+10) % 12)] = notes[i] + "7"
    chords["[{}, {}, {}, {}]".format(i, (i+3) % 12, (i+7) % 12, (i+10) % 12)] = notes[i] + "m7"
    chords["[{}, {}, {}, {}]".format(i, (i+4) % 12, (i+7) % 12, (i+11) % 12)] = notes[i] + "maj7"
    chords["[{}, {}, {}, {}]".format(i, (i+3) % 12, (i+6) % 12, (i+9) % 12)] = notes[i] + "dim7"
    # Add more chords


def mel_to_seq(melody):
    inv = {v: k for k, v in notes.items()}
    inv["Db"] = 1
    inv["D#"] = 3
    inv["Gb"] = 6
    inv["Ab"] = 8
    inv["A#"] = 10
    seq = [inv[j] for j in melody]
    return seq


def randhar(seq):
    harmonies = []
    for note in seq:
        candidates = []
        for chord in chords:
            if note in eval(chord):
                candidates.append(chords[chord])
        harmonies.append(random.choice(candidates))
    return harmonies


def randmel(length):
    seq = [random.randint(0, 11) for _ in range(length)]
    return [notes[j] for j in seq]
