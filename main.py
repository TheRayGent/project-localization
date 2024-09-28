from configparser import ConfigParser
cfg = ConfigParser()
import requests
response = requests.get('https://raw.githubusercontent.com/TheRayGent/project-localization/refs/heads/main/localization/citadel_gc/citadel_gc_russian.txt')

print(response.text)