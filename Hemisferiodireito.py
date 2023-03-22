print("Olá,bem-vindo(a) ao cérebro:hemisfério direito") 
print("Vamos começar,as seguinte variáveis irão ser trabalhadas:")      
input(">Arte,3D e criatividade: ")

if input :"Arte"
print("Poema:É sempre mais difícil ancorar um navio no espaço''-(Ana Cristina César)")

if input:"3d"
print("Exemplo de um cubo=🧊")

if input:"criatividade"
from random import choice
import string
print("Hora das ideias! ")
tamanho = input("Qual será o tamanho da sua nova palavra?: ")
tamanho = int(tamanho)
valores = string.ascii_letters + string.digits
palavra = ''
for i in range(tamanho):
    palavra += choice(valores)

print("Aqui está a sua nova palavra!: " + palavra)
