def list_append(list_a,list_b,flag="2d"):
    '''
    将一个二维数组b追加到另一一个二维数组a
    flag:  1d为2d 为二维列表叠加
    eg:  append( [[1,2,3],[4,5,6]] , ["abc",66]) [[1,2,3,"abc"],[4,5,6,66]]
    '''
    if list_b:
        if flag=="2d":
            if len(list_b)!=0:
                if isinstance(list_b[0],int) or isinstance(list_b[0],str) :
                    for i in range(len(list_a)):
                        list_a[i].append(list_b[i])
                else:
                    for i in range(len(list_a)):
                        for j in range(len(list_b[0])):
                            list_a[i].append(list_b[i][j])      
        if flag=="1d":
            if isinstance(list_b,list):
                for i in list_b:
                    list_a.append(i)
            else:
                list_a.append(list_b)
    return list_a