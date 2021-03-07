from desaf115.lib.interface import *
from desaf115.lib.arquivo import *

arq = 'pessoascadastradas.txt'
if not arquivoExiste(arq):
    criarArquivo(arq)

while True:
    opc = menu(['Ver Pessoas Cadastradas', 'Cadastrar nova Pessoa', 'Sair do Sistema'])
    op = opções('Sua opção')
    if op == 1:
        lerArquivo(arq)
    if op == 2:
        nome = str(input('Nome: '))
        idade = leiaInt('Idade')
        cadastrarPessoa(arq, nome, idade)
    if op == 3:
        break