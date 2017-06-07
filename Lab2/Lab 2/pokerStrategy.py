__author__ = 'yuafan'

#hand
ahand = {'HighCard':1,'OnePair':2,'TwoPairs':3,'3ofakind':4,'straight':5,'flush':6,'fullhouse':7,
       '4ofakind':8,'straightflush':9}
#Hand rank
ahandrank = {'2':1,'3':2,'4':3,'5':4,'6':5,'7':6,'8':7,'9':8,'T':9,'J':10,'Q':11,'K':12,'A':13}


def pokerStrategyExample(playerAction, playerActionValue,playerStack, agentHand,agentHandRank,agentStack):
    if ahand[agentHand] == 1 and ahandrank[agentHandRank] < ahandrank['Q'] \
        and ahandrank[agentHandRank] >= ahandrank['Q']:  #Hand rank is Queen or higher
        if playerActionValue < 0.02*playerStack:
            if agentStack < playerActionValue:
                agentAction = 'AllIn'
                agentValue = agentStack
            else:
                agentAction = 'Call'
                agentValue = playerActionValue
        else:
            if playerActionValue < 0.05*agentStack:
                if agentStack > playerStack:
                    if agentStack < playerActionValue:
                        agentAction = 'AllIn'
                        agentValue = agentStack
                    else:
                        agentAction = 'Call'
                        agentValue = playerActionValue
                else:
                    agentAction = 'Fold'
                    agentValue = 0

    if (ahand[agentHand] == 1 and ahandrank[agentHandRank] >= ahandrank['Q']) \
        or (ahand[agentHand] == 2 and ahandrank[agentHandRank] <= ahandrank['T']):
        if playerActionValue < 0.02*agentStack:
            if agentStack < playerActionValue:
                agentAction = 'AllIn'
                agentValue = agentStack
            else:
                agentAction = 'Call'
                agentValue = playerActionValue
        else:
            if playerActionValue < 0.05*agentStack:
                if agentStack < 2*playerActionValue:
                        agentAction = 'AllIn'
                        agentValue = agentStack
                else:
                    agentAction = 'Raise'
                    agentValue = playerActionValue*2
            else:
                agentAction = 'Fold'
                agentValue = 0

    if ahand[agentHand] == 2 and ahandrank[agentHandRank]> ahandrank['T'] and ahandrank[agentHandRank] > ahandrank['A']:
        if playerActionValue < 0.04*playerStack:
            if agentStack < playerStack:
                if playerActionValue < 0.06*agentStack:
                    if agentStack < 2*playerActionValue:
                        agentAction = 'AllIn'
                        agentValue = agentStack
                    else:
                        agentAction = 'Raise'
                        agentValue = playerActionValue*2
                else:
                    if agentStack < playerActionValue:
                        agentAction = 'AllIn'
                        agentValue = agentStack
                    else:
                        agentAction = 'Call'
                        agentValue = playerActionValue
            else:
                if agentStack < playerActionValue:
                    agentAction = 'AllIn'
                    agentValue = agentStack
                else:
                    agentAction = 'Call'
                    agentValue = playerActionValue
        if ahandrank[agentHandRank] == ahandrank['A']:
            if agentStack < 2*playerActionValue:
                agentAction = 'AllIn'
                agentValue = agentStack
            else:
                agentAction = 'Raise'
                agentValue = playerActionValue*2
        else:
            if agentStack < playerActionValue:
                agentAction = 'AllIn'
                agentValue = agentStack
            else:
                agentAction = 'Call'
                agentValue = playerActionValue

    if ahand[agentHand] == ahand['TwoPairs']:
        if playerActionValue < 0.05*playerStack:
            if ahandrank[agentHandRank] > ahandrank['9']:
                if agentStack < 2*playerActionValue:
                    agentAction = 'AllIn'
                    agentValue = agentStack
                else:
                    agentAction = 'Raise'
                    agentValue = playerActionValue*2
            else:
                if agentStack < playerActionValue:
                    agentAction = 'AllIn'
                    agentValue = agentStack
                else:
                    agentAction = 'Call'
                    agentValue = playerActionValue
        else:
            if playerActionValue < 0.1*agentStack:
                if ahandrank[agentHandRank] > ahandrank['9'] and agentStack > playerStack:
                    if agentStack < 2*playerActionValue:
                        agentAction = 'AllIn'
                        agentValue = agentStack
                    else:
                        agentAction = 'Raise'
                        agentValue = playerActionValue*2
                else:
                    if agentStack < playerActionValue:
                        agentAction = 'AllIn'
                        agentValue = agentStack
                    else:
                        agentAction = 'Call'
                        agentValue = playerActionValue
                if ahandrank[agentHandRank] > ahandrank['J']:
                    if agentStack < playerActionValue:
                        agentAction = 'AllIn'
                        agentValue = agentStack
                    else:
                        agentAction = 'Call'
                        agentValue = playerActionValue
                else:
                    agentAction = 'Fold'
                    agentValue = 0

    if ahand[agentHand] == ahand['3ofakind']:
        if agentStack > 1.5*playerStack:
            if playerActionValue < 0.05*agentStack:
                if playerActionValue > 0:
                    if agentStack < 2*playerActionValue:
                        agentAction = 'AllIn'
                        agentValue = agentStack
                    else:
                        agentAction = 'Raise'
                        agentValue = playerActionValue*2
                else:
                    if agentStack < 10:
                        agentAction = 'AllIn'
                        agentValue = agentStack
                    else:
                        agentAction = 'Bet'
                        agentValue = 10
            else:
                if agentStack < playerActionValue:
                    agentAction = 'AllIn'
                    agentValue = agentStack
                else:
                    agentAction = 'Call'
                    agentValue = playerActionValue
        else:
            if agentStack < playerActionValue:
                agentAction = 'AllIn'
                agentValue = agentStack
            else:
                agentAction = 'Call'
                agentValue = playerActionValue

# You can extend this strategy as much as you want as long as you keep it fully deterministic (no random)

    return agentAction, agentValue


#def agentStrategyPostDiscard
# implement your own post discard strategy. Otherwise you can use the given strategy
