from chord_identifier import sharp_octave  # octave, flat_octave,

chromatic_formula = [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
major_formula = [0, 2, 2, 1, 2, 2, 2, 1]
natural_Minor_formula = [0, 2, 3, 5, 7, 8, 10, 12]

scales = {'chromatic': chromatic_formula, 'major': major_formula, 'natural minor': natural_Minor_formula}
def convert_name(name):
    name = name.split()
    if 'Major' in name:
        return name[0], major_formula
    elif 'Minor' in name:
        return name[0], natural_Minor_formula

def unpack_scale(root_note, formula):
    root_pos = sharp_octave.index(root_note)
    scale = []
    y = 0
    for x in formula:
        y += x
        scale.append(sharp_octave[y + root_pos])
    return scale
    #return [sharp_octave[x + root_pos] for x in formula]


print(unpack_scale('C', chromatic_formula))
#print(unpack_scale(*convert_name('C# Major')))
