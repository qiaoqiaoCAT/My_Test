def combine_list(list1,list2):
    index1=index2=0
    ret_list=[]
    while True:
        if index1>=len(list1):
            ret_list.extend(list2[index2])
            return ret_list
        elif index2>=len(list2):
            ret_list.extend(list1[index1])
            return ret_list
        elif list1[index1]<list2[index2]:
            ret_list.append(list1[index1])
            index1+=1
        else:
            ret_list.append(list2[index2])
            index2+=1

if __name__=='__main__':
    list1=[1,3,4,7]
    list2=[0,2,3,9]
    a=combine_list(list1,list2)
    print(a)
