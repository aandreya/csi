print ("CSI program\n\n\n"
       "I bought a large container of icecream. But that turned out to be I SCREAM!\n"
       "Someone ate my whole container.\n\n"
       "The devil of the person was negligent enough, that he / she left a spoon in the container.\n"
       "I am totaly doing the DNA test on it!\n\nWe are lucky to have DNA database of our workforce, so perpetrators, beware!!!\n\n")

# DNA - characteristics
characteristics = {
    'hair_color': {
        'black': 'CCAGCAATCGC',
        'brown': 'GCCAGTGCCG',
        'blonde': 'TTAGCTATCGC'
    },
    'face_shape': {
        'square': 'GCCACGG',
        'round': 'ACCACAA',
        'oval': 'AGGCCTCA'
    },
    'eye_color': {
        'blue': 'TTGTGGTGGC',
        'green': 'GGGAGGTGGC',
        'brown': 'AAGTAGTGAC'
    },
    'gender': {
        'female': 'TGAAGGACCTTC',
        'male': 'TGCAGGAACTTC'
    },
    'race': {
        'white': 'AAAACCTCA',
        'black': 'CGACTACAG',
        'asian': 'CGCGGGCCG'
    }
}

# suspects - visual propreties
suspects = {
    'Eva': {
        'gender': 'female',
        'race': 'white',
        'hair_color': 'blonde',
        'eye_color': 'blue',
        'face_shape': 'oval'
    },
    'Larisa': {
        'gender': 'female',
        'race': 'white',
        'hair_color': 'brown',
        'eye_color': 'brown',
        'face_shape': 'oval'
    },
    'Matej': {
        'gender': 'male',
        'race': 'white',
        'hair_color': 'black',
        'eye_color': 'blue',
        'face_shape': 'oval'
    },
    'Miha': {
        'gender': 'male',
        'race': 'white',
        'hair_color': 'brown',
        'eye_color': 'green',
        'face_shape': 'square'
    }
}

# prebere obsojeco datoteko
dna_file = open('dna.txt', 'r')
dna = dna_file.read()
dna_file.close()

# sample DNA testing
guilty_party_attributes = {}
is_suspect_found = False

for (attribute_name, types) in characteristics.items():
    for (type_name, type_value) in types.items():
        if type_value in dna:
            guilty_party_attributes[attribute_name] = type_name
            break

# find the specs
print "\nSo, I actually ran a test on it and here are the results:"
print "\n\nOur suspect has the following specs: "
print guilty_party_attributes

for (suspect_name, suspect_attributes) in suspects.items():
    if suspect_attributes == guilty_party_attributes:
        print "\n" + suspect_name + " did it!"
        is_suspect_found = True

if not is_suspect_found:
    print("\n\nGuilty party got away with the crime. No DNA in the database!")