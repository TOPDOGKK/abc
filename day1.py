list1=[9,8,7,6,5,4,3,2,1]
duibicishu=0
jiaohuancishu=0

i=0 #交换了多少轮
while i<len(list1)-1 :
    c=0 #一轮交换多少次
    while c <len(list1)-1-c:
    duibicishu+=1
        if list1[i]>list1[i+1]:
            jiaohuancishu+=1
            list1[i],list1[i+1]=list1[i+1],list1[i]
        i+1
    print("最后列表为{}".format(list1))
    c+=1

print("对比了{}".format(duibicishu))
print("交换了{}".fromat(jiaohuancishu))

