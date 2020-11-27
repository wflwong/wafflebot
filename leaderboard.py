# League Scrim AH/CHU

# # Need a database of all scrim players of Discord user => W/L
# # Need this database to be continually updating into a .txt file
# # Need the code to parse through this .txt file during scrim

# # !scramble ==> makes two teams
# # need !scramble to make the teams AND record who's on what team in temporary .txt
# # !win ==> winning team members on temp .txt get +1 W (contrary to +1 L for other team)

# # # # # # # # # # # # # # # # # # # # # # # # #

import json

# Saves current scrim matchup into .txt

def convertListStr(input_str, separator):
        final = separator.join(input_str)
        return final
    
def saveTeams(team1, team2, file):
    scrim = {}
    scrim['T1'] = team1
    scrim['T2'] = team2
    
    with open(file, 'w+') as fp:
        json.dump(scrim, fp)

def openBoards(file):
    json_file = open(file)
    json_str = json_file.read()
    boards = json.loads(json_str)
    json_file.close
    
    return boards

# Retrieve winning team members from local JSON
""" team parameter => 'T1' or 'T2' """

winners = []
losers = []

def retrieve(winner, loser, file):
     json_file = open(file)
     json_str = json_file.read()
     scrim = json.loads(json_str)
     
     for team in scrim:
         i = 0
         if team == winner:
             while i < len(scrim[winner]):
                 winners.append(scrim[winner][i])
                 i += 1
                 
     for team in scrim:
        i = 0
        if team == loser:
            while i < len(scrim[loser]):
                losers.append(scrim[loser][i])
                i += 1


# Creates database of leaderboards for all users
    
    #   dict = {
    #           discord_user: ['W', 'L']
    #                    }


# Add Discord user into leaderboard with 0W - 0L    
def createUser(user, leaderboard):
    leaderboard[user] = [0, 0]
    
def createNewUser(user, leaderboard):
    i = 0
    for key in leaderboard:
        if user == key:
            i = 1
            
    if i == 0:
        createUser(user, leaderboard)


def removeUser(user, leaderboard):
    leaderboard.pop(user)

def updateBoard(leaderboard):
    with open(leaderboard, "w+") as fp:
        json.dump(leaderboard, fp)
        

# Update player's score records in leaderboards from recent scrim
def adjustWin(user, leaderboard):
    leaderboard[user][0] += 1

def adjustLoss(user, leaderboard):
    leaderboard[user][1] += 1

def scrimAdjust(winners, losers, leaderboard):
    for player in winners:
        adjustWin(player, leaderboard)
    
    for player in losers:
        adjustLoss(player, leaderboard)
    
    with open("leaderboard.json", "w") as fp:
        json.dump(leaderboard, fp)
    
    winners = []
    losers = []


# # #
def test(leaderboard):
    for player in leaderboard:
        leaderboard[player] = "{}-{}".format(leaderboard[player][0], leaderboard[player][1])
    
    return leaderboard
    
    
