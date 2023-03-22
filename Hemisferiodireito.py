print("Olá,bem-vindo(a) ao cérebro:hemisfério direito") 
print("Vamos começar,as seguinte variáveis irão ser demonstradas,pressione ''Enter'':")      
input(">Arte,3D e criatividade: ")

if input :"Arte"
print(">Os neurocientistas afirmam que a arte provoca alterações nos padrões das ondas e do ritmo cerebral, bem como estimula o nosso sistema límbico, provocando emoções. Por meio da arte, o indivíduo pode experienciar o mundo de uma maneira diferente,por exemplo->Poema:É sempre mais difícil ancorar um navio no espaço''-(Ana Cristina César)")

if input:"3d"
print(">Como enxergarmos em três dimensões?: Uma das etapas fundamentais para que você enxergue em 3D, está na retina,É nessa parte do olho que enxergamos a luz. Nela existem células especiais (fotorreceptoras) que traduzem os componentes dessa luz, e ajudam na formação da imagem. É possível distinguir bordas, a intensidade do que estamos vendo e as cores, que permitem que você enxergue formas e contrastes.Esses pontos são fundamentais para que você consiga criar a percepção 3D do que está perto,Como por exemplo:um cubo:🧊")
if input:"criatividade"
from random import choice
import string
print("o pensamento criativo ocorre sobretudo no interior de três redes neurais.São elas: 1)a rede de modo padrão, usada quando o cérebro está gerando ideias e simplesmente imaginando; 2)a rede de controle executivo, ativada para a tomada de decisões e avaliações de ideias; e 3)rede de saliência, usada para discernir quais ideias são relevantes e para facilitar a transição das ideias entre os modos padrão e executivo.Essa última rede tem uma função-chave, ao fazer uma ponte entre o mecanismo de geração de ideias(muitas pré-existentes) e o de avaliação destas.Por exemplo,criação de um nova palavra,o programa simulará as redes cerebrais:")
tamanho = input("Qual será o tamanho da sua nova palavra?(quantos digitos?): ")
tamanho = int(tamanho)
valores = string.ascii_letters 
palavra = ''
for i in range(tamanho):
    palavra += choice(valores)

print("Aqui está a sua nova palavra!: " + palavra)
