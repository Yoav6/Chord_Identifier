from typing import List

octave = ['C', 'C#/D♭', 'D', 'D#/E♭', 'E', 'F', 'F#/G♭', 'G', 'G#/A♭', 'A', 'A#/B♭', 'B']
sharp_octave = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
                #'C2', 'C#2', 'D2', 'D#2', 'E2', 'F2', 'F#2', 'G2', 'G#2', 'A2', 'A#2', 'B2']
flat_octave = ['C', 'Db', 'D', 'Eb', 'E', 'F', 'Gb', 'G', 'Ab', 'A', 'Bb', 'B']
                #'C2', 'C#2', 'D2', 'D#2', 'E2', 'F2', 'F#2', 'G2', 'G#2', 'A2', 'A#2', 'B2']

quality_intervals = {'M': [4, 3], 'm': [3, 4], 'dim': [3, 3], 'aug': [4, 4],
                     'sus4': [5, 2], 'sus2': [2, 5]}
#[['M', [4, 3]], ['m', [3, 4]], ['dim', [3, 3]], ['aug', [4, 4]], ['sus4', [5, 2]], ['sus2', [2, 5]]]
#  'Major': [4, 3], 'Minor': [3, 4], 'Diminished': [3, 3], 'Augmented': [3, 3], 'Sus4': [5, 2], 'Sus2': [2, 5]
extensions_intervals = {'7': [3], "maj7": [4]}

def filter_dupes(arr):
    return list(dict.fromkeys(arr))

def note_index(note):
    return sharp_octave.index(note) if note in sharp_octave else flat_octave.index(note)

def convert(notes):
    """Takes list of note names and converts them to indices"""
    indices = [note_index(note) for note in filter_dupes(notes)]
    return indices

def mod_distance(x: int, y: int, mod=12):
    if y >= mod:
        raise ValueError("'Y' cannot be larger than or equal to 'mod'")
    return mod - x + y if x > y else y - x

def get_intervals(notes):
    #print(notes)
    """Takes a list of note indices and returns a list of intervals between each pair.
    assuming ordering from lowest to highest note"""
    return [mod_distance(y, notes[x+1]) for x, y in enumerate(notes[:-1])]

def get_all_inversions(notes):
    note_count = len(notes)
    notes = sorted(notes)
    notes += [x + 12 for x in notes]
    return [notes[x:x + note_count] for x in range(note_count)]

def find_base_pos(notes: List[int]):
    """Takes indices of notes and returns the smallest or largest arrangement"""
    note_count = len(notes)
    notes = sorted(notes) * 2
    intervals = get_intervals(notes)
    intervals = [sum(intervals[x:x + note_count - 1]) for x in range(note_count + 1)]
    interval_index = intervals.index(min(intervals)) if note_count < 4 else intervals.index(max(intervals))
    return notes[interval_index:interval_index + note_count]

"""def find_root(base_pos_notes, invert_pos_notes=None):
    base_root = base_pos_notes[0]
    if not invert_pos_notes:
        return [base_root] * 2
    else:
        root_index = base_root
        in_base_pos = note_index(notes[0]) == root_index
        root = notes[0] if in_base_pos else sharp_octave[root_index].replace("b", "♭")"""

"""def find_root(notes):
    #takes list of note indices and returns the name of the first one
    note = notes[0]
    return sharp_octave[note] if '#' in note else flat_octave[note]"""

def interval_to_quality(interval):
    for quality, test_interval in quality_intervals.items():
        if interval[0:2] == test_interval:
            for extension, test_interval in extensions_intervals.items():
                if interval[2:] == test_interval:
                    return quality, extension
            return quality, ''
    return '', ''

def notes_to_chord(notes):
    notes = notes.split()
    converted = convert(notes)
    base_pos = find_base_pos(converted)
    #print(get_all_inversions(converted))
    intervals = get_intervals(base_pos)
    #print(intervals)
    quality, extension = interval_to_quality(intervals)
    if quality:
        quality = quality.replace("M", "")
        in_base_pos = converted[0] == base_pos[0]
        root = notes[0] if in_base_pos else sharp_octave[base_pos[0]].replace("b", "♭")
        inversion = '/' + notes[0] if not in_base_pos else ''
        #print(converted, root, intervals)
        #print(*notes, '-->')
        return f'{root}{quality}{extension}{inversion}'
    else:
        #print('Unrecognized Chord')
        return None

if __name__ == '__main__':
    print(notes_to_chord('C Eb Gb'))
    #notes = 'A C F'  # input('Insert 3 notes from lowest to highest (example: "C Eb G": ') #A C F
