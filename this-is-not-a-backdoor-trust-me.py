from os import system
folder = str(input('[*] Folder to save profiles, or <enter> for current: '))
if folder == '':
    system('netsh wlan export profile folder=. key=clear')
else:
    command = "netsh wlan export profile folder="+folder+" key=clear"
    system(command)
