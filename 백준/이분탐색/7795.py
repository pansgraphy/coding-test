import sys
input = sys.stdin.readline

# def binary_search(check, array, start, end):
#     global cnt
#     mid = (start + end) // 2
#     if start > end:
#         return 
#     if array[mid] == check:
#         return cnt
#     elif array[mid] < check:
#         return binary_search(check, array, mid+1, end)
#     elif array[mid] > check:
#         return binary_search(check, array, start, mid-1)


# for tc in range(int(input())):
#     n, m = map(int, input().split())
#     a = b = []
#     a.append(list(map(int, input().split())))
#     b.append(list(map(int, input().split())))


#     cnt = 0
#     for i in a:
#         binary_search(i, b, 0, len(b))


for tc in range(int(input())):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    a.sort()
    b.sort()

    cnt = 0
    for i in range(len(a)):
        for j in range(len(b)):
            if int(b[j]) < int(a[i]):
                cnt += 1
            else:
                break
    print(cnt)
