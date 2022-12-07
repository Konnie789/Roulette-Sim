import random 

print("hello fuckers!", '\n')

#setup of the roulette (American)
roulette_wheel = [
    [0,"green"], [37, "green"],
    [1,"red"], [2,"black"],
    [3,"red"], [4,"black"],
    [5,"red"], [6,"black"],
    [7,"red"], [8,"black"],
    [9,"red"], [10,"black"],
    [11,"black"], [12,"red"],
    [13,"black"], [14,"red"],
    [15,"black"], [16,"red"],
    [17,"black"], [18,"red"],
    [19,"black"], [20,"red"],
    [21,"black"], [22,"red"],
    [23,"black"], [24,"red"],
    [25,"black"], [26,"red"],
    [27,"black"], [28,"red"],
    [29,"black"], [30,"red"],
    [31,"black"], [32,"red"],
    [33,"black"], [34,"red"],
    [35,"black"], [36,"red"],
]

#Starting pot of the simulation
bank = 5000
#counter for how many days has passed.
days_count = 1

#user input loop variable 
i = 0

while i != 1:
    run_time = input("For how many days would you like to run this simulation?\n")
    #user specifies for how long the sim will last in days.
    if run_time.isdigit():

        while days_count < (int(run_time) + 1):

            #Track what the sim has at the start of the betting day
            start_of_day = bank

            
            print("Day ", days_count, " pot of $", start_of_day,".", sep='')
            #check to see if bankrupt
            if start_of_day == 0:
                print("You are out of money!")
                break
            #inital bet is always $500
            bet = 500
            #play until you make $500
            while bank <= start_of_day :
                #track the bets
                print("The current bet is $", bet, ".", sep="")
                #roulette wheel is spun
                roulette_spin = random.choice(roulette_wheel)
                print("The result is ", roulette_spin[0], " ", roulette_spin[1],".", sep="")
                #Successful guess
                if roulette_spin[1] == 'black':
                    print("you win!")
                    #bet is added to your count
                    bank+=bet
                    print("Your new pot is $", bank,".", sep="")
                    if start_of_day < bank:
                        print("You have been successful today!")
                        #progress the day count and start all over
                        days_count += 1
                        print('\n')
                #Unsuccessful guess
                else:
                    print("you lose!")
                    #bet is taken away from the bank 
                    bank-=bet
                    print("Your new pot is $", bank,".", sep="")
                    #bet is then doubled and the roulette wheel is spun again.
                    bet = bet * 2
                    if bet > bank or  bet > 4000:
                        print("You were not successful today.")
                        #progress the day count and start all over
                        days_count += 1
                        print('\n')
                        break

                    print('\n')

        #closes the loop  
        i = 1      
    else: 
        print("error. Please input a number.")

print("At the end of the simulation, the bot has a total pot of $", bank, ".", sep="")
print("The profit made was $", (bank - 5000), sep="")
print('\n')
input("Enter any key to quit.")
