input_f=open("./random.in","r").read()
i_l=input_f.split("\n")[0]
i_n=input_f.split("\n")[1]
i_n=i_n.split(" ")
for i in range(len(i_n)):
    i_n[i]=int(i_n[i])
i_n=list(set(i_n))
i_n.sort()
output=str(len(i_n))+"\n"
for i in i_n:
    output+=str(i)+" "
output_f=open("./random.out","w").write(output)