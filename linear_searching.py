A = [1 , 3 , 5 , 9 , 5]
n = 4
for i in range(len(A)):
    if A[i] == n:
        flag = 1
        break
    else:
        flag = 0

if flag == 1:
    print(i)
else:
    print("not found")
