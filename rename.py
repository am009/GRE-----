
target_dir = r'C:\Users\warren\Music\GRE语音'
import os
for file in os.listdir(target_dir):
    num = file[:file.find('-')]
    rest = file[file.find('-'):]
    if len(num) == 3:
        continue
    else:
        num = '0'*(3-len(num)) +num
    # print(num)
    print(f"{file} --> {num}{rest}")
    os.rename(os.path.join(target_dir, file), os.path.join(target_dir, f'{num}{rest}'))
