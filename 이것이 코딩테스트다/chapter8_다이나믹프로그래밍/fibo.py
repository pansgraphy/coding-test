def fibo(x):
    if x == 1 or x == 2:
        return 1
    return fibo(x - 1) + fibo(x - 2)

print(fibo(4))

# 문제점 : n이 커지면 수행 시간이 기하급수적으로 상승함..!

