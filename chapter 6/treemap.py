i=-1
c=[]
list3=[]
def treemap(lambdaa,lists):
    list2=lists[:]
    treemap1=(lambdaa,lists)
    fun=treemap1[0]
    for element in lists:
        if type(element)==list:
            print element
            global i
            i+=1
            c.append([])
            c[i].append(treemap(lambdaa,element))
            list2.remove(element)
            list2.append(c[i])
            c[i]=list2
        else:
            list2.remove(element)
            list2.append(fun(element))
    return list2