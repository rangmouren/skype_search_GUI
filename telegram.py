from telethon import TelegramClient

# Use your own values from my.telegram.org
api_id = 1395839731
api_hash = 'AAFWbk2gFHIiKJr3R2oZoJJ9T2TRUkzRvbo'
client = TelegramClient('anon', api_id, api_hash)
async def main():
    # Getting information about yourself
    me = await client.get_me()

    # "me" is a user object. You can pretty-print
    # any Telegram object with the "stringify" method:
    print(me.stringify())
    # username = me.username
    # print(username)
    # print(me.phone)

main()