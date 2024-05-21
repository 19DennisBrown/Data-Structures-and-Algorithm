
def search(goals, hattrick):
  for i in range(len(goals)):
    if goals[i] == hattrick:
      return i
  return -1

goals = [2,30,4]
hattrick = 3

result = search(goals, hattrick)

if result != -1:
  print("Spotted")
else:
  print("Not spotted")