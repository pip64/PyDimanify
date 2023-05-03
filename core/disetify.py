import disnake
from disnake.ext import commands
import re
from dimanify import *
from core.markov import *
from core.tryexcept import *
from core.conditions import *
from core.files import *
from core.variables import *
from core.texts import *
from core.randoms import *
from core.funcs import *
from core.other import *
from core.requests import *
from core.cycles import *
#from core.disetify import *

class Бот:
  def __init__(self, префикс, токен, интенты):
    self.prefix = префикс
    self.token = токен
    self.intents = интенты
    self.commands = {}
    self.events = {}

    self.bot = commands.Bot(command_prefix=self.prefix, intents=self.intents)

    @self.bot.event
    async def on_message(message):
      for_changes = {
              "автор": message.author,
              "автор.айди": message.author.id,
              "автор.ник": message.author.name,
              "автор.тег": message.author.discriminator,
              "сообщение": message,
              "сообщение.содержимое": message.content,
              "сообщение.айди": message.id
      }
      if message.content in self.commands:
        if self.commands[message.content]["mention"]:
          await message.reply(self.commands[message.content]["response"])
        else:
          await message.channel.send(self.commands[message.content]["response"])
      for event in self.events:
        if self.events[event]["type"] == "при сообщении":
          if self.events[event]["respond"] != None:
            await message.send(self.events[event]["respond"])

  def команда(self, название, пинг: bool, ответ):
    if название not in self.commands:
      self.commands[f"{self.prefix}{название}"] = {"response": ответ, "mention": пинг}
    else:
      print(f"Команда {название} уже существует.")

  def эвэнт(self, название, тип, ответ, код):
    if название not in self.events:
      if тип in ["при сообщении", "при старте"]:
        if тип == "при сообщении":
          self.events[название] = {"type": тип, "respond": ответ, "code": код}
        elif тип == "при старте":
          self.events[название] = {"type": тип, "code": код}
      else: 
        print(f"Эвэнт {название} уже существует!")
        
  def запустить(self):
    self.bot.run(self.token)