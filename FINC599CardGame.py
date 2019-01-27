BREAKING DOWN PROBLEMS & THOUGHT PROCESS

Consider a modified version of the card game “War”. In this version, there are two players who are dealt 10 cards each, numbered 1 through 10.

"OK. I need to make a game with two players with 10 cards each
from 1 through 10. how do I write this?"

When i was writing this initially I did it with the manual list, [1,2,3,4....], then figured i could use list(range(1,11)) - 11 cos it will only run until 10 as per python rules. but then i figured what if we want to dictate the number of cards at the start of the game? Thus.. coming up with:

	player_1 = list(range(1,(number_of_cards+1)))
	player_2 = list(range(1,(number_of_cards+1)))

I wrote this down as it is without placing it in a function or whatever.
just do it line per line and then piece them together like a puzzle after.

----------------------

In each round of the game, player A and player B play a random card from their deck.

"OK I need to extract a random number from a list. how do i do that?"

Found out about the random module online and decided to import that and put it at the top of my code.

	import random

now i need to name these new variables that i plan to randomly pick
out from the list.

	pick_p1=random.choice(player_1)
	pick_p2=random.choice(player_2)

----------------------
The player who plays the higher card takes back their own
card, as well as the card of their opponent.

"OK I need to compare the 2 picks with if,then statements."

		if pick_p1>pick_p2:

		elif pick_p1<pick_p2:

		elif pick_p1==pick_p2:

"OK I need to figure out what I should make this fucking program do
given those statements"

I need to (1)Remove pick from losing player and (2)append the pick into the winning players deck.

		if pick_p1>pick_p2:
			player_1.append(pick_p2)
			player_2.remove(pick_p2)
		elif pick_p1<pick_p2:
			player_1.remove(pick_p1)
			player_2.append(pick_p1)
		elif pick_p1==pick_p2:

-------------------

In the event of a tie, each player gets their card back...

"OK I need to do this coin flip thing for a tie (based on prof's email)"

For this coin flip, i can probably use a list [1,2]...

		coin_flip = [1,2]

Have the program choose from the list randomly:

		result = random.choice(coin_flip)

and make an if,then statement for the results of winner(same rules as above):

			if result==1:
				player_1.append(pick_p1)
				player_2.remove(pick_p1)
			elif result==2:
				player_1.remove(pick_p1)
				player_2.append(pick_p1)

code now turns into this:
		pick_p1=random.choice(player_1)
		pick_p2=random.choice(player_2)

		if pick_p1>pick_p2:
			player_1.append(pick_p2)
			player_2.remove(pick_p2)
		elif pick_p1<pick_p2:
			player_1.remove(pick_p1)
			player_2.append(pick_p1)
		elif pick_p1==pick_p2:
			coin_flip = [1,2]
			result = random.choice(coin_flip)
			if result==1:
				player_1.append(pick_p1)
				player_2.remove(pick_p1)
			elif result==2:
				player_1.remove(pick_p1)
				player_2.append(pick_p1)

------------------
...and it goes back into their pile randomly

"OK I need to randomize the cards"

I tried to put the pick in randomly but i figured this would be easier.
I stumbled upon the randomize code while looking this up.

		random.shuffle(player_1)
		random.shuffle(player_2)

insert that after all if statements and the code looks like this:

		pick_p1=random.choice(player_1)
		pick_p2=random.choice(player_2)

		if pick_p1>pick_p2:
			player_1.append(pick_p2)
			player_2.remove(pick_p2)
			random.shuffle(player_1)
			random.shuffle(player_2)
		elif pick_p1<pick_p2:
			player_1.remove(pick_p1)
			player_2.append(pick_p1)
			random.shuffle(player_1)
			random.shuffle(player_2)
		elif pick_p1==pick_p2:
			coin_flip = [1,2]
			result = random.choice(coin_flip)
			if result==1:
				player_1.append(pick_p1)
				player_2.remove(pick_p1)
				random.shuffle(player_1)
				random.shuffle(player_2)
			elif result==2:
				player_1.remove(pick_p1)
				player_2.append(pick_p1)
				random.shuffle(player_1)
				random.shuffle(player_2)

