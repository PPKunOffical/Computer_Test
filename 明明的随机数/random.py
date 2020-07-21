input_file=open("random.in",mode="r")
output_list=list(set(input_file.read().split("\n")[1].split(" ")))
for i in range(len(output_list)):
    output_list[i]=int(output_list[i])
output_list.sort()
output=str(len(output_list))+"\n"
for i in output_list:
    output+=str(i)+" "
print(output)
output_file=open("random.out",mode="w")
output_file.write(output)
