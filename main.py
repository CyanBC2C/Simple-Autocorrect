from searching_alg import search

def remove_duplicates(l):
  final = []

  for i in l:
    if i not in final:
      final.append(i)

  return final

def main():
  word = input("Input a word: ")
  s =search(word)
  print("Recommended: ")
  print(remove_duplicates(s))

if __name__=='__main__':
  main()