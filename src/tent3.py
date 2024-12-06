import os
import string
from collections import defaultdict

# Função para obter todos os arquivos .txt
def get_txt_files(base_dir):
    """
    Encontra todos os arquivos .txt em um diretório base
    """
    txt_files = []
    for root, dirs, files in os.walk(base_dir):  # Percorre os diretórios
        for file in files:
            if file.endswith(".txt"):  # Seleciona apenas os arquivos .txt
                txt_files.append(os.path.join(root, file))
    return txt_files

# Função para carregar o conteúdo de um arquivo específico
def load_file_content(file_path):
    """
    Carrega o conteúdo de um arquivo específico
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        return content
    except FileNotFoundError:
        print(f"Arquivo {file_path} não encontrado!")
        return None

# Função para processar o vocabulário usando map
def process_files_with_map(files):
    """
    Processa os arquivos e calcula o vocabulário (palavras únicas)
    """
    word_map = defaultdict(int)  # Dicionário para armazenar palavras e suas contagens

    def process_content(content):
        """
        Processa o conteúdo do arquivo, limpa e atualiza o map
        """
        content = content.translate(str.maketrans('', '', string.punctuation)).lower()
        words = content.split()
        for word in words:
            word_map[word] += 1

    # Usando map para processar os conteúdos dos arquivos
    file_contents = map(load_file_content, files)
    list(map(process_content, filter(None, file_contents)))  # Processa cada conteúdo não vazio

    return word_map, len(word_map)  # Retorna o dicionário de palavras e o tamanho do vocabulário

# Exemplo de uso
base_directory = "document/source-document"  # Substitua pelo caminho da sua pasta principal
txt_files = get_txt_files(base_directory)

print(f"Total de arquivos .txt encontrados: {len(txt_files)}")

# Processar os arquivos encontrados
word_map, vocabulary_size = process_files_with_map(txt_files)

# Resultados
print("Tamanho do vocabulário:", vocabulary_size)
