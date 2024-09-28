from configparser import ConfigParser
import requests
cfg = ConfigParser()

#text = requests.get('https://raw.githubusercontent.com/TheRayGent/project-localization/refs/heads/main/localization/citadel_gc/citadel_gc_russian.txt').text

a = 'D:\\SteamLibrary\\steamapps\\common\\Deadlock'

config_text=requests.get('https://raw.githubusercontent.com/TheRayGent/project-localization/refs/heads/main/config.cfg').text



cfg.read_string(config_text)

for i in cfg.items('EditFiles'):
    b = a+i[1]
    c = requests.get('https://raw.githubusercontent.com/TheRayGent/project-localization/refs/heads/main'+i[1]).text
    print(open(b))



'''with open('ChromeCacheView.cfg', 'w') as config_file:
    cfg.write(config_file)
txt = open('citadel_gc_russian.txt', encoding='utf_8_sig', mode='w')
txt.write(a)'''