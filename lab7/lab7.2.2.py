commentators = {}
while True:
    line = input()
    if not line:
        break
    name, comment = line.split(": ")
    commentators[name] = None

print(len(commentators))
