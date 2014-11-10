import sys
list3=[]
c=[]
k=0
def permute(list1):
    list2=list1[:]
    while True:
        c.append([])
        global k
        a=list2[1]
        list2[1]=list2[0]
        list2[0]=a
        c[k]=list2[:]
        list3.append(c[k])
        k+=1
        for j in range(len(list1)-1):
            p=list2.pop(0)
            list2.append(p)
            if list2==list1:
                list3.append(list1)
                print list3
                sys.exit()
            else:
                c.append([])
                c[k]=list2[:]
                list3.append(c[k])
                k+=1