from typing import List

def quick_sort(a:List,start,end):
    if start >= end or end == -1 :
        print('*')
        return 0
    q=partiton(a,start,end)

    quick_sort(a,start,q-1)
    quick_sort(a,q+1,end)

    print(0)
    return a

def partiton(a:List,start,end):
    print(f'a:{a} start:{start} end:{end}')

    i =start-1
    j = start
    criteria = a[end]

    while j != end:
        if a[j] <= criteria:
            i +=1
            a[i] ,a[j] =a[j] ,a[i]
        j +=1
        print(f'i:{i} j:{j} a:{a}')

    a.insert(i+1,criteria)
    del a[end+1]
    return i+1

a = [8,8,3,10,9,1,6]
print(quick_sort(a,0,len(a)-1))





