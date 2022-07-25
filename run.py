import os ; from settings import Settings

variables = list(vars(Settings).items())
for var in variables:
    if var[1] == '':
        print('One or more of the settings are not filled in')
        exit()

os.system('python send.py & python recieve.py')