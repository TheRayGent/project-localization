txt = open('citadel_gc_russian.txt', encoding='utf_8_sig')
a = ''
for i in txt.readlines():
    if 'Upgrades: Weapon' in i:
        a+='''        }
}'''
        break
    a+=i
txt = open('citadel_gc_russian.txt', encoding='utf_8_sig', mode='w')
txt.write(a)