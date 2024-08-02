h, m = input().split()

h = int(h)
m = int(m)

if h != 0 and m < 45:
    print(h-1, m+15)
elif h == 0 and m < 45:
    print(23, m+15)
else:
    print(h, m-45)