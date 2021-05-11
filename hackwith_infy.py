# write a program to determine a number N is equal to the sum of its proper positive divisors(excluding the number itself)
"""
Input format
> first line:T(number of test cases)
  for each test case 
> first line: N

Output format
> print YES , if N is equal to the sum of its proper positive divisors else Print NO

constraints
1<= T <=100
1<= N <=10power9

Sample Input
3(test case)
6
5
28

output
YES
NO
YES
"""
T = int(input())
for _ in range(T):
    N = int(input())

    if(N==1):
        print("NO")
        continue
    
    #find all divisors

    divisors = set([1])

    i = 2
    while(i*i<=N):
        if(N%i == 0):
            divisors.add(i)
            divisors.add(N//i)

    # add up them
    divisor_sum = sum(divisors)

    #check the sum with N
    if(divisor_sum == N):
        print("YES")
    else:
        print("NO")