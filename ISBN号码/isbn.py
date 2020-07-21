input_file=open("isbn.in",mode="r").read().split("-")
isbn=""
isbn_w=""
for i in input_file:
    isbn_w+=i
    if i != input_file[-1]:
        isbn+=i
isbn_n=[]
for i in range(len(isbn)):
    isbn_n.append(isbn[i])
isbn=0
for i in range(len(isbn_n)):
    isbn+=int(isbn_n[i])*(i+1)
if isbn%11==int(isbn_w[-1]):
    print("Right")
else:
    print(isbn_w[0]+"-"+isbn_w[1:4]+"-"+isbn_w[4:9]+"-"+str(isbn%11))