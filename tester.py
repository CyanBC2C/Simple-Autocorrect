from searching_alg import search

points = 0

with open('aspell.txt','r') as f:
    l = f.readlines()
    f.close()

for i in l:
    correct, incorrect = i.lower().rstrip("\n").split()
    answers = search(incorrect)
    if correct in answers:
        points+=100-(len(answers)*5)
        print('Correct: '+str(points), incorrect, correct, answers)
    else:
        points-=100
        print('Incorrect: '+str(points), incorrect, correct, answers)