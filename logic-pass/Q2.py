def prime_num(n1,n2):
    n=n1
    prime=[]
    while(n<=n2  ) :

        count = 0
        for i in range(2,n2):
            if(n%i==0):
                count=count+1
        if(count==1) :
            prime.append(n)
        n=n+1
    return prime


print(prime_num(7,20))
