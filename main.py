b = input("Enter your name: ").upper().replace(" ", "")
g = input("Enter your partner name: ").upper().replace(" ", "")

el1 = list(b)
el2 = list(g)

# Remove common letters
for ch in el1[:]:
    if ch in el2:
        el1.remove(ch)
        el2.remove(ch)

count = len(el1) + len(el2)

l = ['F', 'L', 'A', 'M', 'E', 'S']
index = 0

while len(l) > 1:
    index = (index + count - 1) % len(l)
    l.pop(index)

result = {
    'F': 'Friends',
    'L': 'Love',
    'A': 'Affection',
    'M': 'Marriage',
    'E': 'Enemy',
    'S': 'Siblings'
}

print("Relationship:", result[l[0]])
