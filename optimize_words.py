import math

with open("common.txt","r",encoding = 'cp850') as f:
  common = f.readlines()

with open("english3.txt","r",encoding = 'cp850') as f:
  al = f.readlines()

scores = dict()

def inverse_normalize_logistic(xi):
  x = (1-(xi/len(common)))
  log = 1/(1+math.e**(-7*(x-.5)))

  return log

for q in al:
  idx = al.index(q)

  try:
    score = inverse_normalize_logistic(common.index(q))
    scores[q] = score
    if idx % 1000 == 0:
      print(idx, q, score)
  except ValueError:
    scores[q] = -.5

with open("final_dict.txt",'w') as f:
  for i in scores.keys():
    f.write(str(scores[i])+" "+i)

  f.close()
