def primer(m,n):
    for num in range(m,n+1):
        if num>1:
            for i in range(2,num):
                if(num%i)==0:
                    break
                else:
                    print(num)
                    break
print('enter the range of numbers to find prime numbers')
m=int(input())
n=int(input())
if m>0 and n>0 and m<n:
    prime(m,n)
else:
    print('enter the correct value')