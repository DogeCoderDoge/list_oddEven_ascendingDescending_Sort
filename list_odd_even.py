n = int(input("how many numbers u want to input? "))

c = 0
list = []
odd = []
even = []
mergedlist = []

while c<n:
    c+=1
    num = int(input("enter number: "))
    list.append(num)

for i in list:
    if i%2==0: even.append(i)
    else: odd.append(i)

def descending(list):
    descending_ = []

    while len(list) > 0:
        g = 0
        for i in list:
            if g < i:
                g = i

        list.pop(list.index(g))         
        #print(g)
        #print(list)
        descending_.append(g)

    #print(list)
    return descending_
    #print(descending_)


def ascending(list):
    ascending_ = []       

    while len(list) > 0:
        g=list[0]
        for i in list:
            if g > i:
                g = i

        #print(g)
        #print(list)
        list.pop(list.index(g))
        ascending_.append(g)

    #print(list)
    return ascending_
    #print(ascending_)

print(list)
#ascending(even)
#descending(odd)
#mergedlist.append(descending(odd))
#mergedlist.append(ascending(even))

for i in descending(odd):
    mergedlist.append(i)

for i in ascending(even):
    mergedlist.append(i)    

print(mergedlist)
