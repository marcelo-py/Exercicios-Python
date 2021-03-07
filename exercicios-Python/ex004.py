import emoji
from playsound import playsound
msg = emoji.emojize('\033[7;35mOlá, Mundo!:alien:\033[m',use_aliases=True)
print (msg)
print('~='*20)
print(emoji.emojize('\033[34mTocando agora...\033[m:notes: O Teatro Mágico - Soprano',use_aliases=True))
playsound('otm-soprano.mp3')
