text = "    Python\t   "

words = text.split(" ")
clean = " ".join(words)

text = text.replace("\t", " ")

def clean_line(line):
    line = " ".join(line.split())
    return line

print(clean_line(text))

text = "  A   B  "
print(" ".join(text.split()))

line = "\tPython\t"
print(line.strip())

lines = ["A","A","B"]
unique=[]
for x in lines:
    if x not in unique:
        unique.append(x)
print(unique)
