#1. 打印出 1--100 一百个数

'''
i = 1
while i <= 100:
    print(i)
    i += 1
'''

#2. 打印出 1--100 能被3整除的数

'''
i = 1
while i <= 100:
    if i % 3 == 0:
        print(i)
        
    i += 1
'''

#3. 打印出 1--100 的偶数

'''
i = 1
while i <= 100:
    if i % 2 == 0:
        print(i)
        
    i += 1
'''

#4. 打印出 1--100 所有数的和


'''
he = 0
num = 1

while num <= 100:
    he += num
    num += 1

print(he)
'''

#  1 2 3 4 5 6 7 8 
#0 1 3 6 

#5. 输入一个数 判断这个数是不是质数

#质数是指在大于1的自然数中，除了1和它本身以外不再有其他因数的自然数。
# 质数是 只能被 1 和它本身整除的数

#2 -- 16 


num = input("请输入一个自然数：")

num = int(num)

if num == 1:
    print("不是质数")
if num == 2:
    print("是质数")
    
chushu = 2
while chushu <= num - 1:
    if num % chushu == 0:
        print("不是质数")
        break
    
    if chushu == num - 1:
        print("是质数")
        break
        
    chushu += 1


#找出 1--100 内 的所有质数

'''
num = 0
while num < 100:
    num += 1
    
    if num == 1:
        continue
    if num == 2:
        print(num)
        continue
    
    chushu = 2
    while chushu <= num - 1:
        if num % chushu == 0:
            break
        
        if chushu == num - 1:
            print(num)
            break
            
        chushu += 1
'''
        
#6. 输入用户名密码 如果错了3次 就退出程序



jihui = 3
print("你一共有 %d 次机会" % jihui)
while 1==1:
    
    yonghuming = input("请输入用户名：")
    mima = input("请输入密码：")

    if yonghuming == "admin"  and mima == "123456":
        print("登录成功")
        break
    else:
        jihui -= 1
        
        
        if jihui == 0:
            print("这不是你的账号！！ 没机会了")
            break
        
        print("登录失败 你还有 %d 次机会" % jihui)


# 有一对兔子 第3个月起每个月都生一对兔子，
# 小兔子长到第三个月后每个月又生一对兔子，假如兔子都不死，问第12个月的兔子总数为多少？















