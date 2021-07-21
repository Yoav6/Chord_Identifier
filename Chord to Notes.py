from chord_identifier import quality_intervals, sharp_octave, note_index, flat_octave  # octave


def is_note(note: str):
    return note in sharp_octave or note in flat_octave

def unpack_chord(chord):
    root_note = chord[0:2] if is_note(chord[0:2]) else chord[0] if is_note(chord[1]) else 'all'
    if '/' in chord:
        pos = chord.index('/') + 1
        inversion_note = chord[pos:pos+2] if is_note(chord[pos:pos+2]) else chord[pos]
    else:
        inversion_note = None
    for quality, interval in quality_intervals.items():
        if quality in chord:
            return root_note, interval, inversion_note
    print('Unrecognized interval, defaulting to Major')
    return root_note, quality_intervals['M'], inversion_note

def intervals_to_notes(root_note, intervals):
    root_note_index = note_index(root_note)
    other_notes = [sharp_octave[root_note_index + sum(intervals[:x+1])] for x in range(len(intervals))]
    return [root_note, *other_notes]

def chord_to_notes(chord):
    root_note, interval, inversion_note = unpack_chord(chord)
    notes = intervals_to_notes(root_note, interval)
    if inversion_note:
        notes.remove(inversion_note)
        notes = [inversion_note] + notes
    print(chord)
    print(root_note, interval, notes)
    return notes

if __name__ == '__main__':
    chord_to_notes('C#M/G#')
