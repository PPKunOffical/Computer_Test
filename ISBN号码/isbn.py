a=open("./isbn.in","r").read()
b=a[:12]
c=0
d=1
for i in b:
    if i!='-':
        e=int(i)
        c=c+e*d
        d+=1
g=c%11
if g==10:
    h='X'
else:
    h=str(g)
if h==a[12]:
    jg="Right"
else:
    b=b+h
    jg=b
output_f=open("./isbn.out","w").write(jg)