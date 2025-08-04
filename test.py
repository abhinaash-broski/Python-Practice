n= int(input("enter the number of series: "))
sum=0
for i in range (1, n+1): 
    sum_i=0
    for j in range (1,i+1): 
        sum_i=sum_i+j 
        
    sum=sum+sum_i
print("Sum of the sums is: ",sum)