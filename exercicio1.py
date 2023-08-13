#  Se achar necessario, faça import de outras bibliotecas





# Crie a função que será avaliada no exercício aqui

def conta_palavras_unicas(frase):
    # Convertendo todas as letras para minúsculas para considerar palavras iguais independentemente de caixa
    frase = frase.lower()
    
    # Dividindo a frase em palavras usando espaço como separador
    palavras = frase.split()
    
    # Usando um conjunto para armazenar palavras únicas
    palavras_unicas = set(palavras)
    
    # Retornando a quantidade de palavras únicas
    return len(palavras_unicas)

# Exemplo de uso
frase_exemplo = "Esta é uma frase de exemplo. Uma frase curta para testar a função."
quantidade_palavras_unicas = conta_palavras_unicas(frase_exemplo)
print("Quantidade de palavras únicas:", quantidade_palavras_unicas)



# Teste a sua função aqui (caso ache necessário)

