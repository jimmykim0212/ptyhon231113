# DeomoListTuple.py

strA = "python is very powerful"
print(strA[0])
print(strA[1])
print(strA[0:6])
print(strA[:6])

colors = ['red','blue','green']
print(len(colors))
print(type(colors))
colors.append("white")
colors.insert(1,"pink")
print(colors)
colors += 'red'
print(colors)
print(colors.pop())
print(colors.pop())
print(colors)
colors.remove("red")
print(colors)
colors.extend(['black','yellow','green'])
print(colors)
colors.sort()
print(colors)
colors.reverse()
print(colors)

#디버깅할 때 중단 점(Break Point)
for item in colors:
    print(item)

t=(1,2,3)
type(t)
device=("아이폰",'아이패드','노트북')

def calc(a,b):
    return a+b,a*b
result = calc(5,6)
result

print('----set 형식----')
a={1,2,3,3,}
b={3,4,4,5}
print(a)
print(type(b))
print(a.union(b))
print(a.intersection(b))
print(a.difference(b))


print('----tuple 형식----')
tp = (10,20,30)
print(len(tp))
print(type(tp))

#함수 정의
def = calc(a,b) :
    return a+b,a*b

result=calc(3,4)
print(result)
print(result[0])
print(result[1])

print('id:%s, name:%s' % ('kim','김유신'))
args = (5,6)
print(calc(*args))
print(calc(5,6))


#선택한 블럭을 주석처리  ctrl + /
print('---형식변환---')
a = set((1,2,3))
print(a)
b = list(a)
print(b)
b.append(4)
print(b)

d = dict(a=1,b=2,c=3)
d

color =


