import random

def roll():
    min_value = 1
    max_value = 6
    roll = random.randint(min_value, max_value)

    return roll

# value = roll()
# print(value)

while True:
    players = input("Enter the number of players (2-4): ")
    if players.isdigit():
        players = int(players)
        if 2 <= players <= 4:
            break
        else:
            print("It should be between 2 - 4 players")
    else:
        print("Invalid number, please try again")

# print(players)
        
max_score = 50
players_scores = [0 for _ in range(players)]
"""Imagine you have a bunch of players (let's say 3 for now) and you want to keep track of their scores. This line of code is like setting up a scoreboard:

1. **Players:** You have `players`, which is like the number of players in the game (so in this case, 3).
2. **Scoreboard:** You create a list called `players_scores`. This is like the actual scoreboard where you will write down the points.
3. **Empty slots:** But the scoreboard is empty at first, right? So for each player (using `range(players)`), you put a "0" in the corresponding slot on the scoreboard.
4. **Placeholder:** Since you don't need to do anything with the player numbers while putting in the zeros, you use a placeholder `_`. It's like saying "just ignore this part, focus on putting the zeros."

So, in the end, you have a list called `players_scores` with three zeros, one for each player, ready to be updated throughout the game! 

Hope this simplified explanation makes it clearer! 

"""

# print(players_scores)

while max(players_scores) < max_score:

    for player_idx in range(players):
        print("\nPlayer number", player_idx + 1,"turn has just started!")
        print("Your total score is:", players_scores[player_idx] , "\n")
        current_score =  0

        while True:
            should_roll = input("Would you like to roll (y/n)? ")
            if should_roll.lower() != "y":
                break


            value = roll()
            if value == 1:
                print("You rolled a 1! Turn done!")
                current_score = 0
                break
            else:
                current_score += value
                print("you rolled a: ", value)

            print("Your current score is: ", current_score)

        players_scores[player_idx] += current_score
        print("Your total score is: ", players_scores[player_idx])


max_score = max(players_scores)
winning_idx = players_scores.index(max_score)
print("Player number " , winning_idx + 1 , " is the winner with a score of: " , max_score)