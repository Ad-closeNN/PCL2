with open('Plain Craft Launcher 2/Application.xaml', 'r', encoding='utf-8') as file:
    lines = file.readlines()

with open("font", 'r', encoding='utf-8') as font:
    font = font.read().replace('\n', '')

for i in range(len(lines)):
    if '<Setter Property="FontFamily" Value="' in lines[i]:
        lines[i] = lines[i].replace('Resources/#PCL English, Microsoft YaHei UI', f'{font}, Resources/#PCL English, Microsoft YaHei UI')

with open('Plain Craft Launcher 2/Application.xaml', 'w', encoding='utf-8') as file:
    file.writelines(lines)
