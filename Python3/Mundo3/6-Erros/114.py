import urllib.request

try:
    site = urllib.request.urlopen("http://www.pudim.com.br/")
except:
    print("Conexão indisponível")
else:
    print("Conexão disponível")
