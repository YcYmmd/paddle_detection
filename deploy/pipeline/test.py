x = 10  # 这是一个全局变量
y = 3
z = 1
while z > 0:
    x = 20
    y = x - 1  # 这是一个局部变量，只在while循环内有效
    x -= 1  # 这将修改全局变量x
    z-=1

print(x)
print(y)