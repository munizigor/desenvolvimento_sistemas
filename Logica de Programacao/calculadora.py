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
class Calculadora:
  def __init__(self, master=None):
    #Criação de 3 frames: Um para o histórico da operação, um onde aparecerá os dígitos e outro para os botões
    self.frame_hist = Frame(raiz)
    self.frame_vetor = Frame(raiz)
    self.frame_botoes = Frame(raiz)
    #Vetor para ir acrescentando os números digitdos
    self.vetor = list()
    self.valor_hist = StringVar()
    self.valor_texto = StringVar()
    #self.valor_texto.set = self.vetor
    self.label_hist = Label(self.frame_hist, textvariable = self.valor_hist, font=("Arial Black", "12"),
                  width=23, height=1, anchor="e")
    self.label_hist.grid(row=0, )
    self.label_texto = Label(self.frame_vetor, textvariable = self.valor_texto, font=("Arial Black", "20"),
                  width=23, height=2, borderwidth=2, relief="groove")
    self.label_texto.grid(row=0)
    self.inserir_botoes()
    self.frame_hist.pack()
    self.frame_vetor.pack()
    self.frame_botoes.pack()
  #Criar botões
  def inserir_botoes(self):
    #Função padrão para criar botoes
    def criar_botao(self, nome, texto, linha, coluna, comando, bg="black",fg="white"):
      var_name = 'self.botao_' + str(nome)
      exec("""{} = Button(self.frame_botoes, text=\"{}\", width=10, 
              height=4, font=(\"Calibri\", \"15\"), bg=\"{}\",
              fg=\"{}\", command = {})""".format(var_name,texto,bg,fg,comando))
      exec("{}.grid(row={},column={})".format(var_name,int(linha),int(coluna)))
    #criando botoes de digitos
    for i in range (0,10):
      criar_botao(self,i, i, (4-((i-1)//3) if i !=0 else 5), (i-1)%3 if i !=0 else 1,"partial(self.preenche_tela,"+str(i)+")")
    #Criando demais botões
    criar_botao(self,"mais_menos","+/-",5,0,"self.mais_menos")
    criar_botao(self,"virgula",",",5,2,"partial(self.preenche_tela,',')")
    criar_botao(self,"divisao","÷",1,3,"partial(self.preenche_tela,'/')",bg="gray24")
    criar_botao(self,"multiplicacao","X",2,3,"partial(self.preenche_tela,'*')",bg="gray24")
    criar_botao(self,"subtracao","-",3,3,"partial(self.preenche_tela,'-')",bg="gray24")
    criar_botao(self,"soma","+",4,3,"partial(self.preenche_tela,'+')",bg="gray24")
    criar_botao(self,"igual","=",5,3,"partial(self.preenche_tela,'=')",bg="blue")
    criar_botao(self,"memoria_mais","M+",1,0,"self.memory_add",bg="gray24")
    criar_botao(self,"memoria_menos","M-",1,1,"self.memory_add",bg="gray24")
    criar_botao(self,"memoria_armazena","MS",1,2,"self.memoria_armazena",bg="gray24")

  def mostra_valor(self):
    self.tela = ''.join(map(str, self.vetor)) 
    self.valor_texto.set(self.tela)
  
  def preenche_tela(self,valor):
    if (valor == ",") and ("," in self.vetor): 
      pass
    elif valor in ["+","-","*","/","="]:
      temp_hist = self.valor_hist.get().replace(',','.')
      temp_valor_vetor = self.valor_texto.get().replace(',','.')
      if temp_hist == "":
        self.valor_hist.set(self.tela+valor)
        self.valor_texto.set("")
        self.vetor.clear()
      else:
        try:
          calculo = eval("{}{}".format(temp_hist,temp_valor_vetor))
        except ZeroDivisionError:   
          calculo = "Impossível dividir por zero"
        #print(calculo)
        self.valor_texto.set(str(calculo).replace('.',','))
        if valor == "=":
          self.valor_hist.set("")
          #self.valor_texto.set(self.tela)
        else:
          self.valor_hist.set(self.tela+valor)
        self.vetor.clear()
    else:
      self.vetor.append(valor)
      self.mostra_valor()

  def mais_menos(self):
    if self.vetor[0]=="-":
      self.vetor.pop(0)
    else:
      self.vetor.insert(0,"-")
    self.mostra_valor()

  def fazer_operacao(self,operacao):
    self.valor_hist[0] = float(self.tela.replace(',','.'))
    self.valor_texto.set("")

  
  def soma(self):
    #Receber valor de self.vetor
    #deixar preencher tela
    #igual, soma, divide e multiplica = soma anterior
    pass

  def multiplicacao(self):
    #Receber valor de self.vetor
    #deixar preencher tela
    #igual, soma, divide e multiplica = multiplicacao anterior
    pass

  def divisao(self):
    pass

  def subtracao(self):
    pass
  def memory_add(self):
    print(float(self.tela.replace(',','.')))

  def memory_subtract(self):
    pass
  def memoria_armazena(self):
    self.store = float(self.tela.replace(',','.'))
    print(self.store)

raiz = Tk()
raiz.title("Calculadora 0.1 - Igor Muniz")
Calculadora(raiz)
raiz.mainloop()