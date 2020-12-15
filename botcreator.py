g = 'bot.py'
c = 'config.py'
bot = open(g, "w", encoding='utf-8')
to = input('token: ')
config = open(c, 'w', encoding='utf-8')
config.write('token = "%0s"' %(to))
bot.write('# made by botcreator.py\n'
           'import config\n'
           'import discord\n'
           'class MyClient(discord.Client):\n'
            '    async def on_ready(self):\n'
            "       print('Logged on as {0}!'.format(self.user))\n")
bot.write("    async def on_message(self, message):\n"
          "        print(str(message.channel) + ':\\n' + str(message.created_at) + ' ' + str(message.author) + ':' + str(message.content))\n"
          "        if message.author == self.user:\n"
          "            return\n")
bot.write("        if message.content == 'Hi' or message.content == 'HI':\n"
          "           await message.channel.send('Hi @' + str(message.author) + '!')\n")
def menud(pa1, pa2):
    print("[" + str(pa1) + "] " + pa2)
run = True
while run:
    menud(1, 'ontext')
    menud(2,'end')
    name = input('>>> ')
    if name == '1':
        ontext = input('user text: ')
        text = input('bot text: ')
        bot.write("        elif message.content == '%1s':\n"
                  "            await message.channel.send('%1s')\n" %(ontext, text))

    if name == '2':
        bot.write('client = MyClient()\n'
                     'client.run(config.token)\n')
        run = False
    else:
        print('is not correct!')
