list=[]
k= int(input())
for i in range(0,k):
    str=input("")
    str1=str.split()
    if str1[0]=="insert":
        list.insert(int(str1[1]),int(str1[2]))
    elif str1[0]=="print":
        print(list)
    elif str1[0]=="remove":
        list.remove(int(str1[1]))
    elif str1[0]=="append":
        list.append(int(str1[1]))
    elif str1[0]=="sort":
        list.sort()
    elif str1[0]=="pop":
        list.pop()
    elif str1[0]=="reverse":
        list.reverse()
