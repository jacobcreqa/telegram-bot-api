# telegram-bot-api
Research and Initialize to use telegram-bot-api with python

1. Create a group on TeleGram
2. Search @BotFather
3. Create a new bot with command `\newbot` 
4. Choose name and username for your bot then you should see the token to access the HTTP API
5. Add the bot to the group
6. Type command: `\start`
7. Open this link to get group chat Id: `https://api.telegram.org/bot<TOKEN>/getUpdates`

You should see the informatin with json format

```
{
    "ok": true,
    "result": [
        {
            "update_id": 635936688,
            "message": {
                "message_id": 5,
                "from": {
                    "id": 5972474843,
                    "is_bot": false,
                    "first_name": "Jacob",
                    "last_name": "Vu",
                    "username": "jacobvu84"
                },
                "chat": {
                    "id": -4154348388, // GROUP_CHAT_ID
                    "title": "telegram bot api",
                    "type": "group",
                    "all_members_are_administrators": true
                },
                "date": 1710491398,
                "text": "/start",
                "entities": [
                    {
                        "offset": 0,
                        "length": 6,
                        "type": "bot_command"
                    }
                ]
            }
        }
    ]
}
```
8. Setup the sytem enviroment variables for `GROUP_CHAT_ID` and `TELEBOT_BOT_TOKEN`
9. Execute the `showTokenAndGroupId.py`
10. Swith to the group on the telegram and type:
--  `\token`: You should see the token value
-- `group_id`: You should see the group Id value
