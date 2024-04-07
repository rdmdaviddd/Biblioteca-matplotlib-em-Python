import matplotlib.pyplot as plt
anos = [1950, 1960, 1970, 1980, 1990]
investimento = [20, 30, 10, 75, 100]
plt.bar(range(len(anos)), investimento)
plt.title("Investimento em Tecnologia") #criando título do gráfico
plt.ylabel("Milhões de R$") #rótulo ao eixo y
plt.xlabel("Década") #rótulo ao eixo x
plt.xticks(range(len(anos)), anos)#rotulo do eixo x informando as decadas no centro das barras do gráfico
plt.show() #exibir gráfico