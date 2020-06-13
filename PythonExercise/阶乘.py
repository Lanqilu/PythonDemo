# 求阶乘
a = 1
x = 1
sum = 1
n = int(input("请输入非负整数n="))
while n < 0:
    n = int(input("请输入非负整数n="))
for i in range(1, n + 1):
    a *= i
print("for循环n!=", a)
while x <= n:
    sum *= x
    x += 1
print('while循环n!=', sum)
