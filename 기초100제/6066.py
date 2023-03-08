a, b, c = map(int, input().split())

list = [a, b, c]

for i in range(len(list)):
    if list[i]%2 == 0:
        print("even")
    else:
        print("odd")