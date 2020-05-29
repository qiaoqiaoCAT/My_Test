#冒泡排序
def bubble_sort(listx):
    for i in range(len(listx)-1):
        for j in range(len(listx)-1-i):
            if listx[j]>listx[j+1]:
                temp=listx[j]
                listx[j]=listx[j+1]
                listx[j+1]=temp
    return listx

