txt = "Hello, welcome to my world."
pos = []
c = 0
for i in txt:
    c = c + 1
    if txt.find("e",c) != -1 and txt.find("e",c) not in pos:
        pos.append(txt.find("e",c))
print(pos)