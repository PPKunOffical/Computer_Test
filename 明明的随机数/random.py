input_file=open("random.in","r")
output_list=list(set(input_file.read().split("\n")[1].split(" ")))
def bubbleSort(arr):
    n = len(arr)
    for i in range(n-1):
        for x in range(n-1-i):
            if arr[x] > arr[x + 1]:
                arr[x], arr[x + 1] = arr[x + 1], arr[x]
    return arr
output_list=bubbleSort(output_list)
output=str(len(output_list))+"\n"
for i in output_list:
    output+=i+" "
print(output)
output_file=open("random.out","w")
output_file.write(str(output))
