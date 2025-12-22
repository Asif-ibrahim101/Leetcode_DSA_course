from collections import defaultdict

def find_players_with_0_or_1_loss(matches):
    #we create a map to store te players that lost
    losses = defaultdict(int)

    for winner, loser in matches:
        losses[loser] += 1 #increamentig the loss count

        losses[winner] += 0 #ensuring the winner is in the list

    
    #creating two arrays for winner and lower
    zero_loss = []
    one_loss = []

    for player, count in losses.items():
        if count == 0:
            zero_loss.append(player)
        elif count == 1:
            one_loss.append(player)
    
    return [sorted(zero_loss), sorted(one_loss)]