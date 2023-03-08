n = int(input())

sum = 0

for i in range(100):
    sum+=i
    if sum >= n:
        print(i)
        break
