""" Module to automate message deletion. """
import random
from asyncio import sleep
from datetime import datetime, timedelta, timezone
from telethon.tl.functions.account import UpdateProfileRequest
from emoji import emojize
from pagermaid import bot, log, version
from pagermaid.listener import listener

auto_change_name_init = False
#dizzy = emojize(":dizzy:", use_aliases=True)
#cake = emojize(":cake:", use_aliases=True)
all_time_emoji_name = ["clock12", "clock1230", "clock1", "clock130", "clock2", "clock230", "clock3", "clock330",
                       "clock4", "clock430", "clock5", "clock530", "clock6", "clock630", "clock7", "clock730", "clock8",
                       "clock830", "clock9", "clock930", "clock10", "clock1030", "clock11", "clock1130"]
#time_emoji_symb = [emojize(":%s:" % s, use_aliases=True) for s in all_time_emoji_name]


@listener(incoming=True, outgoing=True, ignore_edited=True)
async def change_name_auto(context):
    global auto_change_name_init
    if auto_change_name_init:
        return
    else:
        auto_change_name_init = True
    await log("开始每 30 秒更新一次 last_name")
    while True:
        try:
            time_cur = datetime.utcnow().replace(tzinfo=timezone.utc).astimezone(timezone(
                timedelta(hours=8))).strftime('%H:%M:%S:%p:%a')
            hour, minu, seco, p, abbwn = time_cur.split(':')
            if seco == '00' or seco == '20' or seco == '40':
                shift = 0
                mult = 1
                if int(minu) > 30: shift = 1
                # print((int(hour)%12)*2+shift)
                # hour symbols
                # hsym = time_emoji_symb[(int(hour)%12)*2+shift]
                # await client1.send_message('me', hsym)
                last_names = ['故事的小黄花', '从出生那年就飘着', '童年的荡秋千', '随记忆一直晃到现在', 'ReSoSoSiDoSiLa', 'SoLaSiSiSiSiLaSiLaSo',
                              '吹着前奏望着天空', '我想起花瓣试着掉落', '为你翘课的那一天', '花落的那一天', '教室的那一间', '我怎么看不见', '消失的下雨天', '我好想再淋一遍',
                              '没想到失去的勇气我还留着', '好想再问一遍', '你会等待还是离开', '刮风这天我试过握着你手', '但偏偏雨渐渐大到我看你不见', '还要多久我才能在你身边',
                              '等到放晴的那天也许我会比较好一点', '从前从前有个人爱你很久', '但偏偏风渐渐把距离吹得好远', '好不容易又能再多爱一天', '但故事的最后你好像还是说了拜拜',
                              '为你翘课的那一天', '花落的那一天', '教室的那一间', '我怎么看不见', '消失的下雨天', '我好想再淋一遍', '没想到失去的勇气我还留着', '好想再问一遍',
                              '你会等待还是离开', '刮风这天我试过握着你手', '但偏偏雨渐渐大到我看你不见', '还要多久我才能在你身边', '等到放晴的那天也许我会比较好一点',
                              '从前从前有个人爱你很久', '偏偏风渐渐把距离吹得好远', '好不容易又能再多爱一天', '但故事的最后你好像还是说了拜拜', '刮风这天我试过握着你手',
                              '但偏偏雨渐渐大到我看你不见', '还要多久我才能够在你身边', '等到放晴那天也许我会比较好一点', '从前从前有个人爱你很久', '但偏偏雨渐渐把距离吹得好远',
                              '好不容易又能再多爱一天', '但故事的最后你好像还是说了拜', '静止了所有的花开', '遥远了清晰了爱', '天郁闷爱却很喜欢', '那时候我不懂', '这叫爱',
                              '你喜欢站在那窗台', '你好久都没再来', '彩色的', '时间染上空白', '是你流的泪晕开', '不要你离开', '距离隔不开', '思念变成海', '在窗外进不来',
                              '原谅说太快', '爱成了阻碍', '手中的风筝', '放太快回不来', '不要你离开', '回忆划不开', '欠你的宠爱', '我在等待重来', '天空仍灿烂',
                              '它爱着大海', '情歌被打败', '爱已不存在', '你喜欢站在那窗台', '你好久都没再来', '彩色的时间', '染上空白', '是你流的泪晕开', '不要你离开',
                              '距离隔不开', '思念变成海', '在窗外进不来', '原谅说太快', '爱成了阻碍', '手中的风筝', '放太快回不来', '不要你离开', '回忆划不开',
                              '欠你的宠爱', '我在等待重来', '天空仍灿烂', '它爱着大海', '情歌被打败', '爱已不存在']
                k = random.randint(0, 95)
                first_name = last_names[k]
                last_name = '大脑斧 %s:%s  ' % (hour, minu)

                await client1(UpdateProfileRequest(first_name=first_name, last_name=last_name))
                logger.info('Updated -> %s' % first_name)
                logger.info('Updated -> %s' % last_name)
            '''if seco == '00' or seco == '30':
                shift = 0
                if int(minu) > 30: shift = 1
                hsym = time_emoji_symb[(int(hour) % 12) * 2 + shift]
                for_fun = random.random()
                if for_fun < 0.10:
                    last_name = '%s时%s分 %s' % (hour, minu, hsym)
                elif for_fun < 0.30:
                    last_name = '%s:%s %s %s %s' % (hour, minu, p, abbwn, hsym)
                elif for_fun < 0.60:
                    last_name = '%s:%s %s UTC+8 %s' % (hour, minu, p, hsym)
                elif for_fun < 0.90:
                    last_name = '%s' % dizzy
                else:
                    last_name = '%s' % cake 
                await bot(UpdateProfileRequest(last_name=last_name)) '''
        except:
            pass
        await sleep(1)
