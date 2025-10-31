def divisors(integer):
    divisor_list = []
    n = integer
    x = 2
    


    while (x < n):
        if n % x == 0:
            divisor_list.append(x)
        x = x + 1
    
        
        

    if len(divisor_list) == 0 :
        print ("%d is prime"%x)
        
    print(divisor_list)

"""

    if n > 1:
        #PRIMES DONE
        for i in range(len(prime_number_list)):
            if n == prime_number_list[i]:
                print (n, "is prime")
            elif multiples_two == 0:
                for j in range(n):
                    if x < n:
                        if multiples_two == 0:
                            divisor_list.append(x)
                        elif x == n:
                            divisor_list.append(x)
                        else:
                            divisor_list.append(x)

                        x = x * 2  
                        j + 1
            elif multiples_two == 1:
                for j in range(n):
                    if x < n:
                        if multiples_two == 0:
                            divisor_list.append(x)
                        elif x == n:
                            divisor_list.append(x)
                        else:
                            divisor_list.append(x)

                        x = x * 2  
                        j + 1
            else:
                for k in range(n):
                    if y < n:
                        if multiples_five == 0:
                            divisor_list.append(y)
                        elif y == n:
                            divisor_list.append(y)
                        y = y * 5  
                        k + 1
                    else:
                        break
                
        print (divisor_list)
    else: 
        print("n = 1. No available divisions")
    pass     

                
               
n == prime_number_list[i]:               
     
            
    
    # if x is divisable by 2, add 2 to list
    # if x is % 2 = 0, see if x is > multiples of 2 list all under the value that x is -> will take long
    # if x % 2 = 1, x is not divisable by 2 
    
    

   for i in range(len(prime_number_list)):
        
        x = n % prime_number_list[i]
        if (x == 0):
            divisor_list.append(prime_number_list[i])
        x+=1
            break
        i + 1



      for i in range(len(prime_number_list)):
        
            y = n % prime_number_list[i]
            if (y == 0):
                return ("%d is prime"%(prime_number_list[i]))
            i+=1
    else:
        return(divisor_list)

"""