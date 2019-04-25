"""LOGIC:
1. Id all numbers that 
i. cannot be divided by either 6, 9 or 20
ii. cannot be broken down into numbers that divide by the above

1. Loop through 1-n
2. If number divides by 6, 9 or 20 then not a MN number
3. Else if number > than any of above then can it be broken down 
   into numbers that do divide by above
"""

def nugget():
    nn_list = []
    #Loop through numbers in range
    for i in range(1,50):
        #If num divides exactly by above 3 then NN
        if i % 6 == 0 or i % 9 == 0 or i % 20 == 0:
            nn_list.append(i)
        #Else if num divide by 9, and the remainder divide by 6 then NN
        #PROBLEM = Need to loop through however many times it divides by 9 then attempt to divide remainder
        elif (i // 9 >0) and ((i % 9) % 6 == 0) :       
            nn_list.append(i)
        #Else if num divide by 20, and the remainder divide by 6 or 9 then NN
        elif (i // 20 >0) and (((i % 20) % 9 == 0) or ((i % 20) % 6 == 0)):    
            nn_list.append(i)
            
    print(nn_list)

        
nugget()

