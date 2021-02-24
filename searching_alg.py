import time
letter_list = list("abcdefghijklmnopqrstuvwxyz")

def condense_list(l:list):
    my_dict = {}
    for i in letter_list:
        my_dict[i] = l.count(i)

    return my_dict

def order(w1, w2):
    w1l = list(w1)

    total = 0

    for i in range(2):
        try:
            if w1[i]==w2[i]:
                total+=i**3
        except IndexError:
            pass


    words = []
    for i in range(len(w1l)):
        words.append(w1l[:i])
        words.append(w1l[i:])

    words = [i for i in words if len(i)>=1]

    for i in words:
        if "".join(i) in w2:
            total+=len(i)**2

    return total


def compare_dict(d1:dict, d2:dict):
    total = 0
    lengthd1 = 0
    lengthd2 = 0
    for i in letter_list:
        diff = abs(d1[i]-d2[i])
        lengthd1+=d1[i]
        lengthd2+=d2[i]

        # if d2[i] ==0 or d1[i]==0:
        #     # total-=5
        #     continue

        if diff==0:
            total+=10

        elif diff==1:
            total+=5
        # else:
        #     total-=5

    if abs(lengthd2-lengthd1)>3:
        return 0

    return total/max(abs(lengthd2-lengthd1),1)



def search(word:str):
    with open('final_dict.txt', 'r') as f:
        word_list = f.readlines()
        word_list = [word.rstrip('\n') for word in word_list]
        word_list = [i.split() for i in word_list]
        points = [float(i[0]) for i in word_list]
        word_list = [i[1] for i in word_list]

    w = word.lower()
    word = list(word)
    word = condense_list(word)

    if w in word_list:
        return w

    word_list_list = [list(i) for i in word_list]
    word_list_dict = [condense_list(i) for i in word_list_list]

    close = []
    best = 0
    for i in range(len(word_list)):


        diff = abs(len(word_list[i])-len(w))

        if diff>3:
            continue

        d= compare_dict(word, word_list_dict[i])
        # d=0
        q=order(w, word_list[i])

        d += q
        d += points[i] * 50

        if (d>best) and not (abs(best-d)<10):
            close = []
            close.append(word_list[i])
            best = d

        if (abs(best-d)<10):
            close.append(word_list[i])

    return close


