"""
    @ Baek 9935, 문자열 폭발
    @ Prob. https://www.acmicpc.net/problem/9935
      Ref. 
      Ref Prob.
    @ Algo: 
    @ Start day: 22. 12. 09
    @ End day: 22. 12. 09
"""



#input = sys.stdin.readline
string = input()
del_string = input()

last = del_string[-1]
crr = []
length = len(del_string)
for i in string:
  crr.append(i)
  if i == last and "".join(crr[-length:]) == del_string:
    del crr[-length:]
  
if len(crr) == 0:
  print("FRULA")
else:
  print(''.join(crr))
   

'''
def main():
 
  string = input()    # 전체 문자열
  bomb = input()      # 폭발 문자열

  lastChar = bomb[-1] # 폭발 문자열의 마지막 글자
  stack = []
  length = len(bomb)  # 폭발 문자열의 길이

  for char in string:
    stack.append(char)
    if char == lastChar and ''.join(stack[-length:]) == bomb:
      del stack[-length:]

  answer = ''.join(stack)

  if answer == '':
    print("FRULA")
  else:
    print(answer)
        
if __name__ == '__main__':
    main()
'''