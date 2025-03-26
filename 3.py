n = float(input("请输入一个数："))
def gongshi(n):
    if n == 0:
        return 1
    else:
        return n * gongshi(n - 1)
print(gongshi(n))