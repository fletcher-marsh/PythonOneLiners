def bubble(L):
    swapping = True
    while(swapping):
        swapping = False
        for i in range(len(L)-1):
            if L[i] > L[i+1]:
                L[i], L[i+1] = L[i+1], L[i]
                swapping = True

L = [4, 4, 2, 5]
bubble(L)
print(L)


def select(L):
    small = L[0]
    smallI = 0
    for cS in range(len(L)):
        small = L[cS]
        for i in range(cS, len(L)):
            if L[i] < small:
                small = L[i]
                smallI = i
        L[cS], L[smallI] = L[smallI], L[cS]

L = [2, 4,1,4,6,8,5,4]
select(L)
print(L)


'''Name the worst-case big-oh of the following. Remember that integer inputs 
n have bit length 2**n!'''


def f1(n): 
   k=1
   while (k**2 < n): 
      k += 1 
   return k




def f2(n): 
   k=1
   while (n > 0): 
      (n, k) = (n//4, k+1)
   return k




def f3(n): 
   k=1
   for i in range(n, n**2):
       for j in range(n**3):
           k += 1 
   return k




def f4(n): 
   k=1
   for i in range(n, n**2): 
      k += 1 
   for j in range(n**3): 
      k += 1
   return k


'''
Write the function rowSetMap(a) that takes a non-empty rectangular 2d list a, 
which you may assume contains only integer values, and returns a dictionary 
mapping each value in the 2d list to a set of indexes of the rows in which that 
value occurs in the 2d list. 
'''


def rSM(a):
    d = {}
    for row in range(len(a)):
        for col in range(len(a[0])):
            key = a[row][col]
            if key in d.keys():
                d[key].add(row)
            else:
                d[key] = set([row])
    return d

print(rSM([[1, 2, 3], [2, 3, 4], [5, 6, 7]]))


