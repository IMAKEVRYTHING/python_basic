# 조합 in DFS

def DFS(L, s) :
  global cnt
  if L == m :
    for j in range(L) :
      print(res[j], end = ' ')
    cnt += 1
    print()
  else :
    for i in range(s, n+1) :
      res[L] = i
      DFS(L+1, i+1)

  if __name__ == "__main__" :
    n, m = 4, 2
    res = [0] * (n+1)
    cnt = 0
    DFS(0, 1)
    print(cnt)

# 순열 in DFS
    
def DFS(L) :
  global cnt
  if L == m :
    for j in range(L) :
      print(res[j], end = ' ')
    cnt += 1
    print()
  else :
    for i in range(1, n+1) :
      if ch[i] == 0 :
        ch[i] = 1
        res[L] = i
        DFS(L+1)
        ch[i] = 0

if __name__ == "__main__" :
  n, m = 3, 2
  res = [0] * n
  ch = [0] * (n+1)
  cnt = 0
  DFS(0)
  print(cnt)
  
# 중복순열 in DFS

def DFS(L) :
  global cnt
  if L == m :
    for j in range(L) :
      print(res[j], end = ' ')
    cnt += 1
    print()
  else :
    for i in range(1, n+1) :
      res[L] = i
      DFS(L+1)

if __name__ == "__main__" :
  n, m = 3, 2
  res = [0] * (n+1)
  cnt = 0
  DFS(0)
  print(cnt)
