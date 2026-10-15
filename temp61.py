import zlib

str_object1 = open('C:/Users/Adam/Desktop/Shortcut/Game/Archipelago/output/AP_61094742389519305888.archipelago', 'rb').read()
str_object2 = zlib.decompress(str_object1)
f = open('C:/Users/Adam/Desktop/Shortcut/Game/Archipelago/output/AP_61094742389519305888.data', 'wb')
f.write(str_object2)
f.close()
