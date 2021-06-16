
start1 = ['fee', 'fie', 'foe']
rhymes = [
    ('flop', 'get a mop'),
    ('fope', 'turn the rope'),
    ('fa', 'get your ma'),
    ('fudge', 'call the judge'),
    ('fat', 'pet the cat'),
    ('fog', 'walk the dog'),
    ('fun', "say we're done")
]
start2 = "Someone better"

for i, j in rhymes:
    for k in start1:
        print(k.capitalize() + "! ", end="")
    print(i.capitalize() + "!\n" + start2 + " " + j + ".")
