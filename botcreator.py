filename = input('botname: ')
file = filename + '.py'
bot = open(file, "w+", encoding='utf-8')
to = input('token: ')
bot.write('token = "%0s"' %(to))
bot.write('# made by botcreator.py\n'
           'import config\n'
           'import discord\n'
           'class MyClient(discord.Client):\n'
            '    async def on_ready(self):\n'
            "       print('Logged on as %0s!')\n" %(filename))
bot.write("    async def on_message(self, message):\n"
          "        print(str(message.channel) + ':\\n' + str(message.created_at) + ' ' + str(message.author) + ':' + str(message.content))\n"
          "        if message.author == self.user:\n"
          "            return\n")
f = 0
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
        if f == 0:
            bot.write("        if message.content == '%1s':\n"
                      "            await message.channel.send('%1s')\n" % (ontext, text))
        else:
            bot.write("        elif message.content == '%1s':\n"
                        "            await message.channel.send('%1s')\n" %(ontext, text))

    elif name == '2':
        bot.write('client = MyClient()\n'
                     'client.run(token)\n')
        run = False
    else:
        print('is not correct!')
    f = 1
bot.close()
