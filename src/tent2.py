import os
import string
from collections import defaultdict

def get_txt_files(base_dir):
    txt_files = []
    for root, dirs, files in os.walk(base_dir):  # Percorre os diretórios
        for file in files:
            if file.endswith(".txt"):  # Seleciona apenas os arquivos .txt
                txt_files.append(os.path.join(root, file))
    return txt_files

# Exemplo de uso
base_directory = "document/source-document"
txt_files = get_txt_files(base_directory)

print(f"Total de arquivos .txt encontrados: {len(txt_files)}")


def process_files(files):
    word_count = defaultdict(int)
    
    for file_path in files:
        with open(file_path, "r", encoding="utf-8") as file:
            content = file.read()
            # Pré-processamento: Remover pontuações e converter para minúsculas
            content = content.translate(str.maketrans('', '', string.punctuation)).lower()
            words = content.split()

            # Atualizar o contador de palavras
            for word in words:
                word_count[word] += 1

    return word_count

# Processar os arquivos .txt
word_count = process_files(txt_files)

# Resultados
# vocabulary_size = len(word_count)
# print("Tamanho do vocabulário:", vocabulary_size)
