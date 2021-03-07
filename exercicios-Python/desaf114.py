import urllib
import urllib.request
s = 'http://pudim.com.br'
try:
    site = urllib.request.urlopen(s)
except:
    print('O Site {} não está acessivel no momento, volte mais tarde!'.format(s))
else:
    print('Tudo OK! Consegui acessar o Site', s)
    print(site.read())