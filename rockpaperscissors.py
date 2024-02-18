import random

player_wins = 0
pc_wins = 0
rounds = {}
round = 1

def win_check(player_wins, pc_wins):
    if player_wins > pc_wins:
        print("Player wins the game!")
    else:
        print("Computer wins the game!")

def round_check(player_choice, pc_choice, player_wins, pc_wins):
    if player_choice == "a":   #1st scenario rock
        if pc_choice == "a":
            print("Player Rock vs Pc Rock")
            print("Its a draw!")
        elif pc_choice == "b":
            print("Player Rock vs Pc Paper")
            print("Paper wraps rock...Pc wins!")
            pc_wins += 1
        else:
            print("Player Rock vs Pc Scissors")
            print("Rock breaks Scissors... Player wins!")
            player_wins += 1
    elif player_choice == "b":   #2nd scenario paper
        if pc_choice == "a":
            print("Player Paper vs Pc Rock")
            print("Paper wraps rock...Player wins!")
            player_wins += 1
        elif pc_choice == "b":
            print(f"Player Paper vs Pc Paper")
            print("Its a draw!")
        else:
            print("Player Paper vs Pc Scissors")
            print("Scissors cuts paper... Pc wins!")
            pc_wins += 1
    else:                              #3rd scenario scissors
        if pc_choice == "a":
            print("Player Scissors vs Pc Rock")
            print("Rock breaks Scissors... Pc wins!")
            pc_wins += 1
        elif pc_choice == "b":
            print("Player Scissors vs Pc Paper")
            print("Scissors cuts paper... Player wins!")
            player_wins += 1
        else:
            print("Its a draw!")

    return player_wins, pc_wins

# game start
while player_wins < 3 and pc_wins < 3:
    try:
        if round == 1:
            print("First round")
        else:
            print("Round " + str(round))
        print(" ")
        player = input("Choose your weapon:\na for rock\nb for paper\nc for scissors\n")
        if player not in ["a","b","c"]:
            raise ValueError
        pc = random.choice(["a", "b", "c"])
        player_wins, pc_wins = round_check(player, pc, player_wins, pc_wins)
        rounds["Round " + str(round)] = "Player " + str(player_wins) + " - " + str(pc_wins) + " Computer"
        print(f"Score: Player {player_wins} - {pc_wins} Pc")
        print("End of round " + str(round) + " \n" + " ")
        print(" ")
        round += 1
    except:
        print("Invalid choice, Please try again\n")

win_check(player_wins,pc_wins)

print(f"Total rounds: {round-1}")
print("The score history is:")
for round_info in rounds:
    print(round_info, rounds[round_info])

