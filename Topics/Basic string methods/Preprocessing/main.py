text = input()
g = [x.lower() for x in text if x not in ",.!?"]
print(''.join(g))

