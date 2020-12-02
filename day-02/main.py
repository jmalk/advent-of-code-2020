with open('input.txt', 'r') as f:
  lines = f.readlines()
f.close()

lines = [l.replace("\n", "") for l in lines]

def isValid(password, letter, min, max):
  occurrences = password.count(letter)
  return occurrences >= min and occurrences <= max

validPasswords = 0

for line in lines:
  lineParts = line.split()
  minStr = lineParts[0].split("-")[0]
  min = int(minStr)

  maxStr = lineParts[0].split("-")[1]
  max = int(maxStr)

  requiredLetter = lineParts[1].split(":")[0]
  password = lineParts[2]

  if isValid(password, requiredLetter, min, max):
    validPasswords = validPasswords + 1

print(validPasswords)
