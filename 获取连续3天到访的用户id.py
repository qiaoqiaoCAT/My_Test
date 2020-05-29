def test():
    #从文件中读取数据，存存放在列表中
    with open('./customer','r') as f:
        data=f.readlines()
        data=[x.strip() for x in data if x.strip()!='']
    #将每个人的日期放在一个listz中，构成key:value结构
    dictx={}
    for x in data:
        if x[0] in dictx.keys():  #
            dictx[x[0]].append(x[2])
        else:
            dictx[x[0]]=[x[2]]
    #对dictx中的value进行去重复以及排序
    ret_set=[list(set(x)) for x in dictx.values()]
    index=0
    for key in dictx:
        dictx[key]=ret_set[index]
        index+=1
    [x.sort() for x in dictx.values()]

    #遍历每一个key的value，如果其value有连续3天的就append
    ret=[]
    for key in dictx:
        listx=dictx[key]
        tmp=[listx[0]]
        index=0
        for i in range(1,len(listx)):
            if len(tmp)>=3:
                break
            if int(listx[i])==int(tmp[index])+1:
                tmp.append(listx[i])
                index+=1
            else:
                tmp=[listx[i]]
                index=0
        if len(tmp)>=3:
            ret.append(key)
    return  ret
if __name__=='__main__':
    a=test()
    print(a)