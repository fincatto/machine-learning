#eh gordinho? perninha curta? faz au au?
porco1 = [1, 1, 0]
porco2 = [1, 1, 0]
porco3 = [1, 1, 0]
cacho1 = [1, 1, 1]
cacho2 = [0, 1, 1]
cacho3 = [0, 1, 1]

#conjunto dos dados e treinamento (os 3 primeiros sao porcos)
dados1 = [porco1, porco2, porco3, cacho1, cacho2, cacho3]
marca1 = ['poico', 'poico', 'poico', 'cacho', 'cacho', 'cacho']

#este aqui eh qual?
miste1 = [1, 1, 1]
miste2 = [1, 0, 0]
teste1 = [miste1, miste2]

#toca o baile
from sklearn.naive_bayes import MultinomialNB
modelo = MultinomialNB()
modelo.fit(dados1, marca1)
print(modelo.predict(teste1))