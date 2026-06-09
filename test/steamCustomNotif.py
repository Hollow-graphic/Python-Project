import steam

class MyClient(steam.Client):
    async def on_ready(self):
        print(f"Bot connecté : {self.user}")
        recever = await self.fetch_user(int(account[3]))
        await recever.send("Bot démarré !")

account = open("account.txt", "r").read().splitlines()

client = MyClient()
client.run(account[0], account[1])