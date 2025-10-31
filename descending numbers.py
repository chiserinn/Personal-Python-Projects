def descending_order(num):
    no = num
    num_list = []
    j=0
    

    while no > 0:
        num_list.append(no % 10)
        no//=10
        
        
    sorted_num = sorted(num_list, reverse = True)
    #calc_num = [int(j) for j in sorted_num]
    calc_num = sorted_num[0]

    for j in sorted_num:
        calc_num += sorted_num[j]
        j+=1

    print(calc_num)
    
    
descending_order(12445)
            