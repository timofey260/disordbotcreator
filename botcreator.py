def menud(pa1, pa2):
    print("[" + str(pa1) + "] " + pa2)
menud(1, 'crate')
menud(2, 'open')
mode = input()
if mode == '1':
    filename = input('botname: ')
    filep = filename + '.py'
    filet = filename + '.txt'
    bot = open(filet, "w+", encoding='utf-8')
    to = input('token: ')
    bot.write('token = "%0s"\n' % to)
    bot.write('# made by botcreator\n'
              'import discord\n'
              'class MyClient(discord.Client):\n'
              '    async def on_ready(self):\n'
              "       print('Logged on as %0s!')\n"
              "    async def on_message(self, message):\n"
              "        print(str(message.author) + ': ' + str(message.content))\n"
              "        if message.author == self.user:\n"
              "            return\n" % filename)

    f = 0
    run = True
    while run:
        menud(1, 'ontext')
        menud(2, 'exit')
        menud(3, 'create py')
        name = input('>>> ')
        if name == '1':
            ontext = input('user text: ')
            text = input('bot text: ')
            bot = open(filet, 'a')

            bot.write("        elif message.content == '%1s':\n"
                      "            await message.channel.send('%1s')\n" % (ontext, text))

        elif name == '2':
            run = False

        elif name == '3':
            bot.close()
            botl = open(filet).readlines()
            botf = open(filep, 'w+')
            for x in botl:
                botf.write(x)
            botf.write('client = MyClient()\n'
                       'client.run(token)\n')

            botf.close()

        else:
            print('is not correct!')
        f = 1
elif mode == '2':
    filename = input('filename: ')
    filep = filename + '.py'
    filet = filename + '.txt'
    bot = open(filet, 'a', encoding='utf-8')
    run = True
    f = 0
    while run:
        menud(1, 'ontext')
        menud(2, 'exit')
        menud(3, 'create py')
        name = input('>>> ')
        if name == '1':
            ontext = input('user text: ')
            text = input('bot text: ')
            bot = open(filet, 'a')
            if f == 0:
                bot.write("        if message.content == '%1s':\n"
                          "            await message.channel.send('%1s')\n" % (ontext, text))
            else:
                bot.write("        elif message.content == '%1s':\n"
                          "            await message.channel.send('%1s')\n" % (ontext, text))

        elif name == '2':
            run = False

        elif name == '3':
            bot.close()
            botl = open(filet).readlines()
            botf = open(filep, 'w+')
            for x in botl:
                botf.write(x)
            botf.write('client = MyClient()\n'
                       'client.run(token)\n')

            botf.close()

        else:
            print('is not correct!')
        f = 1
