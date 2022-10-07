


print('Welocme to sandader , just for a test. PIN: 1234')
restart=('Y')
chances = 3
count = 3 
balance = 67.4
pinn = 1234



new_pin = pinn


try:
    while chances >= 0:
        pin = int(input('Please Enter Your 4 digit pin: '))
        if pin == pinn:
            print('you entered your pin correctly\n')
            while restart not in ('n', 'NO', 'no', 'N'):
                print('Please press 1 for balance\n')
                print('Please press 2 to make w withdraw\n')
                print('Please press 3 to Pay in \n')
                print('Please press 4 to return card \n')
                print('Please press 5 change password\n')
                option = int(input('what would you liek to choose?'))
                if option == 1:
                    print('you balance is $' ,balance, )
                    restart = input('would you like to go back to menu?')
                    if restart in ('n', 'NO', 'no', 'N'):
                        print('thank you')
                        break
                elif option == 2:
                    option2 = ('Y')
                    withdrawl = float(input('how much would you like to withdraw \n10/20/30/40/50/60/70   '))
                    if withdrawl in [10, 20, 30, 40, 50 ,60 ,70]:
                        balance = balance - withdrawl
                        print('\nYour Balance is now ', balance)
                        restart = input('would you lie to go back menu?')
                        if restart in ('n', 'NO', 'no', 'N'):
                            print("thank you")
                            break
                    elif withdrawl != [10,20,30,40,50,60,70]:
                        print('invalid amount, please retry\n')
                        restart = ('y')
                    elif withdrawl == 1:
                        withdrawl = float(input('please enter desier amount:'))
                elif option == 3:
                    Pay_in = float(input('how much would you like to pay in'))
                    balance = balance + Pay_in
                    print('\nyou balance is now' , balance)
                    restart = input('would you like to go back menu')
                    if restart in ('n', 'NO', 'no', 'N').lower:
                        print('thank you')
                        break
                elif option == 4:
                    print('Please wiat whilst you card returned....\n')
                    print('Thank you for your service')
                    break

                elif option == 5:                 
                        input('Do you want to change pin y/n: ? ')
                        new_password = float(input("what is your new password:  "))
                        repet_password = float(input("repet password:  "))
                        if new_password != repet_password:
                            print("PASSWORD NOT MATCH")
                            
                        elif new_password == repet_password:
                            pinn = pinn - pinn + new_password
                            print("PIN changed")
                            restart = input('would you like to go back menu? y/n')
                            if restart in ('n', 'NO', 'no', 'N'):
                                print('thank you')
                                break


                    
                else:
                    print('Please enter a correct number \n')
                    restart = ('y')


        elif pin != ('1234'):
            count -= 1
            print('incorrect password left try : ' + str(count))
            chances -= 1
            if chances == 0:
                print("\nNo more tries")
                break

except ValueError:
        print('only numbers pin' )
       



    
