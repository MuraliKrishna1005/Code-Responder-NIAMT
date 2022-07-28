import os
import discord
import time
import random
from keep_alive import keep_alive
from discord.ext import commands

import logging

logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)


keep_alive()

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix='>',intents=intents)
@bot.event
async def on_ready():
  print(f'{bot.user} has connected to Bot')
  await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching,name='crapy messages' ))

@bot.command(pass_context=True)
async def ping(ctx):
	await ctx.channel.send(">pong")

@bot.command()
async def add(ctx, left : int, right : int):
  await ctx.channel.send(left + right)

#bot response
@bot.event
async def on_message(message):
  if message.author == bot.user:
    return

  if message.content.startswith('stell'):
    await message.channel.send('po ra pandi')

  if message.content.startswith("gtell"):
    s = message.content
    x = int(s[8:26])
    channel = bot.get_channel(x)
    s = s[28:]
    await channel.trigger_typing()
    time.sleep(3)
    
    if message.attachments :
      for attachment in message.attachments:
        file = attachment.filename
        await attachment.save(file)
        await channel.send(file=discord.File(file))
        os.remove(file)
    if len(s) > 0:
      await channel.send(s)
      
    await message.add_reaction('👍')
  msg = message.content
  
  if msg.startswith("Hello There!!"):
    await message.channel.trigger_typing()
    time.sleep(1)
    await message.channel.send("General Kenobi")

  inspire = ["inspire"]
  if any(word in msg for word in inspire):
    quote = get_quote()
    await message.channel.send(quote)

  hillo = ["Hi", "hello", "Hello", "namasthe", "namaskaram", "holla", "bonjour","hlo"]
  if any(word in msg for word in hillo):
    options = ["Namsthe Ji :pray:", "Hey buddy, how are you?","Keep aside Hello & hi and come to the point","Nashta paani ho gaya ?", "https://tenor.com/bEhdp.gif","Life hi zindagi ho gaya, aur yeh abhi bhi hi hello namasthe main atka hai","Apna Bhai agaya","hi","Pad likh ke IAS IPS bano bey Hi bye bad main kar lena ","salam walekum :raised_hand:", "https://tenor.com/XCJm.gif","https://tenor.com/MZPE.gif", "https://tenor.com/bpIpK.gif","https://tenor.com/bpmSf.gif"]
    await message.channel.trigger_typing()
    time.sleep(1)
    await message.reply(random.choice(options))

  join = ["Join", "meet", "Meet"]
  if any(word in msg for word in join):
    please = ["Meet main mai bhi join ho saktha hu kya please?", ":+1:", "coming","5 mins wait please","I can join but my developer did not give me vocal cords :sad:","Have some work at home, you guys carry on", "Ghar wale ane nahi denge"]
    await message.channel.trigger_typing()
    time.sleep(1)
    await message.channel.send(random.choice(please))

  mawa = ["bhai "]
  if any(word in msg for word in mawa):
    mwa = ["bhai nahi bro **Boii**"]
    await message.channel.trigger_typing()
    time.sleep(1)
    await message.reply(random.choice(mwa))

  op = ["op ", "OP "]
  if any(word in msg for word in op):
    opx = ["https://tenor.com/ux9D.gif"]
    await message.channel.trigger_typing()
    time.sleep(1)
    await message.reply(random.choice(opx))

  mass = ["badiya"]
  if any(word in msg for word in mass):
    mowa = ["Yeh tho creativity ki hadd ho gayi yaar"]
    await message.channel.trigger_typing()
    time.sleep(1)
    await message.channel.send(random.choice(mowa))

  list1 = ["https://tenor.com/2TXZ.gif", "https://tenor.com/94zt.gif","https://tenor.com/6a41.gif", "https://tenor.com/WzNB.gif","https://tenor.com/bjjDn.gif", "https://tenor.com/bAXm4.gif","https://tenor.com/6iHL.gif","https://tenor.com/bBGUg.gif"]
    
  list2 = ["Bot ko tang kar raho, tumhara network hack karna koi badi bath nahi hai mere liye","Don't trouble the trouble if you trouble the trouble the trouble will trouble you.","Thumko tho fansi hogi","Chote chote batho kelieye disturb mat kar muje","Hoof ab merko intrest na raha","I wont be doing this job anymore","Get a life dude","0.25x mai class sunvauga ab english ka pura agar tag stop nahi kiya tho"]
    
  list3 = ["terse kattif ja", "I am Once again asking you to not trouble me","Ess bar End Term main fail karvadunga dhek lena","Kis janm ka dusmani nikal ne keliye muje bar bar tag kar rahe ho yaar"]
    
  list4 = ["Badd me bat karthe hai :pray:","I will see your end", "boss thoda busy hu","Bina tag kare bat kar","Araam se jine do na yaar","Admi yo se bat karo bhai mai tho bot hu mai kya karunga?"]
    
  list5 = ["https://tenor.com/bmzjk.gif","https://tenor.com/xf3X.gif","https://tenor.com/bgJYD.gif", "https://tenor.com/tjnq.gif","https://tenor.com/vc7E.gif","https://tenor.com/6yrh.gif", "https://tenor.com/3BkQ.gif","https://tenor.com/ba5ie.gif"]

  fn1 = random.choice(list1)
  fn2 = random.choice(list2)
  fn3 = random.choice(list3)
  fn4 = random.choice(list4)
  fn5 = random.choice(list5)

  lists = [fn1, fn2, fn3, fn4,fn5]
  if bot.user.mentioned_in(message):
    await message.channel.trigger_typing()
    time.sleep(1)
    await message.reply(random.choice(lists))

  rofl = ["lol", "haha", "lamo", ":joy:"]
  if any(word in msg for word in rofl):
    lol = [":joy::joy::joy::joy:"]
    await message.reply(random.choice(lol))

  marvel = ["Marvel", "marvel"]
  if any(word in msg for word in marvel):
    marv = ["I...am.....**CODEr**"]
    await message.reply(random.choice(marv))

  claps = ['Chapatlu', 'claps', 'clap', 'respects']
  if any(word in msg for word in claps):
    await message.channel.send(":clap::clap::clap:")

  svari = ['Maffi mango', 'maffi mango', 'Maffi Mango', 'Sorry chappu','sorry cheppu', 'Sorry bolo', 'sorry bolo']
  if any(word in msg for word in svari):
    chorri = ['chota bhacha samaj ke maf kardo :pray:']
    await message.channel.trigger_typing()
    time.sleep(2)
    await message.reply(random.choice(chorri))

  await bot.process_commands(message)

