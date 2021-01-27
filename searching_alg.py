
letter_list = list("abcdefghijklmnopqrstuvwxyz")

def condense_list(l:list):
    my_dict = {}
    for i in letter_list:
        my_dict[i] = l.count(i)

    return my_dict

def order(w1, w2):
    w1l = list(w1)

    total = 0

    words = []
    for i in range(len(w1l)):
        words.append(w1l[:i])
        words.append(w1l[i:])

    words = [i for i in words if len(i)>=1]

    for i in words:
        if "".join(i) in w2:
            total+=len(i)

    return total


def compare_dict(d1:dict, d2:dict):
    total = 0
    lengthd1 = 0
    lengthd2 = 0
    for i in letter_list:
        diff = abs(d1[i]-d2[i])
        lengthd1+=d1[i]
        lengthd2+=d2[i]

        if d2[i] ==0 or d1[i]==0:
            # total-=5
            continue
        if diff==0:
            total+=5
        if diff<=2:
            total+=3

    if abs(lengthd2-lengthd1)>3:
        return 0

    return total/max(abs(lengthd2-lengthd1),2)

with open('english3.txt', 'r') as f:
    word_list = f.readlines()
    word_list = [word.rstrip('\n') for word in word_list]

def search_with(word:str):
    w = word.lower()
    word = list(word)
    word = condense_list(word)

    if w in word_list:
        return w

    word_list_list = [list(i) for i in word_list]
    word_list_dict = [condense_list(i) for i in word_list_list]

    close = ''
    best = 0
    for i in range(len(word_list)):

        d= compare_dict(word, word_list_dict[i])
        q=order(w, word_list[i])
        d+=q

        if d>best:
            close = word_list[i]
            best = d

        # if d==best:
        #     close+=", "+word_list[i]
        #     print(close, d,q)

    return close


print(search_with(input("Enter a word: ")))
