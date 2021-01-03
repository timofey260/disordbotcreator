def menud(pa1, pa2):
    print("[" + str(pa1) + "] " + pa2)


menud(1, 'crate')
menud(2, 'open')
mode = input()
if mode == '1':
    filename = input('botname: ')
    filep = filename + '.py'
    filet = filename + '.txt'
    bot = open(filet, "w+", encoding='utf-8')def menud(pa1, pa2):
    print("[" + str(pa1) + "] " + pa2)


menud(1, 'create')
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
    filemes = "onmessage for %0s.txt" % filename
    botmescl = 0
    run = True
    while run:

        menud(1, 'ontext')
        menud(2, 'exit')
        menud(3, 'create py')
        name = input('>>> ')
        if name == '1':
            ontext = input('user text: ')
            text = input('bot text: ')

            if botmescl == 1:
                botmes = open(filemes, 'a')
                botmes.write("        elif message.content == '%1s':\n"
                             "            await message.channel.send('%1s')\n" % (ontext, text))
                botmes.close()
            elif botmescl == 0:
                botmes = open(filemes, 'w+')
                botmes.write("        elif message.content == '%1s':\n"
                             "            await message.channel.send('%1s')\n" % (ontext, text))
                botmes.close()
                botmescl = 1
        elif name == '2':
            run = False

        elif name == '3':
            bot.close()
            botl = open(filet).readlines()
            botf = open(filep, 'w+')
            botmes = open(filemes).readlines()
            for x in botl:
                botf.write(x)
                print(x)
            for y in botmes:
                botf.write(y)
                print(y)
            botf.write('client = MyClient()\n'
                       'client.run(token)\n')

            botf.close()

        else:
            print('is not correct!')

elif mode == '2':
    filename = input('filename: ')
    filemes = "onmessage for %0s.txt" % filename
    filep = filename + '.py'
    filet = filename + '.txt'
    bot = open(filet, 'a', encoding='utf-8')
    run = True
    while run:
        menud(1, 'ontext')
        menud(2, 'exit')
        menud(3, 'create py')
        name = input('>>> ')
        if name == '1':
            ontext = input('user text: ')
            text = input('bot text: ')
            botmesopn = 1
            try:
                botmes = open(filemes, 'a')
            except:
                botmesopn = 0
            if botmesopn == 0:
                botmes = open(filemes, "w+")
                botmes.write("        elif message.content == '%1s':\n"
                      "            await message.channel.send('%1s')\n" % (ontext, text))
            elif botmesopn == 1:
                botmes = open(filemes, "a")
                botmes.write("        elif message.content == '%1s':\n"
                      "            await message.channel.send('%1s')\n" % (ontext, text))
            botmes.close()
        elif name == '2':
            run = False

        elif name == '3':
            bot.close()
            botl = open(filet).readlines()
            botf = open(filep, 'w+')
            try:
                botmes = open(filemes).readlines()
            except:
                print('not message')
            for x in botl:
                botf.write(x)
                print(x)
            try:
                for y in botmes:
                    botf.write(y)
                    print(y)
            except:
                print("not message compilate")
            botf.write('client = MyClient()\n'
                       'client.run(token)\n')

            botf.close()

        else:
            print('is not correct!')

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

elif mode == '2':
    filename = input('filename: ')
    filep = filename + '.py'
    filet = filename + '.txt'
    bot = open(filet, 'a', encoding='utf-8')
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
