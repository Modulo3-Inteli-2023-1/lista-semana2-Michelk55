#  Se achar necessario, faça import de outras bibliotecas





# Crie a função que será avaliada no exercício aqui

def is_anagram(str1, str2):
    # Removendo espaços em branco e convertendo para letras minúsculas para normalizar as strings
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()
    
    # Verificando se as strings têm o mesmo comprimento após a remoção de espaços
    if len(str1) != len(str2):
        return False
    
    # Usando dicionários para contar a ocorrência de cada letra nas duas strings
    count_dict1 = {}
    count_dict2 = {}
    
    for char in str1:
        count_dict1[char] = count_dict1.get(char, 0) + 1
        
    for char in str2:
        count_dict2[char] = count_dict2.get(char, 0) + 1
        
    # Verificando se os dicionários de contagem são iguais
    return count_dict1 == count_dict2

# Exemplos de uso
print(is_anagram("Amor", "Roma"))  # True
print(is_anagram("Pedra", "Padre"))  # True
print(is_anagram("Perda", "Pedra"))  # True
print(is_anagram("Hello", "World"))  # False





# Teste a sua função aqui (caso ache necessário)



