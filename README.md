# Roulette-Sim
Could you make money through Roulette? Lets Find Out!

This is a small project with the aim of figuring out if you are able to make a profit playing Roulette at a casino. 
This project was inspired by a recent episode of the podcast "How Did We Get Here?" hosted my Zak Zeeks and Jacob Rabon IV called "The Solemn Solicitation of Ludwig's Crippling Addiction" where the hosts would talk about a strategy to create income through playing Roulette.

The premise of the game is to bet a set amount (in the case of this project, it is $500) and bet consistently on one of the colours, in this case black. If the inital bet is correct, the winner gets $500 and is done playing for the day. If the best is inncorrect, then the player would bet again, this time doubling their bet to $1000. This, if they win, they will make back the $500 lost and the targeted goal of $500 profit. Each time you would lose, the bet will be doubled until there is a win. 

While it assumed that it since a bet on black in roulette is almost a 50/50 chance to win, and the likelyhood of getting 4-5 loses in the row are small, the simulation was not able to successfully make a profit on average. Inside the excel file, you will find 4 different sets of data. A run of 10 10-day intervals where there is no limit to the size of bet the simulation can make (except it cannot bet money it does not have), a run 10 30-day intervals with no betting limit, a run 10 10-day intervals where the maximum amount of money that the simulation can bid is $4000, and a run of 10 simulations 30-day intervals with the same betting limit. Each of these 4 runs, the simulation had lost money in over 50% of the runs, and in the case 30-day intervals, the simulation went completely bankrupt over 50% of the time. 

The reason I believe that this is happening is due to the nature of the game itself. In American Roulette, there are two designated zones that are neither black or red and are labeled green, the 0 and the 00. This is to give the casino a house advantage and prevents the player from having a true 50/50 chance at consistently winning money and creating a profit. 

This test was done from an inital pot of $5000, and further tests will be done with higher pots and higher/lower bets will provide with considerably different results. 

Thank you for the time to look at my little project and if there is any feedback please feel free to message me or leave any comments. 
