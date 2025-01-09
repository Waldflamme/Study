dic = {0:'1',1:[],2:'0',3:'4',4:[]}
dic1 = {}
for key in dic:
    if len(dic[key])>=1:
        dic1[key]=dic[key]
print(dic1)