str1=''
str2='hiiert'
x=min(len(str1),len(str2))
str3=''
for i in range(x):
    str4=str1[i]+str2[i]
    str3=str3+str4
if len(str1)==len(str2):
    print str3
    
elif len(str1)>len(str2):
    print str3+str1[x:]
    
else:
    print str3+str2[x:]