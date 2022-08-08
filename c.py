
profits = [-2 , 1 , 3 , 4 , -5 , 4 , 2 , -1 , -6]


for i in range(0 , len(profits)):

    max_profit = 0

    for j in range(i , len(profits)):

        max_profit += profits[j]

        print(f'{i} - {j} = {max_profit}')
        print()
       




