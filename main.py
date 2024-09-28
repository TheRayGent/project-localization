from configparser import ConfigParser
import requests
cfg = ConfigParser()

#a = 'D:\\SteamLibrary\\steamapps\\common\\Deadlock'
a = input('Введите путь до папки игры\n(Пример: D:/SteamLibrary/steamapps/common/Deadlock)\n').strip()
if a[-2:-1]=='\\' or a[-2:-1]=='/':
    a += 'game/citadel/resource'
else: a += '/game/citadel/resource'
config_text=requests.get('https://raw.githubusercontent.com/TheRayGent/project-localization/refs/heads/main/config.cfg').text



cfg.read_string(config_text)

for i in cfg.items('EditFiles'):
    b = a+i[1]
    c = requests.get('https://raw.githubusercontent.com/TheRayGent/project-localization/refs/heads/main'+i[1]).text
    print(b,end='')
    txt = open(a+i[1], encoding='utf_8_sig', mode='w')
    txt.write(c)
    txt = open(a+i[1], encoding='utf_8_sig')
    c1=''
    for j in txt.readlines():
        if '\ufeff' in j: c1+=j.replace('\ufeff','')
        else: c1+=j
    txt = open(a+i[1], encoding='utf_8_sig', mode='w')
    txt.write(c1)
    print(' - успешно')
print('Кастомный перевод установлен успешно!')
input()
