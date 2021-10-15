# Conceitos-Iniciais-Open-Cv
Conceitos iniciais sobre a biblioteca OpenCv utilizando a linguagem python.


##Armazenar uma imagem numa variável

img=cv.imread('Nome da foto . jpg ou png')

##Qual o motivo da foto estar com um aspecto azulado?
https://learnopencv.com/why-does-opencv-use-bgr-color-format/ 

##Arestas

O segmento de reta que liga dois vértices 

Os contornos se baseiam nas arestas( uso da biblioteca cv.Canny)

.cv.Canny (Imagem , 125,175)

##Frequência da Imagem :

.Atualização de quadros por segundos 

60Hz => No período de um segundo acontece uma atualização de 60 quadros
Números de oscilação da onda em um segundo

##Convolução de Imagem

Convolução é o processo de calcular a intensidade de um determinado pixel em função da intensidade de seus vizinhos. 

Convolução : Àrea de de ánalise e processamento

##Alteração da cor para RGB

Por padrão a imagem ao ser manipulada no openCv vem definida em BGR , o que gera em alguns usuários frustração, ao carregar uma imagem e ela estar com um aspecto azulado. Para gerar essa correção é necessário atualizar para o padrao RGB.

(uso da biblioteca cv.COLOR_BGR2RGB)


##Imagem com Blur ( Borragem)

Borragem de uma fotografia , recurso utilizado em alguns casos para borrar o rosto de alguns usuários quando há detecção facial.
(uso da biblioteca .cv.GaussianBlur(Imagem, (5,5), cv.BORDER_DEFAULT))
