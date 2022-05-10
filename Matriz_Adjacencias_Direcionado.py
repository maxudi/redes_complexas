# -*- coding: utf-8 -*-
"""
Created on Tue May 10 15:26:47 2022

@author: MAXIMIANO EDUARDO PEREIRA
"""

class Grafo:
    
    def __init__(self, vertices):
        self.vertices = vertices
        self.grafo = [[0]*self.vertices for i in range(self.vertices)]
        
    def adiciona_aresta(self, u, v):
        #Para gravos direcionados simples
        self.grafo[u-1][v-1] = 1    #trocar "=" por "+=" se for grafo múltiplo
        
       # self.grafo[v-1][u-1] = 1   (Caso o grafo não seja direcionado)
    
    def mostra_matriz(self):
        print('A matriz de adjacências é: ')
        for i in range(self.vertices):
            print(self.grafo[i])
    
    def conta_vertices(self):
        print('A Matriz possui grau: ')
        for i in range(self.vertices):
            print(self.vertices)
            
g = Grafo(4)    #cria grafo com n vértices nesse caso 4
#g.mostra_matriz() #mostra matriz de adjacências neste caso uma matriz 4x4 com zeros

g.adiciona_aresta(1,2)
g.adiciona_aresta(2,3)
g.adiciona_aresta(2,4)
#g.adiciona_aresta(5,6)
#g.adiciona_aresta(1,7)

g.mostra_matriz()
g.mostra_vertices()




