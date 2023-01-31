# Operator NOT
# Ask a parent if he/she can attend one of his/her child's games.
# You have the following cases:
# If you have a vacation, or it is a day off, then yes you can attend the son's game.
# Otherwise, he cannot attend, as he would be busy.

vacation = True
dayOff = False

if not(vacation or dayOff):
    print('Cannot attend the game')
else:
    print('You can attend the game')