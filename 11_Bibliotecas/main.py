import requests

resposta = requests.get("https://api.github.com/users/torvalds")
dados = resposta.json()

print(dados["name"])
print(dados["public_repos"])
print(dados["followers"])

resposta = requests.get("https://api.github.com/users/AdrielC5")
dados = resposta.json()

print(dados["name"])
print(dados["public_repos"])
print(dados["followers"])