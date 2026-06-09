


def message_manager(username, message, config, obs_client, pygame):
    username = username[1:]
    global current_game
    
    if len(message) >= 94:
        print("!message to long")
        return
    if username == "HollowetNini" and message.startswith("!game"):
        current_game = message[6:]
        print(f'game changed to {current_game}')
        return
    if message.startswith("!color"):
        color = message[6:]
        if " " not in message:
            message = f"{message}, {message}"
        if not "," in color:
            color = color.replace(" ", ", ")
        if not config.has_section(username):
            config.add_section(username)
        config[username]["color"] = color
        with open("config.ini", "w") as f:
            config.write(f)
        return
    if message.lower() in list:
        print(f"play sound: {message.lower()}.mp3")
        pygame.mixer.music.load(os.path.join(sound_dir, message.lower()+".mp3"))
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            time.sleep(0.1)
        return
    if current_game == "vivid":
        if   message.lower() in ["left",    "gauche"]:
            file_write(vivid_file, "UnknownEnum.Value_11")
            return
        elif message.lower() in ["right",   "droite"]:
            file_write(vivid_file, "UnknownEnum.Value_12")
            return
        elif message.lower() in ["up",      "haut"]:
            file_write(vivid_file, "UnknownEnum.Value_13")
            return
        elif message.lower() in ["down",    "bas"]:
            file_write(vivid_file, "UnknownEnum.Value_14")
            return
        elif message.lower() in ["confirm", "confirmer"]:
            file_write(vivid_file, "UnknownEnum.Value_4")
            return
        elif message.lower() in ["cancel",  "retour"]:
            file_write(vivid_file, "UnknownEnum.Value_5")
            return
        elif message.lower() in ["hold", "maintenir"]:
            file_write(vivid_file, "Hold")
            return
    
    color = config.get(username, "color", fallback=None)
    if not color:
        color = f"{random_color()}, {random_color()}"
        
    character = username
    file = r".\web\custom_character\assets\sp_u_" + username.lower() + ".png"
    if not os.path.exists(file):
        character = str(randint(0,5))

    obs_hide(obs_client, "_VividChat", 1, True)
    obs_hide(obs_client, "_VividChat", 2, True)

    file_write(live_username, username)
    file_write(live_message, message)
    file_write(live_color, color)
    file_write(live_character, character)
    
    obs_refresh_web(obs_client, "textbox")
    obs_refresh_web(obs_client, "character")
    
    engine = pyttsx3.init()
    engine.setProperty("volume", 1.0) # volume (0.0 à 1.0)
    engine.say(message)
    engine.runAndWait()
    
    time.sleep(5)
    obs_hide(obs_client, "_VividChat", 1, False)
    obs_hide(obs_client, "_VividChat", 2, False)