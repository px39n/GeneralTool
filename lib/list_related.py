#删除a.remove("abc") del a[1]
'''排序
a = [[1,2],[3,5],[1,0],[4,7],[5,7]]
a.sort(key=lambda x : x[1]+x[0])
print(a)
'''
'''去重
 tag_name=list(set(tag_list[0]))
 '''

 #打散    split()----"|".join(row[1]) 


def list_append(list_a,list_b,flag="2d"):
    '''
    将一个二维数组b追加到另一一个二维数组a
    flag:  1d为2d 为二维列表叠加
    eg:  append( [[1,2,3],[4,5,6]] , ["abc",66]) [[1,2,3,"abc"],[4,5,6,66]]
    '''
    if list_b:
        if flag=="2d":
            if len(list_b)!=0:
                list_a[0]=list_a[0]+list_b[0]
                list_a[0]=list_a[0]+list_b[0] 
        if flag=="1d":
            if list_a:
                list_a=list_a+list_b if isinstance(list_b,list) else list_a+[list_b]         
    return list_a


def join(origin_list,join_list,field):
    new=[]
    for item in origin_list:
        temp=item
        if join_list.get(item[1]) and join_list.get(item[1])[0]:
            temp[2]=join_list.get(item[1])[0]
            i=i+1
        new.append(temp)
    return new