Lista1=["almaszár","kerékgyártó","Flóra-pihenő","Malomvölgy","Misina","Égervölgyi tó","Tenkes","Zsolnay-kút"]

n=0
while n < len(Lista1):
    print(Lista1[n],len(Lista1[n]))
    n+=1

for i in range(len(Lista1)):
    if len(Lista1[i]) > 10:
        print(Lista1[i],"hosszabb 10 karakternél.")
