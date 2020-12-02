with open('input.txt', 'r') as f:
  lines = f.readlines()
f.close()

lines = [l.replace("\n", "") for l in lines]

def isValid(password, letter, firstPosition, secondPosition):
  firstIndex = firstPosition - 1
  secondIndex = secondPosition - 1
  occurrences = 0

  if password[firstIndex] == letter:
    occurrences = occurrences + 1

  if password[secondIndex] == letter:
    occurrences = occurrences + 1

  return occurrences == 1

validPasswords = 0

for line in lines:
  lineParts = line.split()
  firstPositionStr = lineParts[0].split("-")[0]
  firstPosition = int(firstPositionStr)

  secondPositionStr = lineParts[0].split("-")[1]
  secondPosition = int(secondPositionStr)

  requiredLetter = lineParts[1].split(":")[0]
  password = lineParts[2]

  if isValid(password, requiredLetter, firstPosition, secondPosition):
    validPasswords = validPasswords + 1

print(validPasswords)
