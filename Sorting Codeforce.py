t = int(input())

for i in range(t):
  n = int(input())
  arr = sorted(map(int, input().split()))

  flag = True
  for j in range(len(arr)-1):
    if arr[j] - arr[j+1] > 1:
      flag = False
      break

  if flag:
    print("YES")
  else:
    print("NO")
    
  

