n = int(input("请输入一个数字："))
def gongshi(n):
    for i in range(2 , n):
        print(f"{i}")
if n >= 0:
    gongshi(n)
else:
    print("请输入正整数")