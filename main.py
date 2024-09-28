from configparser import ConfigParser
import requests
cfg = ConfigParser()

#text = requests.get('https://raw.githubusercontent.com/TheRayGent/project-localization/refs/heads/main/localization/citadel_gc/citadel_gc_russian.txt').text

a = 'D:\\SteamLibrary\\steamapps\\common\\Deadlock'

config_text=requests.get('https://raw.githubusercontent.com/TheRayGent/project-localization/refs/heads/main/config.cfg').text



cfg.read_string(config_text)

for i in cfg.items('EditFiles'):
    c =i[1]
    b = f'{a}{requests.get(f'https://raw.githubusercontent.com/TheRayGent/project-localization/refs/heads/main{c}')}'
    print(c)



'''with open('ChromeCacheView.cfg', 'w') as config_file:
    cfg.write(config_file)
txt = open('citadel_gc_russian.txt', encoding='utf_8_sig', mode='w')
txt.write(a)'''