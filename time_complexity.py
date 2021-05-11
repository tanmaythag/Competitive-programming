# what is the time complexity


def fun(n):
    for in in range(1,n):      # n times
        j=1
        while j<i*i:           # n*n times  
            j=j+1
            if j%i==0:
                for k in range(0,j): # n*n time 
                    print("tanmay")

# here the time complecity will be in worst case
# n*(n*n)*(n*n)
# O(n^5) 

#----------------------------------------------------------------------------------

#questionn2


def func(n):
    counter=0
    for j in range(n/2,n):     # logn
        while j*n/2<=2:        #n
            k=1
            while k<=n:
                count=count+1
                k=k*2
            j=j+1
            print(count)

# answer is O(nlog(n))