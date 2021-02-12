with open("common.txt","r") as f:
  common = f.readlines()

with open("english3.txt","r") as f:
  al = f.readlines()

scores = dict()

def inverse_normalize(xi):
  return 1-(xi/len(common))

for q in al:
  idx = al.index(q)
  if idx%1000==0:
    print(idx, q)
  try:
    score = inverse_normalize(common.index(q))
    scores[q] = score
  except ValueError:
    scores[q] = 0

with open("final_dict.txt") as f:
  for i in scores.keys():
    f.write(str(scores[i])+" "+i)

  f.close()
