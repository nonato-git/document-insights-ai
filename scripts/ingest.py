import os
from typing import List, Dict

# Para PDF
import PyPDF2

# Para DOCX
import docx

def extrair_texto_pdf(caminho_arquivo: str) -> str:
    texto = ''
    try:
        with open(caminho_arquivo, 'rb') as file:
            leitor = PyPDF2.PdfReader(file)
            for pagina in leitor.pages:
                texto += pagina.extract_text() or ''
    except Exception as e:
        print(f'Erro ao ler PDF {caminho_arquivo}: {e}')
    return texto

def extrair_texto_docx(caminho_arquivo: str) -> str:
    texto = ''
    try:
        doc = docx.Document(caminho_arquivo)
        for paragrafo in doc.paragraphs:
            texto += paragrafo.text + '\n'
    except Exception as e:
        print(f'Erro ao ler DOCX {caminho_arquivo}: {e}')
    return texto

def extrair_texto_txt(caminho_arquivo: str) -> str:
    texto = ''
    try:
        with open(caminho_arquivo, 'r', encoding='utf-8', errors='ignore') as f:
            texto = f.read()
    except Exception as e:
        print(f'Erro ao ler TXT {caminho_arquivo}: {e}')
    return texto

def preprocessar_texto(texto: str) -> str:
    texto = texto.replace('\n', ' ').strip()
    return texto

def ler_documentos(diretorio='data') -> List[Dict[str, str]]:
    documentos = []
    for filename in os.listdir(diretorio):
        caminho = os.path.join(diretorio, filename)
        if os.path.isfile(caminho):
            if filename.lower().endswith('.pdf'):
                texto = extrair_texto_pdf(caminho)
            elif filename.lower().endswith('.docx'):
                texto = extrair_texto_docx(caminho)
            elif filename.lower().endswith('.txt'):
                texto = extrair_texto_txt(caminho)
            else:
                print(f'Formato não suportado para arquivo {filename}, pulando.')
                continue

            texto_limpo = preprocessar_texto(texto)
            documentos.append({'nome_arquivo': filename, 'conteudo': texto_limpo})

    return documentos

if __name__ == '__main__':
    docs = ler_documentos()
    print(f'Foram processados {len(docs)} documentos.')
    for doc in docs:
        print(f"Arquivo: {doc['nome_arquivo']} - Conteúdo (primeiros 150 caracteres): {doc['conteudo'][:150]}")
