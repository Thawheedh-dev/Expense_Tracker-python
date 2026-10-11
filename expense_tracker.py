types=['Education','groceries','Snacks','miscellaneous']
education=[]
groceries=[]
snacks=[]
miscell=[]
print("")
while True:
    type=input('''Info: Select the type of expense, Enter the amount OR to see total of each enter 5,
     to see total overall enter 6
    1.Education
    2.Groceries
    3.Snacks
    4.miscellaneous

Enter type: ''')
    
    
    if type=='1':
       amount=input("in Rs.")
       education.append(int(amount))
       print(education)
    elif type=='2':
        amount=input("in Rs.")
        groceries.append(int(amount))
        print(groceries)
    elif type=='3':
        amount=input("in Rs.")
        snacks.append(int(amount))
        print(snacks)
    elif type =='4':
      amount=input("in Rs.")
      miscell.append(int(amount))
      print(miscell)
    elif type=='5':
        type_amount=input('''
                1.Education
                2.Groceries
                3.Snacks
                4.miscellaneous
            Enter type to get total amount: ''')
        if type_amount=='1':
            print('The total in education is Rs.',sum(education))
        elif type_amount=='2':
            print('The total in groceries is Rs.',sum(groceries))
        elif type_amount=='3':
            print('The total in snacks is Rs.',sum(snacks))
        elif type_amount =='4':
            print('The total in Miscellaneous is Rs.',sum(miscell))
    elif type=='6':
        print("The total is Rs.",sum(education)+sum(groceries)+sum(snacks)+sum(miscell))