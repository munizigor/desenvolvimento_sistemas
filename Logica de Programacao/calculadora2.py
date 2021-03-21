'''
CURSO: Superior de Tecnologia em Análise e Desenvolvimento de Sistemas
MATÉRIA: Algoritmos e Lógica de Programação
NOME: Igor Muniz da Silva
RA: 72100176
Atividade: Criar umprograma em Python, que simula o uso de uma calculadora com as operações básicas  
(+ - /  *)  e  uso  da memória  da  calculadora  (MS armazenamento  do resultado,  M+  adição  do  
valor  armazenado  à  operação  e  M-subtração  do  valor armazenado à operação), sendo que é sugerido 
fortemente o uso de vetores/arrays para manipulação das operações e valores numéricos.
•  Programação Python: 80 % da nota (Será verificado se o aluno abordou todos itens propostos no 
trabalho);
•Interface: 20  %  da  nota  (Será  verificado  se  o  aluno abordou  questões  básicas  de interface 
e design do usuário (UX –User Experience)
'''
#Importação de bibliotecas
from tkinter import *
from functools import partial

#Criação da classe Calculadora
raiz = Tk()
raiz.title("Calculadora 0.1 - Igor Muniz")
frame_cima = Frame(raiz)
frame_baixo = Frame(raiz)
vetor = list()
var = StringVar()
#var.set = vetor
l = Label(frame_cima, textvariable = var, font=("Arial Black", "20"),
width=23, height=2, borderwidth=2, relief="groove")
l.grid(row=0)
#Criar botões
def inserir_botoes():
    #Função padrão para criar botoes
    def criar_botao(nome, texto, linha, coluna, comando, bg="black",fg="white"):
        var_name = 'botao_' + str(nome)
        exec("""{} = Button(frame_baixo, text=\"{}\", width=10, 
                height=4, font=(\"Calibri\", \"15\"), bg=\"{}\",
                fg=\"{}\", command = {})""".format(var_name,texto,bg,fg,comando))
        exec("{}.grid(row={},column={})".format(var_name,int(linha),int(coluna)))
    #criando botoes de digitos
    for i in range (0,10):
        criar_botao(i, i, (4-((i-1)//3) if i !=0 else 5), (i-1)%3 if i !=0 else 1,"partial(teste,"+str(i)+")")
    #Criando demais botões
    criar_botao("mais_menos","+/-",5,0,"memory_add('c')")
    criar_botao("virgula",",",5,2,"memory_add('c')")
    criar_botao("divide","÷",1,3,"memory_add('c')",bg="gray24")
    criar_botao("multiplica","X",2,3,"memory_add('c')",bg="gray24")
    criar_botao("diminui","-",3,3,"memory_add('c')",bg="gray24")
    criar_botao("soma","+",4,3,"memory_add('c')",bg="gray24")
    criar_botao("igual","=",5,3,"memory_add('c')",bg="gray24")
    criar_botao("memoria_mais","M+",1,0,"memory_add('c')",bg="gray24")
    criar_botao("memoria_menos","M-",1,1,"memory_add('c')",bg="gray24")
    criar_botao("memoria_armazena","MS",1,2,"memory_add('c')",bg="gray24")

def teste(valor):
    vetor.append(valor)
    print(vetor)
    tela = ''.join(map(str, vetor)) 
    var.set(tela)

def memory_add(c):
    print("ADD")

def memory_subtract():
    pass

inserir_botoes()
frame_cima.pack()
frame_baixo.pack()

#Calculadora(raiz)
raiz.mainloop()