# Create a function called win_percentage() that takes
# two parameters named wins and losses.
# This function should return out the total percentage
# of games won by a team based on these two numbers.


def win_percentage(wins, losses):
    total_percent_of_wins = wins / (wins + losses) * 100
    return total_percent_of_wins


print(win_percentage(5, 5))

print(win_percentage(10, 0))

