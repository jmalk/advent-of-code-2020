with open('input.txt', 'r') as f:
    lines = f.readlines()
f.close()

lines = [l.replace("\n", "") for l in lines]

lines = [int(line) for line in lines]

for i in range(0, len(lines)):
    for j in range(i + 1, len(lines)):
        if lines[i] + lines[j] == 2020:
            print(lines[i] * lines[j])
