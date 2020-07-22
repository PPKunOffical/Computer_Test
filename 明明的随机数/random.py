input_f=open("./random.in","r").read()
#分段
i_l=input_f.split("\n")[0]
i_n=input_f.split("\n")[1]
i_n=i_n.split(" ")
for i in range(len(i_n)):
    i_n[i]=int(i_n[i]) #列表值转数字，不然sort()会按照字母顺序排序
i_n=list(set(i_n)) #去掉重复
i_n.sort()
output=str(len(i_n))+"\n" #去重后数量
for i in i_n:
    output+=str(i)+" " #去重排序后
output_f=open("./random.out","w").write(output) #写入"random.out"
