a=0
n=int(open("common.in","r").read())
for i in range(1,n+1):
    a+=n//i #约数数量=n//1+n//2+n//3+.....
output_f=open("common.out","w").write(str(a))
