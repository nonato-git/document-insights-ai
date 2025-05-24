
# Document Insights AI

Projeto de ingestão, indexação e busca de documentos utilizando Python e a biblioteca Whoosh.

---

## Descrição

Este projeto tem como objetivo aplicar técnicas de organização e pesquisa de documentos através da ingestão de dados e criação de índices inteligentes usando inteligência artificial local (Whoosh). Permite extrair conhecimento de textos variados (txt, pdf, docx) e realizar buscas eficientes.

---

## Estrutura do Projeto

- `/data/` — arquivos de exemplo (.txt, .pdf, .docx) para testes
- `/scripts/` — scripts Python para ingestão, criação de índice, busca e geração de arquivos de exemplo
- `README.md` — documentação do projeto

---

## Scripts

### 1. Gerar arquivos de exemplo

```bash
python scripts/gerar_exemplos.py
```

Cria arquivos de texto, PDF e DOCX na pasta `/data/` para teste.

---

### 2. Ingestão e criação do índice

```bash
python scripts/create_index.py
```

Lê os arquivos da pasta `/data/` e cria um índice local na pasta `/indexdir/`.

---

### 3. Buscar no índice

```bash
python scripts/search_index.py
```

Executa uma busca interativa nos documentos indexados. Digite termos para pesquisar e visualize os resultados. Digite `sair` para encerrar.

---

## Dependências

Instale as bibliotecas necessárias com:

```bash
pip install python-docx fpdf whoosh
```

---

## Como rodar

1. Clone o repositório:

```bash
git clone <[URL_DO_REPOSITORI](https://github.com/nonato-git/copilot-openai-lab/tree/main)>
cd document-insights-ai
```

2. (Opcional) Crie e ative um ambiente virtual Python:

```bash
python -m venv venv
venv\Scripts\activate  # Windows
# ou
source venv/bin/activate  # Linux/Mac
```

3. Instale as dependências (ver acima)

4. Gere os arquivos de exemplo, crie o índice e faça buscas seguindo os scripts listados.

---

## Considerações Finais

Este projeto é uma aplicação prática dos conceitos de ingestão, indexação e pesquisa de documentos utilizando Python. Pode ser expandido para incluir outros formatos, mecanismos de busca mais robustos ou até uma interface web.

---

## Autor

Nonato-git

---

## Link do repositório

https://github.com/nonato-git/document-insights-ai
