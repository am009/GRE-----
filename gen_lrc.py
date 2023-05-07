from pylrc.classes import Lyrics, LyricLine


gres = []
with open('gre长难句.txt', 'r') as f:
    gres = f.readlines()

def write_lrc(path, text):
    lrc = Lyrics([LyricLine("[00:00]", text), LyricLine("[59:00]")])
    with open(path, 'w') as f:
        f.write(lrc.toLRC())

target_dir = r'C:\Users\warren\Music\GRE语音'
import os
for file in os.listdir(target_dir):
    if not file.endswith('.mp3'): continue
    num = int(file[:file.find('-')])
    path = os.path.join(target_dir, file).removesuffix('.mp3')+'.lrc'
    write_lrc(path, gres[num-1])
