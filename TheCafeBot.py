#I want the bot to print out a greeting and explain that it is a coffee brewing sim, and then I want it to send reactions to it's own message. If a user clicks on these reactions, then
#I want a function to handle the reaction based upon 

import discord
import random
from discord.ext import commands
import cafe_bot_token



bases_dict = {
	"☕" : {
		"Description" : "Dirty bean juice. Gotta love it.",
		"Cost" : 2,
		"Name" : "Coffee"
		},

	"🥛" : {
		"Description" : "Moo juice.",
		"Cost" : 2,
		"Name" : "Milk"
		},

	"🍵" : {
		"Description" : "Dirty leaf juice. It's okay.",
		"Cost" : 2,
		"Name" : "Tea"
		}
	}


additives_dict = {
	"🌲" : {
		"Name" : "Cinnamon",
		"Description" : "Who knew this was tree bark?",
		"Cost" : 2
	},

	"🧂" : {
		"Name" : "Sugar",
		"Description" : "Sweet crystals",
		"Cost" : 1
	},

	"🍫" : {
		"Name" : "Cocoa Powder",
		"Description" : "Surprisingly bitter on its own",
		"Cost" : 2
	}
}
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)
token = cafe_bot_token.Cafebottoken

@bot.event
async def on_ready():
	print(f"{bot.user} is online.")


@bot.command()
async def coffee(ctx,):
	channel = bot.get_channel(1033607560063877172)
	text= '> Welcome to the cafe. Below are some options for you to choose from.'

	sent_message = await channel.send(text)
	await sent_message.add_reaction('☕')
	await sent_message.add_reaction('🥛')
	await sent_message.add_reaction('🍵')

def cost_format(cost):
	return "${:,.2f}".format(cost)

cost = 0

@bot.event
async def on_reaction_add(reaction, user):
    channel = bot.get_channel(1033607560063877172)
    if user.bot == True:
        return

    print()

    if reaction.message.channel.id != channel.id:
        return

    base_choice = reaction.emoji

    if base_choice in bases_dict:
        global cost
        cost += bases_dict[base_choice]["Cost"]
        await channel.send(bases_dict[base_choice]["Description"])
        await channel.send( 'The cost of this base is : {0}'.format(cost_format(bases_dict[base_choice]["Cost"])))
        await channel.send(' Your total so far is {0}'.format(cost_format(cost)))



bot.run(token)
