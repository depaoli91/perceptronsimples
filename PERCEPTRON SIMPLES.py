
#ALGORITMO DE TREINAMENTO - PERCEPTRON SIMPLES
import numpy as np 
import pandas as pd
import time

#DADOS DE ENTRADA DA AMOSTRA DE TREINAMENTO
x1=np.array([[-1,-1,-1,-1],[0.1, 0.3, 0.6, 0.5],[0.4,0.7,0.9,0.7],[0.7,0.2,0.8,0.1]])

#DADOS DE SAÍDA PARA A AMOSTRA DE TREINAMENTO
d=np.array([[1, -1, -1, 1]])

#INICIALIZAÇÃO DOS PESOS
w2=np.array([0.5, 0.2, 0.3, 0.4])

#TAXA DE APRENDIZAGEM
ef=0.7

# INICIALIZAÇÃO DO NÚMERO DE ÉPOCAS E DO ERRO
ep=0

#INICIALIZAÇÃO DOS ERROS POR AMOSTRA
erro1=[1]; erro2=[1]
erro3=[1]; erro4=[1]

# LOOP DE APRENDIZAGEM

while (True):

      
 for i in range(0,4): # POR AMOSTRA DE TREINAMENTO

 #POTENCIAL DE ATIVAÇÃO POR AMOSTRA DE TREINAMENTO
    
     x2=x1[:,i]  # AMOSTRA CONTENDO OS ELEMENTOS SEQUENCIAIS EXEMPLO: I=0 X2=[-1,0.1,0.4,0.7]
     x3=x2[:,np.newaxis] #TRANSPOSIÇÃO DO VETOR
     u=np.dot(w2,x3) # POTENCIAL DE ATIVAÇÃO

 #FUNÇÃO SINAL - DEGRAU BIPOLAR
     
     if u < 0:
         y=1
     if u==0:
         y=0
     if u > 0:
         y=-1
       
     erro=d[0,i]-y   #ERRO
      
 # ATUALIZAÇÃO DO ERRO POR AMOSTRA
 
     if i==0:
         erro1.pop()
                 
         aux1=np.dot(ef,erro)
         x2=x1[:,i]
         aux2=np.dot(aux1,x2)
         w2=np.add(w2,-aux2)
         x3=x2[:,np.newaxis]
         u=np.dot(w2,x3)
 
         if u < 0:
             y=1
         if u==0:
             y=0
         if u > 0:
             y=-1
        
         erro=d[0,i]-y
         erro1.append(erro)

         ep=ep+1
         
         print("EPOCAS:",ep)
     if i==1:
         erro2.pop()
         
         aux1=np.dot(ef,erro)
         x2=x1[:,i]
         aux2=np.dot(aux1,x2)
         w2=np.add(w2,-aux2)
         x3=x2[:,np.newaxis]
         u=np.dot(w2,x3)
 
         if u < 0:
             y=1
         if u==0:
             y=0
         if u > 0:
             y=-1
        
         erro=d[0,i]-y
         erro2.append(erro)

         ep=ep+1
         
         print("EPOCAS:",ep)
     if i==2:
         erro3.pop()
         
         aux1=np.dot(ef,erro)
         x2=x1[:,i]
         aux2=np.dot(aux1,x2)
         w2=np.add(w2,-aux2)
         x3=x2[:,np.newaxis]
         u=np.dot(w2,x3)
 
         if u < 0:
             y=1
         if u==0:
             y=0
         if u > 0:
             y=-1
        
         erro=d[0,i]-y
         erro3.append(erro)

         ep=ep+1
         
         print("EPOCAS:",ep)
     if i==3:
         erro4.pop()
         
         aux1=np.dot(ef,erro)
         x2=x1[:,i]
         aux2=np.dot(aux1,x2)
         w2=np.add(w2,-aux2)
         x3=x2[:,np.newaxis]
         u=np.dot(w2,x3)
 
         if u < 0:
             y=1
         if u==0:
             y=0
         if u > 0:
             y=-1
        
         erro=d[0,i]-y
         erro4.append(erro)
         
         ep=ep+1
         
         print("EPOCAS:",ep)


     if(erro1==[0]): # CRITÉRIO DE SAÍDA
         if(erro2==[0]):
             if(erro3==[0]):
                 if(erro4==[0]):
                     break
  
   
     
     time.sleep(1)
     
 if(erro1==[0]): # CRITÉRIO DE SAÍDA
        if(erro2==[0]):
            if(erro3==[0]):
                if(erro4==[0]):
                    break
     
 
#ALGORITMO DE OPERAÇÃO - PERCEPTRON SIMPLES

# AMOSTRA A SER CLASSIFICADA

amostra=np.array([[-1,0.5,0.7,0.1]])
amostra=amostra.reshape(4,1)

# CALCULO DO POTENCIAL DE ATIVAÇÃO
 
u2=np.dot(w2,amostra)

# FUNÇÃO SINAL - DEGRAU BIPOLAR
    
if u2 < 0:
      y=1
if u2==0:
      y=0       
if u2 > 0:
     y=-1
     
# CLASSIFICAÇÃO FINAL DA AMOSTRA
        
if y==-1:
   print("AMOSTRA PERTENCE A CLASSE A")
if y==1:
  print("AMOSTRA PERTENCE A CLASSE B")

 
 
        



 
  
    
    
     
     
     
    
         
         
     
     
    
 
 


 
     
         
  
         
         
 
       
    
    