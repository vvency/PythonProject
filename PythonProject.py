
# -*- coding: utf-8 -*-
print("I'm ok")
print("I\'m \"ok\"")# \はエスケープ文字　\nは改行　\tはtab
print("Pythonを\n勉強してる")
print(3>2)
print(5>2 and 3>7)
print(5>2 or 3>7)
print(not 1>2)
print(10//3)#取整
print(10%3)#取余

A = ord('A')#获取字符的整数表示
B = ord('了')
C = chr(25991)#把编码转换为对应的字符
D = len("ひらて")#计算str包含多少个字符
print(A)
print(B)
print(C)
print(D)

#格式化字符串
#在字符串内部，%s表示用字符串替换，%d表示用整数替换，%f表示用浮点数替换，%s会把任何数据类型转换为字符串，%%表示一个%（转义）
print('これは%s,%sで作った'%('ジャム','リンゴ'))

s1 = 72
s2 = 85
r = (s2 - s1)/s1*100
print('%.1f%%'%r)# %.xf可以指定保留x位小数


#条件语句
age = 20
if age >= 6:
	print('青年')
elif age >= 18:
	print('成年')
else:
	print('子ども')

s = input('birth:')#input返回类型为str
birth = int(s)
if birth < 2000:
	print('00前')
else:
	print('00后')

height = 1.75
weight = 80.5
bmi = weight/(height*height)
if bmi <= 18.5:
	print('过轻')
elif 18.5 < bmi <= 25:
	print('正常')
elif 25 < bmi <= 28:
	print('过重')
elif 28 < bmi <= 32:
	print('肥胖')
else:
	print('严重肥胖')

#循环语句
names = ['松本','佐藤','平手']
for name in names:
	print(name)

sum = 0
for x in range(101):#range(x)生成从0开始小于x的整数
	sum = sum + x
print(sum)

sum = 0
n = 99
while n > 0:
	sum = sum + n
	n = n - 1
print(sum)

L = ['Bart', 'Lisa', 'Adam']
for name in L:
	print('Hello,',name,'!')

n = 1
while n <= 100:
    if n > 10: # 当n = 11时，条件满足，执行break语句
        break # break语句会结束当前循环
    print(n)
    n = n + 1
print('END')

n = 0
while n < 10:
    n = n + 1
    if n % 2 == 0: # 如果n是偶数，执行continue语句
        continue # continue语句会直接继续下一轮循环，后续的print()语句不会执行
    print(n)


d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
print(d['Michael'])


def my_abs(x):
	if not isinstance(x,(int,float)): #参数类型检查
		raise TypeError('違う')
	if x >= 0:
		return x
	else:
		return -x
print(my_abs(-1))


import math
def quadratic(a,b,c):
	delta = pow(b,2) - 4 * a * c
	if a != 0 and delta >= 0:
		r1 = (-b + math.sqrt(delta)) / (2 * a)
		r2 = (-b - math.sqrt(delta)) / (2 * a)
		return r1,r2
	else:
		print('无实数根')

print(quadratic(1,2,1))


def calc(*numbers):#使用*定义可变参数
	sum = 0
	for n in numbers:
		sum = sum + n * n
	return sum

print(calc(1,2,3),calc(1,2,3,6,9))


def product(*numbers):
	sum = 1
	if len(numbers) >= 1:
		for n in numbers:
			sum = sum * n
		return sum
	else:
		raise TypeError('違う')

print('product(5) =', product(5))
print('product(5, 6) =', product(5, 6))
print('product(5, 6, 7) =', product(5, 6, 7))
print('product(5, 6, 7, 9) =', product(5, 6, 7, 9))



def fact(n): #递归函数
    if n==1:
        return 1
    return n * fact(n - 1)

print(fact(5))



def move(n,a,b,c):          #递归函数-汉诺塔
	if n == 1:               
		print(a,'>',c)
	elif n > 1:
		move(n-1,a,c,b)
		move(1,a,b,c)
		move(n-1,b,a,c)
	else:
		print('None')

print(move(6,'a','b','c'))
		

def trim(s):
	s = s[1:-1]
	return s

print(trim(' dfafa '))


def findMinandMax(L):
	if len(L) == 0:
		return(None,None)
	else:
		min = L[0]
		max = L[0]
		for n in L: #迭代
			if n < min:
				min = n
			if n > max:
				max = n
		return(min,max)

print(findMinandMax((8,3,6,9,30)))

L1 = ['Hello', 'World', 18, 'Apple', None]
L2 = [s.lower() for s in L1 if isinstance(s,str)]
L3 = [s.lower() if isinstance(s,str) else s for s in L1]
print(L2)
print(L3)


def triangles():
	row = [1]
	while True:
		yield row   #生成器函数
		row = [1]+[row[k]+row[k+1]for k in range(len(row)-1)]+[1]
o = triangles()
print(next(o))
print(next(o))
print(next(o))
print(next(o))
print(next(o))