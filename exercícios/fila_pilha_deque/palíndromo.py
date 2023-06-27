# Implemente uma função que, usando deque, indique se um string é um palíndromo ou não.
from packages.deque.deque import Deque
import re
from unidecode import unidecode

deque = Deque()

palindromo_candidato = input().lower().replace(" ", "")
palindromo_candidato_acentuacao = unidecode(palindromo_candidato)
palindromo_candidato_pontuacao = re.sub(r'[^\w\s]', '', palindromo_candidato_acentuacao)


for i in palindromo_candidato_pontuacao:
    deque.push_back(i)

deque2 = deque.reverse()
print(deque2)

if deque == deque2:
    print("Sao iguais")
else:
    print("Não sao iguais")