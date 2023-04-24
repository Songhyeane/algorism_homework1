from typing import List

array = [7,9,4,8,6,3]

def heap_sort(a):

    for i in range(1,len(a)):
        c = i
        while c!= 0 :
            r = (c-1) //2
            if a[r] < a[c]:
                a[r],a[c] = a[c],a[r]

            c = r

    for j in range(len(a)-1,-1,-1):
        a[0],a[j] = a[j],a[0]
        r = 0
        c = 1

        while c <j :
            c=2*r+1
            if c<j-1 and a[c] < a[c+1]:
                c+=1
            if c< j and a[r] < a[c]:
                a[r],a[c] = a[c],a[r]

            r = c

b = [7,9,4,8,6,3]
heap_sort(b)
print(b)










