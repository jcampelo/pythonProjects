import urllib.request

content = urllib.request.urlopen("https://www.melhorcambio.com/dolar-hoje").read()
content = str(content)
find = '<input type="hidden" value="'
posicao = int(content.index(find) +len(find))
dolar = content[posicao:posicao + 4]


print (" O valor do dólar hoje é: " + dolar)