def maximum_power(n):
    res=0
    for i in range(n,0,-1):
        if((i&(i-1))==0):
            res=i
            break
    return res

def maximize(price_count,price,m):

    if sum(price)==price_count and m==0:
        return sum(price)
    else:
        price.sort()
        price.reverse()
        i=0
        while m>0 and i<len(price):
            max_pow_2=maximum_power(price[i])
            price[i]=price[i]//max_pow_2
            m-=max_pow_2
            i+=1
        return sum(price)

price_count=int(input("Enter price count:"))
price=[]
for _ in range(price_count):
    price.append(int(input()))
m=int(input("\nEnter the no. of coupons"))
print(maximize(price_count,price,m))