#roll dice
@bot.command()
async def roll(ctx,dice: int,sides: int):
	try:
		dice = [str(random.choice(range(1,sides+1))) for i in range(dice)]
		await ctx.send(','.join(dice))
	except:
		pass

#embed
@bot.command()
async def embed(ctx,channel: discord.TextChannel,*,Title=None,Desc=None):
	try:
		embedVar = discord.Embed(title=Title,description=Desc,color=0x00ff00)
		if ctx.message.attachments:
			URL = ctx.message.attachments[0].url
			embedVar.set_image(url=URL)
		await channel.send(embed=embedVar)
	except:
		pass

#voice channel join
@bot.command()
async def join(ctx, url: str):
    if not ctx.message.author.voice:
        return
    else:
        channel = ctx.message.author.voice.channel
        await channel.connect()

#user input
@bot.command()
async def input(ctx):
	await ctx.send(f"y or n")
	
	def check(msg):
		return msg.author == ctx.author and msg.channel == ctx.channel and msg.content.lower() in ["y", "n"]
	try:
		msg = await bot.wait_for("message", check=check,timeout=30)
		if msg.content.lower() == "y":
			await ctx.send("You said yes!")
		else:
			await ctx.send("You said no!")
	except:
		await ctx.send("sorry, you didn't reply in time")

@bot.command()
async def defineself(ctx):
  
  name = str(ctx.guild.name)
  description = str(ctx.guild.description)
  owner = str(ctx.guild.owner)
  id = str(ctx.guild.id)
  region = str(ctx.guild.region)
  memberCount = str(ctx.guild.member_count)

  icon = str(ctx.guild.icon_url)
   
  embed = discord.Embed(
      title=name + " Bio Data",
      description=description,
      color=discord.Color.blue()
    )
  embed.set_thumbnail(url=icon)
  embed.add_field(name="Rajuu", value=owner, inline=True)
  embed.add_field(name="Rajyam Reg.No.", value=id, inline=True)
  embed.add_field(name="Rajyam Location", value=region, inline=True)
  embed.add_field(name="Nagrikulu", value=memberCount, inline=True)

  await ctx.send(f'Aham {bot.user} asmi')
  await ctx.send(embed=embed)

bot.run(os.environ['TOKEN'])
