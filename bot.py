import discord
import random
import json
from leaderboard import *
from discord.ext import commands

intents = discord.Intents.default()
intents.members = True
client = commands.Bot(command_prefix=".", intents=intents)
dash = '-' * 40

def openJSON(file):
    json_file = open(file)
    json_str = json_file.read()
    leaderboard = json.loads(json_str)
    json_file.close()

leaderboards = openBoards('E:\Desktop\Waffledong\leaderboard.json')

@client.event
async def on_ready():
    bot_channel = client.get_channel(781144966705053698)    
    await bot_channel.send("`Waffledong is ready to rumble`")


@client.command()
async def waffle(ctx):
    await ctx.send('wong')

# Inhouses
team1 = []
team2 = []

@client.command()
async def scramble(ctx):
    channel = client.get_channel(649033428393787423)                    
    members = channel.members                                           #getting a list of all members in channel

    # Randomizes the list of members in channel
    random.shuffle(members)

    for member in members[:len(members)//2]:
        team1.append(member.name)
    
    for member in members[len(members)//2:]:
        team2.append(member.name)

    # Creates a Team 1 and Team 2 list of members' names (T1 consisting of first half of random list; T2 second half)
    t1 = "".join([":blue_circle: " + "\t" + member.name + '\n' for member in members[:len(members)//2]])
    t2 = "".join([":red_circle: " + "\t" + member.name + '\n' for member in members[len(members)//2:]])

    # Creates final string where the BOT will send all teams in one Discord message
    final_str = '{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}'.format(dash, "**TEAM 1** (Left Side)", dash, t1, dash, "**TEAM 2** (Right Side)", dash, t2)
    
    # Save the teams into local JSON file
    scrim = openJSON('E:\Desktop\Waffledong\scrim.json')
    if scrim != None:
        scrim.truncate(0)
    saveTeams(team1, team2, 'E:\Desktop\Waffledong\scrim.json')

    # Add players not currently on the leaderboards
    currentBoards = openBoards('E:\Desktop\Waffledong\leaderboard.json')
    for player in team1:
        createNewUser(player, currentBoards)
    
    for player in team2:
        createNewUser(player, currentBoards)
    
    with open('E:\Desktop\Waffledong\leaderboard.json', "w") as fp:
        json.dump(currentBoards, fp)
        fp.close()

    await ctx.channel.send(final_str)


# Displays leaderboards in Printable form


def displayBoards(file):
    json_file = open(file)
    json_str = json_file.read()
    leaderboard = json.loads(json_str)
    json_file.close()
    
    for player in leaderboard:
        leaderboard[player] = "{} - {}".format(leaderboard[player][0], leaderboard[player][1])
    final = "\n".join("**{}**\t{}".format(v, k) for k, v in leaderboard.items())
    return final


@client.command()
async def leaderboard(ctx):
    displayBoard = displayBoards('E:\Desktop\Waffledong\leaderboard.json')
    final_str = '{}\n{}\n{}\n{}'.format(dash, "**AhChu** \t LoL Leaderboards", dash, displayBoard)
    await ctx.send(final_str)


# Make changes to leaderboards AFTER A SCRIM

winners = []
losers = []

def adjustBoards(winner, loser):
    retrieve(winner, loser, 'E:\Desktop\Waffledong\scrim.json')
    scrimAdjust(winner, loser, 'E:\Desktop\Waffledong\leaderboard.json')

    f = open('E:\Desktop\Waffledong\scrim.json', 'r+')
    f.truncate(0)

@client.command()
async def t1win(ctx):
    # adjustBoards(winners, losers)
    displayBoard = openJSON('E:\Desktop\Waffledong\leaderboard.json')
    retrieve("T1", "T2", 'E:\Desktop\Waffledong\scrim.json')

    print(winners)
    print(losers)

    scrimAdjust(winners, losers, displayBoard)

    await ctx.send("`Leaderboards updated. Type .leaderboard to see current rankings.`")

@client.command()
async def t2win(ctx):
    displayBoard = openJSON('E:\Desktop\Waffledong\leaderboard.json')
    retrieve("T2", "T1", 'E:\Desktop\Waffledong\scrim.json')
    scrimAdjust(winners, losers, displayBoard)

    await ctx.send("`Leaderboards updated. Type .leaderboard to see current rankings.`")

    

client.run('NzgxNjk2NzY4OTk4ODk5NzIz.X8BZ2A.UWMCSJeQEU3qxRjhMpb19ZgpfCI')