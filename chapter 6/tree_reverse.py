def tree_reverse(list1):
    list2=list1[::-1]
    list3=[]
    for element in list2:
       if type(element)==list:
            list3.append(tree_reverse(element))
       else:
           list3.append(element)
    return list3