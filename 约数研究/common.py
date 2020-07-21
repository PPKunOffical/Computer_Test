a=0
n=int(open("common.in","r").read())
for i in range(1,n+1):
    a+=n//i
output_f=open("common.out","w").write(str(a))