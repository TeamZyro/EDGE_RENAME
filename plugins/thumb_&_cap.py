from pyrogram import Client, filters 
from helper.database import db

from bot import Bot 

@Bot.on_message(filters.private & filters.command(['set_caption', 'setcaption']))
async def add_caption(client, message):
    if len(message.command) == 1:
       return await message.reply_text("**Gɪᴠᴇ Tʜᴇ Cᴀᴩᴛɪᴏɴ\n\nExᴀᴍᴩʟᴇ:- `/set_caption {filename}\n\n💾 Sɪᴢᴇ: {filesize}\n\n⏰ Dᴜʀᴀᴛɪᴏɴ: {duration}`**")
    caption = message.text.split(" ", 1)[1]
    await db.set_caption(message.from_user.id, caption=caption)
    await message.reply_text("**✅ Cᴀᴩᴛɪᴏɴ Sᴀᴠᴇᴅ**")
   
from bot import Bot 

@Bot.on_message(filters.private & filters.command(['del_caption', 'delcaption']))
async def delete_caption(client, message):
    caption = await db.get_caption(message.from_user.id)  
    if not caption:
       return await message.reply_text("**😔 Yᴏᴜ Dᴏɴ'ᴛ Hᴀᴠᴇ Aɴy Cᴀᴩᴛɪᴏɴ**")
    await db.set_caption(message.from_user.id, caption=None)
    await message.reply_text("**❌️ Cᴀᴩᴛɪᴏɴ Dᴇʟᴇᴛᴇᴅ**")
                                       
from bot import Bot 

@Bot.on_message(filters.private & filters.command(['see_caption', 'view_caption']))
async def see_caption(client, message):
    caption = await db.get_caption(message.from_user.id)  
    if caption:
       await message.reply_text(f"**Yᴏᴜ'ʀᴇ Cᴀᴩᴛɪᴏɴ:-**\n\n`{caption}`")
    else:
       await message.reply_text("**😔 Yᴏᴜ Dᴏɴ'ᴛ Hᴀᴠᴇ Aɴy Cᴀᴩᴛɪᴏɴ**")


from bot import Bot 

@Bot.on_message(filters.private & filters.command(['view_thumb', 'viewthumb']))
async def viewthumb(client, message):    
    thumb = await db.get_thumbnail(message.from_user.id)
    if thumb:
       await client.send_photo(chat_id=message.chat.id, photo=thumb)
    else:
        await message.reply_text("😔 **Yᴏᴜ Dᴏɴ'ᴛ Hᴀᴠᴇ Aɴy Tʜᴜᴍʙɴᴀɪʟ**")
		
from bot import Bot 

@Bot.on_message(filters.private & filters.command(['del_thumb', 'delthumb']))
async def removethumb(client, message):
    await db.set_thumbnail(message.from_user.id, file_id=None)
    await message.reply_text("❌️ **Tʜᴜᴍʙɴᴀɪʟ Dᴇʟᴇᴛᴇᴅ**")
	
from bot import Bot 

@Bot.on_message(filters.private & filters.photo)
async def addthumbs(client, message):
    mkn = await message.reply_text("Please Wait ...")
    await db.set_thumbnail(message.from_user.id, file_id=message.photo.file_id)                
    await mkn.edit("✅️ **Tʜᴜᴍʙɴᴀɪʟ Sᴀᴠᴇᴅ**")


