from configparser import ConfigParser
import requests
cfg = ConfigParser()

#text = requests.get('https://raw.githubusercontent.com/TheRayGent/project-localization/refs/heads/main/localization/citadel_gc/citadel_gc_russian.txt').text



config_text=requests.get('https://raw.githubusercontent.com/TheRayGent/project-localization/refs/heads/main/config.cfg').text



cfg.read_string(config_text)
print(cfg.items('EditFiles'))
