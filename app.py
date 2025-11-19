n=int(input())
left=0
right=100
for i in range(100):
    mid=(left+right)//2
    print(mid)
    if mid==n:
        print(f"最终猜了{i+1}次")
        break
    elif mid>n:
        right=mid
    else:
        left=mid

hajimi=["hello",9.9,9]
#查询
print(hajimi[0])
#修改
hajimi[1]="miao"
print(hajimi)
#添加
hajimi.append("miaomiao")
print(hajimi)
#删除
hajimi.remove("miaomiao")
print(hajimi)
#插入
hajimi.insert(2,"maodie")
print(hajimi)

set1={1,2,3,4,5,6,7,8,9}
set2={5,8,9,0,11,34}
#交集
set3=set1&set2
print(set3)
set4=set1|set2
print(set4)


haokun=('shuijiao',666,6.66,True,[6,6],{'shui':'jiao'})
print(haokun)
element='shuijiao'
if element in haokun:
    index=haokun.index(element)
    print(index)
else:
    print('maodie')
# 统计元素出现次数
count=haokun.count('hello')
print(count)
#不可修改


maodiehaqizhi={
    "kun":{"数分":666,"离散数学":999,"某语言":1111},
    "sleep":{"数分":6,"离散数学":9,"某语言":1}
}
print(maodiehaqizhi)
#添加
maodiehaqizhi["maio9"]={"数分":6666,"离散数学":9999,"某语言":11111}
print(f"miao9就是最big的：{maodiehaqizhi}")
#修改
maodiehaqizhi["kun"]={"数分":0,"离散数学":0,"某语言":0}
print(maodiehaqizhi)
#删除
maodiehaqizhi.pop("kun")
print(maodiehaqizhi)
#遍历
for student in maodiehaqizhi:
    print(student)