I could have probably ended here but i was curious as to who wins so
I put this code in:

	if len(player_1)==0:
		player_2_wins.append(1)
		#print('PLAYER 2 WINS!')
	else:
		player_1_wins.append(1)
		#print('PLAYER 1 WINS!')

and put a list at the very top to consolidate:

	player_1_wins = list()
	player_2_wins = list()

Its just to calculate whos list is empty and that's the loser.
Append (1) into the list and then i added all 1s in list after to see
total wins of player.

	print('player 1 wins',' ', sum(player_1_wins),' ', 'times')
	print('player 2 wins',' ', sum(player_2_wins),' ', 'times')

---------------
A.
Write a series of functions that simulates the game

"AHM OK so this needs to be in a function"

I initially put this all in a while loop but now it says function,
I put the while loop in the function. this is where the puzzle thing comes in.

code is now:

import random

simulations = int(input("Welcome to WAR! How many times do you want to run the simulation?:"))
number_of_cards = int(input("How many cards per player?:"))
player_1_wins = list()
player_2_wins = list()

def war_game():
	player_1 = list(range(1,(number_of_cards+1)))
	player_2 = list(range(1,(number_of_cards+1)))
	rounds = 0

	while player_1 and player_2:
		pick_p1=random.choice(player_1)
		pick_p2=random.choice(player_2)

		if pick_p1>pick_p2:
			player_1.append(pick_p2)
			player_2.remove(pick_p2)
			random.shuffle(player_1)
			random.shuffle(player_2)
		elif pick_p1<pick_p2:
			player_1.remove(pick_p1)
			player_2.append(pick_p1)
			random.shuffle(player_1)
			random.shuffle(player_2)
		elif pick_p1==pick_p2:

			coin_flip = [1,2]
			result = random.choice(coin_flip)
			if result==1:
				player_1.append(pick_p1)
				player_2.remove(pick_p1)
				random.shuffle(player_1)
				random.shuffle(player_2)
			elif result==2:
				player_1.remove(pick_p1)
				player_2.append(pick_p1)
				random.shuffle(player_1)
				random.shuffle(player_2)


	if len(player_1)==0:
		player_2_wins.append(1)
	else:
		player_1_wins.append(1)

for i in range(simulations):
	war_game()


Added the (for i) statement to run the function. and added
variable (simulations) up top to dictate how many times i want to run it.

the input function is used when you want the user to input
a value and used that.

--------------

calculate the number of rounds each game takes.

"OK I need to make a counter for every loop the function makes"

added this at the top of the function:

	rounds = 0

added this at the end of the funtion:

	rounds+=1

I will also need to consolidate the number of rounds per simulation in
a list
-------------
Run your program 10,000 times and record each result.

this is where the input code comes in handy.
I already put this code in so it should be ok

put this at the very top of the code cos i want it outside of the
def function:

	total_rounds = list()

and this one at the bottom:

	total_rounds.append(rounds)
-------------
Time how long the simulation takes.

"OK I need to time it"

found the code of time. put this at the start to record time it starts:
	t0 = time.time()

put this at the very end to record time code hits this line:
	t1 = time.time()

subtract!
	total_time= t1-t0

-------------
Plot a histogram of the distribution of the number of rounds played. Make sure there is a title, legend, and labeled axes.

plt.hist(total_rounds, bins=20)
plt.title('WAR Histogram of Rounds')
plt.xlabel('Number of Rounds')
plt.ylabel('Frequency')
plt.show()


------------
C.
Re-run the program for a game with 25 distinct cards. How long did this simulation take?
Does it vary linearly with respect to the 10 card
game?

just changed the input numbers so i dont have to write code again w 25 cards.


------------

After that it's a matter of debugging and maybe fixing indents and stuff.
Notice that my code has a lot of print statements i have disabled.

This helped a lot when i was starting out the code and it made me see
what was pick 1 and pick 2 and if it compared correctly.
and if number of rounds was working good.
