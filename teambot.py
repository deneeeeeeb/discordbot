#! /home/pi/.pyenv/shims/python -u

# init
import discord
import random
import configparser
import os

client = discord.Client()


members = ["a","b","c","d", "e", "f", "g"]
pickno  = 4


# login
@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')


# res
@client.event
async def on_message(message):

    global pickno
    global members

    # if mentioned me
    if client.user.mentioned_in(message):

        if client.user != message.author \
           and message.content.count('@everyone') == 0 \
           and message.content.count('@here') == 0:

            # get message
            message_list = message.content.split()

            
            # 0) print info
            if len(message_list) == 2 and message_list[1] == "info":
                print('hit0')

                # send message
                m = "pickup : " + str(pickno) + "\n"
                m = m + "members : "
                for member in members:
                    m = m + member + " "
                await client.send_message(message.channel, m)

            # 1) set pick number
            elif len(message_list) == 2:
                print('hit1')
                # global pickno
                pickno = int(message_list[1])

                # send message
                m = "pickup : " + str(pickno)
                await client.send_message(message.channel, m)


            # 2) set members
            # set members & just exec team
            elif len(message_list) > 1:
                print('hit2')
                new_members = []
                target_members = message_list[1:]
                for member in target_members:
                    new_members.append(member)
                # global members
                members = new_members
                result_members = random.sample(members, pickno)
                print(''.join(map(str, result_members)))

                # send message
                m = "members : "
                for member in members:
                    m = m + member + " "
                await client.send_message(message.channel, m)


            # 3) exec pickup
            # just exec team
            else:
                print('hit3')
                result_members = random.sample(members, pickno)
                print(''.join(map(str, result_members)))

                # send message
                m = ""
                for member in result_members:
                    m = m + member + " "
                await client.send_message(message.channel, m)



# run
confpath = os.path.dirname(os.path.abspath(__file__)) + "/etc/token.conf"
inifile = configparser.ConfigParser()
inifile.read(confpath, 'UTF-8')
TOKEN=inifile.get('prod', 'TEAM_SELECTOR')
client.run(TOKEN)

