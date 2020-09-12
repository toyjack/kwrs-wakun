import re

with open('./data.txt', encoding='utf-8') as f:
    lines = f.readlines()

def reComp(added):
    if added==[]:
        return '［和名(.)］'
    else:
        return '［和名(.)['+''.join(added)+']］'

r = ['乃', '太', '為', '世', '奴', '衣', '由', '須', '夜', '呂', '比', '紀', '勢','木', '子', '爾', '之', '布', '知', '恵','利', '万', '々', '毛']
p = re.compile('［和名['+''.join(r)+'](.)］')
keys = []

for line in lines:
    m = p.search(line)
    if m:
        keys.append(m.group(1))

keys = list(set(keys))
added = list((set(r)|set(keys))-set(r))

print('Results:', ''.join(keys))
print('results:',keys)
print('Added:',''.join(added))
print('Added', added)

