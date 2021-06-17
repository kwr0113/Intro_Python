
e2f = {
    'dog': 'chien',
    'cat': 'chat',
    'walrus': 'morse'
}

f2e = {}

for k, v in e2f.items():
    f2e.update({v: k})

print(e2f)
print(f2e)
