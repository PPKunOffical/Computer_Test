input_f=open("game.in","r").read()
r_n=input_f.split("\n")[0]
s_n=input_f.split("\n")[1].split(" ")
all_n=[]
sx_n=[]
c_n=len(s_n)
x_n=0
#第一次for循环把所有数字加起来
for i in s_n:
    for x in s_n:
        if x_n<c_n:
            all_n.append(str(int(i)+int(x))+" "+str(i)+" "+str(x))
        x_n+=1
#第二次for循环去除不在列表里的数字
for i in all_n:
    s=i.split(" ")[0]
    for x in s_n:
        if s == x:
            sx_n.append(i)
#第三次for循环比较大小
for i in sx_n:
    n=int(i.split(" ")[0])
    n_o=int(i.split(" ")[1])
    n_t=int(i.split(" ")[2])
    if n_o>n_t:
        jg=n_o
    else:
        jg=n_t
output_f=open("./game.out","w").write(str(jg))
