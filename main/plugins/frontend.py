#Github.com/Vasusen-code

import time, os

from .. import bot as Drone
from .. import userbot, Bot
from .. import FORCESUB as fs
from main.plugins.pyroplug import get_msg
from main.plugins.helpers import get_link, join, screenshot

from telethon import events
from pyrogram.errors import FloodWait

from ethon.telefunc import force_sub

ft = f"要使用此机器人，您必须加入 @{fs}."

message = "将您想要开始保存的消息链接发送给我，作为对此消息的回复。"
          
process=[]
timer=[]
user=[]

# To-Do:
# Make these codes shorter and clean
# ofc will never do it. 

@Drone.on(events.NewMessage(incoming=True, func=lambda e: e.is_private))
async def clone(event):
    if event.is_reply:
        reply = await event.get_reply_message()
        if reply.text == message:
            return
    try:
        link = get_link(event.text)
        if not link:
            return
    except TypeError:
        return
    s, r = await force_sub(event.client, fs, event.sender_id, ft)
    if s == True:
        await event.reply(r)
        return
    edit = await event.reply("处理中!")
    if f'{int(event.sender_id)}' in user:
        return await edit.edit("请不要发送垃圾链接，请等待正在进行的过程完成。")
    user.append(f'{int(event.sender_id)}')
    try:
        if 't.me/+' in link:
            q = await join(userbot, link)
            await edit.edit(q)
        if 't.me/' in link:
            await get_msg(userbot, Bot, event.sender_id, edit.id, link, 0)
    except FloodWait as fw:
        await Drone.send_message(event.sender_id, f'由于来自电报的 floodwait，请在 {fw.x} 秒后重试。')
    except Exception as e:
        print(e)
        await Drone.send_message(event.sender_id, f"复制 `{link}` 时出错\n\n**错误：** {str(e)}")
    ind = user.index(f'{int(event.sender_id)}')
    user.pop(int(ind))
