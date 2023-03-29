def count_by(x, n):
    _ = []
    for i in range(1,n+1):
        n = x*i
        _.append(n)
    return _
print(count_by(2,5))