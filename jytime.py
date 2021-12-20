from os import replace
from mirai import GroupMessage,At
import random
import datetime
day = 0
hour = 0
minuts = 0
s = 0
def RandomNum(y):
    num=random.randint(0,y)
    return num
def RandomTime():
    global day,hour,minuts,s
    month=datetime.datetime.now().month
    year=datetime.datetime.now().year
    day=0
    if month == 1 or month == 7 or month == 3 or month == 5 or month == 8 or month == 10 or month == 12:
        day = 31
    elif month == 4 or month == 6 or month == 9 or month == 11:
        day = 30
    elif month == 2:
        if year%4 == 0 and year%100 != 0 or year%400 == 0:
            day = 29
        else :
            day = 28
    day = RandomNum(day)
    hour = RandomNum(23)
    minuts = RandomNum(59)
    s = day*24*60*60+hour*60*60+minuts*60
    return str(day)+"天"+str(hour)+"小时"+str(minuts)+"分"
def get_Id(string):
            list_str = list(string)
            list_str.pop(0)
            list_str = ''.join(list_str)
            return str(list_str)
def main(bot):
    @bot.on(GroupMessage)
    async def send_group_message(event: GroupMessage):
        async def Do(string_time,groupid,id):
            if string_time == 'd':
                global s
                string = RandomTime()
                await bot.mute(
                    memberId = id,
                    target = groupid,
                    time = s
                )
                await bot.send(event,'禁言成功'+string)
            if string_time == 'h':
                hour = RandomNum(23)
                minuts = RandomNum(59)
                s = hour*60*60+minuts*60
                string = str(hour)+"小时"+str(minuts)+"分钟"
                await bot.mute(
                    memberId = id,
                    target = groupid,
                    time = s
                )
                await bot.send(event,'禁言成功'+string)
            if string_time == 'm':
                minuts = RandomNum(59)
                s = minuts*60
                string = str(minuts)+"分钟"
                print(id)
                await bot.mute(
                    memberId = id,
                    target = groupid,
                    time = s
                )
                await bot.send(event,'禁言成功'+string)
        if "禁言/" in str(event.message_chain):
            groupid = event.group.id
            string = []
            string = str(event.message_chain).split('/',2)
            string[2] = get_Id(string[2])
            await Do(string[1],groupid,string[2])
        if "解禁/" in str(event.message_chain):
            groupid = event.group.id
            string = []
            string = str(event.message_chain).split('/',1)
            string[1] = get_Id(string[1])
            await bot.unmute(
                memberId = string[1],
                target = groupid
            )
            return bot.send(event,"解禁成功")
