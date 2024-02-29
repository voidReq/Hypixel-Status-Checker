import discord
from discord.ext import commands
import requests

TOKEN = ''

intents = discord.Intents.default()
intents.messages = True
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)
#Prefix and intens sent

@bot.event
async def on_ready():
    print("Logged in")


@bot.event
async def on_message(message):
    username = str(message.author).split('#')[0]
    user_message = str(message.content)
    channel = str(message.channel.name)
    print(f'{username}: "{user_message}" | Channel:#{channel}')
    await bot.process_commands(message)
#Logs each message, outputs it

@bot.command()
async def status(ctx, player):
    try:
      response = requests.get( #Requests uuid
          f'https://api.mojang.com/users/profiles/minecraft/{player}').json(
          )
    except Exception as e:
      print("Error occured")
      print(e)
      await ctx.send("Unknown error")
    uuid = response.get("id", None)
    if not uuid:
        await ctx.send(f"Player named {player} doesn't exist")
        return  
    key = ''
    data = requests.get(
        f'https://api.hypixel.net/status?key={key}&uuid={uuid}').json() #Returns status by UUID

    if data['session']['online']: #Checks status
        if data['session']['mode'] == 'LOBBY':
            await ctx.send('Player is in lobby')
        elif data['session']['mode'] == 'BEDWARS_EIGHT_TWO':
            await ctx.send('Player is in doubles, on the map: ' +
                           data['session']['map'])
        elif data['session']['mode'] == 'BEDWARS_EIGHT_ONE':
            await ctx.send('Player is in solos, on the map: ' +
                           data['session']['map'])
        elif data['session']['mode'] == 'BEDWARS_FOUR_THREE':
            await ctx.send('Player is in threes, on the map: ' +
                           data['session']['map'])
        elif data['session']['mode'] == 'BEDWARS_FOUR_FOUR':
            await ctx.send('Player is in fours, on the map: ' +
                           data['session']['map'])
        elif data['session']['mode'] == 'BEDWARS_TWO_FOUR':
            await ctx.send('Player is in 4v4, on the map: ' +
                           data['session']['map'])
        elif data['session']['mode'] == 'BEDWARS_FOUR_FOUR_VOIDLESS':
            await ctx.send('Player is in fours voidless, on the map: ' +
                           data['session']['map'])
        elif data['session']['mode'] == 'BEDWARS_EIGHT_TWO_VOIDLESS':
            await ctx.send('Player is in doubles voidless, on the map: ' +
                           data['session']['map'])
        elif data['session']['mode'] == 'BEDWARS_FOUR_FOUR_ARMED':
            await ctx.send('Player is in fours armed, on the map: ' +
                           data['session']['map'])
        elif data['session']['mode'] == 'BEDWARS_FOUR_FOUR_LUCKY':
            await ctx.send('Player is in fours lucky block, on the map: ' +
                           data['session']['map'])
        elif data['session']['mode'] == 'BEDWARS_FOUR_FOUR_RUSH':
            await ctx.send('Player is in fours rush, on the map: ' +
                           data['session']['map'])
        elif data['session']['mode'] == 'BEDWARS_FOUR_FOUR_ULTIMATE':
            await ctx.send('Player is in fours ultimates, on the map: ' +
                           data['session']['map'])
        elif data['session']['mode'] == 'BEDWARS_CASTLE':
            await ctx.send('Player is in bedwars castle, on the map: ' +
                           data['session']['map'])
        elif data['session']['mode'] == 'BEDWARS_EIGHT_TWO_ARMED':
            await ctx.send('Player is in doubles armed, on the map: ' +
                           data['session']['map'])
        elif data['session']['mode'] == 'BEDWARS_EIGHT_TWO_LUCKY':
            await ctx.send('Player is in doubles lucky block, on the map: ' +
                           data['session']['map'])
        elif data['session']['mode'] == 'BEDWARS_EIGHT_TWO_RUSH':
            await ctx.send('Player is in doubles rush, on the map: ' +
                           data['session']['map'])
        elif data['session']['mode'] == 'BEDWARS_EIGHT_TWO_ULTIMATE':
            await ctx.send('Player is in doubles ultimate, on the map: ' +
                           data['session']['map'])
        elif data['session']['mode'] == 'BEDWARS_PRACTICE':
            await ctx.send('Player is in practice')
        elif data['session']['mode'] == 'DUELS_BOXING_DUEL':
            await ctx.send('Player is in boxing, on the map: ' +
                           data['session']['map'])
        elif data['session']['mode'] == 'DUELS_BRIDGE_DUEL':
            await ctx.send('Player is in bridge, on the map: ' +
                           data['session']['map'])
        elif data['session']['mode'] == 'DUELS_SUMO_DUEL':
            await ctx.send('Player is in sumo, on the map: ' +
                           data['session']['map'])
        elif data['session']['mode'] == 'DUELS_CLASSIC_DUEL':
            await ctx.send('Player is in classic duels, on the map: ' +
                           data['session']['map'])
        elif data['session']['mode'] == 'DUELS_SW_DUEL':
            await ctx.send('Player is in skywars duels, on the map: ' +
                           data['session']['map'])
        elif data['session']['mode'] == 'DUELS_SW_DOUBLES':
            await ctx.send('Player is in skywars doubles duels, on the map: ' +
                           data['session']['map'])
        elif data['session']['mode'] == 'DUELS_BOW_DUEL':
            await ctx.send('Player is in bow duels, on the map: ' +
                           data['session']['map'])
        elif data['session']['mode'] == 'DUELS_UHC_DUEL':
            await ctx.send('Player is in UHC duels, on the map: ' +
                           data['session']['map'])
        elif data['session']['mode'] == 'DUELS_UHC_DOUBLES':
            await ctx.send('Player is in UHC doubles duels, on the map: ' +
                           data['session']['map'])
        elif data['session']['mode'] == 'DUELS_UHC_FOUR':
            await ctx.send('Player is in fours UHC duels, on the map: ' +
                           data['session']['map'])
        elif data['session']['mode'] == 'DUELS_UHC_MEETUP':
            await ctx.send('Player is in UHC meetup duels, on the map: ' +
                           data['session']['map'])
        elif data['session']['mode'] == 'DUELS_POTION_DUEL':
            await ctx.send('Player is in nodebuff, on the map: ' +
                           data['session']['map'])
        elif data['session']['mode'] == 'DUELS_COMBO_DUEL':
            await ctx.send('Player is in combo duels, on the map: ' +
                           data['session']['map'])
        elif data['session']['mode'] == 'DUELS_OP_DUEL':
            await ctx.send('Player is in OP solos duels, on the map: ' +
                           data['session']['map'])
        elif data['session']['mode'] == 'DUELS_OP_DUEL':
            await ctx.send('Player is in OP doubles duels, on the map: ' +
                           data['session']['map'])
        elif data['session']['mode'] == 'DUELS_MW_DUEL':
            await ctx.send('Player is in megawalls duels, on the map: ' +
                           data['session']['map'])
        elif data['session']['mode'] == 'DUELS_DOUBLESL':
            await ctx.send('Player is in double megwalls duels, on the map: ' +
                           data['session']['map'])
        elif data['session']['mode'] == 'DUELS_BLITZ_DUEL':
            await ctx.send('Player is in blitz duels, on the map: ' +
                           data['session']['map'])
        elif data['session']['mode'] == 'DUELS_BOWSPLEEF_DUEL':
            await ctx.send('Player is in bowspleef duels, on the map: ' +
                           data['session']['map'])
        elif data['session']['mode'] == 'DUELS_BRIDGE_DOUBLES':
            await ctx.send('Player is in bridge doubles duels, on the map: ' +
                           data['session']['map'])
        elif data['session']['mode'] == 'DUELS_BRIDGE_FOUR':
            await ctx.send('Player is in bridge fours duels, on the map: ' +
                           data['session']['map'])
        elif data['session']['mode'] == 'DUELS_BRIDGE_2V2V2V2':
            await ctx.send('Player is in 2v2v2v2 bridge duels, on the map: ' +
                           data['session']['map'])
        elif data['session']['mode'] == 'DUELS_BRIDGE_3V3V3V3':
            await ctx.send('Player is in 3v3v3v3 bridge duels, on the map: ' +
                           data['session']['map'])
        elif data['session']['gameType'] != 'BEDWARS':
            await ctx.send(f'Player in unkown mode:(**{data}**)')
    if not data['session']['online']:
        await ctx.send('Player offline')


bot.run(TOKEN)
