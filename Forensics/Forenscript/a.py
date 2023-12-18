content = open('a.bin', 'rb').read()
output = open('b.png', 'wb')
result = []

for i in range(0, len(content), 4):
    for j in range(4):
        result.append(content[i + (3 - j)])

output.write(bytes(result))