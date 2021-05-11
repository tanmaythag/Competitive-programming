# given an array of n elements and a number m we need to find all distinct pairs 
#  existing in the array whose pair sum is divisible by the given number m.
# print the total number of such pairs. Distinct pairs means(1,2) and (2,1) are the same i.e, 
# ordering of the pairs doesn't matter
 """
 example input
 10 9 4 5 7 2 8 20 21

 15

 output
 4

 Explantion 
 The following pairs give as sum divisible by 15: 
 10,5
 10,20
 9,21
 7,8

 Input format

 The first line of input contains T , the number of test cases.
 In the next 2*T lines:
 > the first contains n followed by n elements of the array
 > the next line contains m 

 Output Format
 print T lines for all the required outputs
 """
# take input
T = int(input())
for _ in range(T):
    arr = list(map(int, input().split()))
    arr = arr[1:]
    m = int(input())
    # create a dictionary for the frequencies of remainders

    remainders = {}
    for num in arr:
        curr_rem = num%m
        if curr_rem in remainders:
            remainders[curr_rem]+=1
        else:
            remainders[curr_rem]=1
    
    # multiply the frequencies with complements frequencies or do nC2
        num_pairs = 0
        for rem in remainders:
            complement = m - rem
            pairs = 0
            if complement ==m or (2*complement == m):
                pairs = (remainders[rem]*(remainders[rem]-1))//2
            if complement in remainders:
                pairs = remainders[rem]*remainders[complement]
                remainders[rem] = 0
            
            num_pairs = pairs + num_pairs

        # finall print the sum
        print(num_pairs)


 
