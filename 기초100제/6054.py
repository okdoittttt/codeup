a, b = map(int, input().split())

c = bool(int(a))
d = bool(int(b))

print(not c and not d)
print((c and d) or (not c and not d))
print((c and d) or (d and c))
print(bool(int(a)) or bool(int(b)))
print(bool(int(a)) and bool(int(b)))

