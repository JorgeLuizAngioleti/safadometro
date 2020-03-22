"coding: utf-8"
# Importa os módulos App e FloatLaylout da biblioteca Kivy.
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
#from kivy import Config
#Config.set('graphics','multisamples', '0')
# Objeto que cria nossa interface (janela).
class Interface(FloatLayout):
      
      def calcular(self,status):

# Nossas variáveis irão receber os parâmetros
# do nosso arquivo kv.
# ids - Busca as id dos widgets do arquivo kv
# .text é o parâmetros que queremos do id que selecionamos
# estamos convertendo para inteiro (int()), uma vez que
# o valor recebido é sempre uma string (str()).
        dia = int(self.ids.dia.text)
        mes = int(self.ids.mes.text)
        ano = int(self.ids.ano.text)

# easter eggs
        if dia == 1 and mes == 1 and ano == 84:
          self.ids.lb1.text = '[b][size=40] 99% [/size][/b] [b][size=40][color=#0B1EF5] ANJO [/b][/size][/color]'
          self.ids.lb2.text = '[b][size=40] Mais aquele [color=#F60404] 1% [/color] ...[/size][/b] '

# Verifica o valor da variável recebida do arquivo kv e o tipo
#print(dia)
#print(type(dia))
        else:

# Realiza o somatório da variável mês.
             somatorio = sum(range(mes + 1))

# Calculo que será realizado e exibido nos Labels.
             safadeza = somatorio + (ano / 100) * (50 - dia)
             anjo = 100 - safadeza

# lb1 e lb2, na posição text recebe o texto e valor das variaveis.
# [b][color] - estão sendo utilizados para formatar o texto na hora de exibir
# para que funcione o parâmetro markup do arquivo kv deve estar True.
# Estou utilizando round para arredondar o valor final.
             self.ids.lb1.text = '[b][color=#0B1EF5] %d %% ANJO' % round(anjo)
             self.ids.lb2.text = '[b][color=#F60404] Mas aquele(s) %d %% é VAGABUNDO' % round(safadeza)

# Objeto que cria nosso aplicativo e exibe a interface
class SafadometroApp(App):
    def build(self):
        return Interface()

if __name__=='__main__':
     SafadometroApp().run()
