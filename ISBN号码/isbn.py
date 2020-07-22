a=open("./isbn.in","r").read()
b=a[:12] #获取识别号之前的数字
c=0
d=1
for i in b:
    if i!='-': #略过”-“号
        e=int(i)
        c=c+e*d
        d+=1
g=c%11 #计算识别号
if g==10: #如果是十那么就是"X"
    h='X'
else:
    h=str(g)
if h==a[12]:
    jg="Right"
else:
    b=b+h
    jg=b
output_f=open("./isbn.out","w").write(jg) #写入"isbn.out"
