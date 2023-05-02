import disnake
from disnake.ext import commands

class Бот:
  def __init__(self, префикс, токен, интенты):
    self.prefix = префикс
    self.token = токен
    self.intents = интенты
    self.commands = {}

    self.bot = commands.Bot(command_prefix=self.prefix, intents=self.intents)

    @self.bot.event
    async def on_message(message):
      if message.content in self.commands:
        if self.commands[message.content]["mention"]:
          await message.reply(self.commands[message.content]["response"])
        else:
          await message.channel.send(self.commands[message.content]["response"])

  def команда(self, название, пинг: bool, ответ):
    if название not in self.commands:
      self.commands[f"{self.prefix}{название}"] = {"response": ответ, "mention": пинг}
    else:
      print(f"Команда {название} уже существует.")
  
  def запустить(self):
    self.bot.run(self.token)
