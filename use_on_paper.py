from searching_alg import search
from rich.progress import track

read_file = input("What file do you want to check?: ")
write_file = input("What file do you want to write to?: ")

with open(read_file,'r') as f:
    words = f.read()
    f.close()

whitelist = set('abcdefghijklmnopqrstuvwxyz ABCDEFGHIJKLMNOPQRSTUVWXYZ')
answer = ''.join(filter(whitelist.__contains__, words))
answer = answer.split()

newpara = []

for step in track(range(len(answer))):
    newpara.append(search(answer[step]))

with open(write_file,'w') as f:
    f.write(" ".join(newpara))
    f.close()
