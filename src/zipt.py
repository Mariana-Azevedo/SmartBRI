import os
import string
from collections import defaultdict
from nltk.corpus import stopwords
import nltk

# Função para obter todos os arquivos .txt
def get_txt_files(base_dir):
    txt_files = []
    for root, dirs, files in os.walk(base_dir):  # Percorre os diretórios
        for file in files:
            if file.endswith(".txt"):  # Seleciona apenas os arquivos .txt
                txt_files.append(os.path.join(root, file))
    return txt_files


def process_files_with_map(files):
    word_map = defaultdict(int)
    total_files = len(files)  # Verificar número de arquivos processados
    total_words = 0  # Contar palavras processadas

    for file_path in files:
        with open(file_path, "r", encoding="utf-8") as file:
            content = file.read()
            content = content.translate(str.maketrans('', '', string.punctuation)).lower()
            words = content.split()
            total_words += len(words)  # Atualiza o total de palavras processadas

            for word in words:
                word_map[word] += 1

    print(f"Total de arquivos processados: {total_files}")
    print(f"Total de palavras processadas: {total_words}")
    return word_map
                   
                   
# Função para processar os arquivos e calcular o vocabulário
# def process_files_with_map(files):
#     word_map = defaultdict(int)

#     for file_path in files:
#         with open(file_path, "r", encoding="utf-8") as file:
#             content = file.read()
#             content = content.translate(str.maketrans('', '', string.punctuation)).lower()
#             words = content.split()
#             for word in words:
#                 word_map[word] += 1

#     return word_map

# Caminho base para os arquivos
base_directory = "document"
txt_files = get_txt_files(base_directory)

# Processar os arquivos encontrados
word_map = process_files_with_map(txt_files)

# Responder perguntas
vocabulary_size = len(word_map)
total_words = sum(word_map.values())

top_10_frequent = sorted(word_map.items(), key=lambda x: x[1], reverse=True)[:10]
least_10_frequent = sorted(word_map.items(), key=lambda x: x[1])[:10]

nltk.download('stopwords')
english_stopwords = set(stopwords.words('english'))
stopwords_freq = {word: freq for word, freq in word_map.items() if word in english_stopwords}

top_10_stopwords = sorted(stopwords_freq.items(), key=lambda x: x[1], reverse=True)[:10]
least_10_stopwords = sorted(stopwords_freq.items(), key=lambda x: x[1])[:10]

# Exibindo resultados
print(f"Tamanho do vocabulário: {vocabulary_size}")
print(f"Total de palavras na coleção: {total_words}")
print("As 10 palavras mais frequentes e suas frequências:", top_10_frequent)
print("As 10 palavras menos frequentes e suas frequências:", least_10_frequent)
print("As 10 stopwords mais frequentes:", top_10_stopwords)
print("As 10 stopwords menos frequentes:", least_10_stopwords)
