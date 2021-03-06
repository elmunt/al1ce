#!/usr/bin/env python       #Indication d'un fichier python.
# -*- coding: utf-8 -*-     #Lecture du fichier sous format UTF-8 (inclut les accents).

import discord, subprocess, os, youtube_dl      #Importer des fonctions des autres modules.
from discord.ext import commands    #Importer des commandes depuis le fichier «discord.ext».

file=open('/home/al1ce/Bot/token.txt', 'r')     #Définit la variable «file» sur le contenu du fichier «token.txt».
TOKEN = file.read().rstrip("\n")        #Module discord, lecture du «TOKEN» contenu dans la variable «file».

description = '''AL1CE_Bot in Python'''     #Description du bot.
bot = commands.Bot(command_prefix='.', description=description)     #Définit le préfixe «.» pour ordonner le bot.
bot.remove_command('help')

@bot.event      #Démarrage du bot.
async def on_ready():       #Définit la fonction de démarrage «on_ready».
    print('------')     #Affiche des marges sur le terminal pour rendre lisible le contenu (esthétique).
    print('Logged in as')       #Afficher l'identification du bot (le nom).
    print(bot.user.name)
    print("ID : " + bot.user.id)
    print("Token : " + TOKEN)       #Afficher le token utilisé sur le terminal.
    print('------')
    await bot.change_presence(game=discord.Game(name='you, master ... <3', type=2))     #Définit le statut du bot pour les utilisateurs «listening to».

players = {}
    
class Voice:
  def __init__(self, client):
    self.client = client
    
#Commands

@bot.command()      #Définit une commande pour le bot.
async def hello():      #Définit la fonction «hello».
    """Al1ce answers you!"""        #Description de la commande «hello».
    gitEmbed=discord.Embed(title="Who am I?", description="Hi! My name is Al1ce, and i was created to make your life easier! =D", color=0x0080ff)       #Définit le contenu de la fonction «hello».
    gitEmbed.set_author(name="AL1CE", icon_url="https://i.imgur.com/TwxY5sr.png")       #Ajout des images pour rendre plus esthétiques la commande.
    gitEmbed.set_thumbnail(url="https://i.imgur.com/TwxY5sr.png")
    await bot.say(embed=gitEmbed)       #Lecture de la commande par le bot.

@bot.command()      #Définit une commande pour le bot.
async def github():     #Définit la fonction «github».
    """Give github's link"""        #Descritpion de la commande «github».
    gitEmbed=discord.Embed(title="GitHub", url="https://github.com/NicksQ69/al1ce", description="GitHub by NicksQ69, co-written with Squidoss and Elmunt", color=0x0080ff)      #Définit le contenu de la fonction «github».
    gitEmbed.set_author(name="AL1CE", icon_url="https://i.imgur.com/TwxY5sr.png")       #Ajout des images pour rendre plus esthétiques la commande.
    gitEmbed.set_thumbnail(url="https://i.imgur.com/IHRXykr.png")
    await bot.say(embed=gitEmbed)       #Lecture de la commande par le bot.
    #await bot.say("https://github.com/NicksQ69/al1ce")

@bot.command()      #Définit une commande pour le bot.
async def website():        #Définit la fonction «website».
    """Give official website's link"""      #Description de la commande «website».
    gitEmbed=discord.Embed(title="AL1CE", url="http://al1ce.fr", description="Official website of AL1CE, made by NicksQ69", color=0x0080ff)     #Définit le contenu de la fonction «website».
    gitEmbed.set_author(name="AL1CE", icon_url="https://i.imgur.com/TwxY5sr.png")       #Ajout des images pour rendre plus esthétiques la commande.
    gitEmbed.set_thumbnail(url="https://i.imgur.com/Tyohpwv.png")
    await bot.say(embed=gitEmbed)       #Lecture de la commande par le bot.
    #await bot.say("http://al1ce.fr")

@bot.command(pass_context=True)     #Définit une commande pour le bot.
async def reboot(ctx):      #Définit la fonction «reboot».
    """Ask to reboot now"""     #Description de la commande «reboot».
    if ctx.message.author.id == '192361476844027904','357566595029008387':       #Si l'identification correspond à l'identification donnée, ...
        await bot.say("Restart in progress")        #Alors, le programme de redémarrage s'éffectue.
        await bot.say("{} , my beloved master ... <3.".format(ctx.message.author.mention))
        print("Restart in progress")
        subprocess.call("./start.sh", shell=True)       #Exécute le programme "shell" : «start.sh»
        sys.exit()      #Fermeture du programme «bot.py».
    else:       #Sinon, ...
        await bot.say("Unauthorized access")        #Afficher que l'accès n'est pas autorisé.
        
@bot.command()      #Définit une commande pour le bot.
async def ping():   #Définit la fonction «ping».
    """Replies pong !"""        #Description de la commande «ping».
    message.author.send("Pong !")      #Lecture de la commande par le bot.

#Voice commands
  
@commands.command(pass_context=True)
async def join(self, ctx):
    channel = ctx.message.author.voice.voice_channel
    await self.client.join_voice_channel(channel)
    await self.client.say(":microphone: Joined '{}' voice channel :microphone:".format(channel.name))

@commands.command(pass_context=True)
async def leave(self, ctx):
    channel = ctx.message.author.voice.voice_channel
    server = ctx.message.server
    voice_client = self.client.voice_client_in(server)
    await voice_client.disconnect()
    await self.client.say(":microphone: Left '{}' voice channel :microphone:".format(channel.name))
    
@commands.command(pass_context=True)
async def play(self, ctx, url):
    server = ctx.message.server
    voice_client = self.client.voice_client_in(server)
    player = await voice_client.create_ytdl_player(url)
    players[server.id] = player
    player.start()
    await self.client.say(":musical_note: Now playing : {} :musical_note:".format(url))
    
@commands.command(pass_context=True)
async def pause(self, ctx):
    id = ctx.message.server.id
    players[id].pause()
    await self.client.say(":pause_button: Music paused :pause_button:")
    
@commands.command(pass_context=True)
async def resume(self, ctx):
    id = ctx.message.server.id
    players[id].resume()
    await self.client.say(":play_pause: Music resumed :play_pause:")
    
@commands.command(pass_context=True)
async def stop(self, ctx):
    id = ctx.message.server.id
    players[id].stop()
    await self.client.say(":stop_button: Music stopped :stop_button:")
    
def setup(client):
  client.add_cog(Voice(client))
    
bot.run(TOKEN)      #Exécution du bot à partir de la variable «TOKEN».
