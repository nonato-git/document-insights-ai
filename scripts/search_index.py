import os
from whoosh.index import open_dir
from whoosh.qparser import QueryParser

def buscar_no_indice(consulta):
    # Abre o índice que criamos na pasta indexdir
    if not os.path.exists("indexdir"):
        print("Índice não encontrado. Rode o create_index.py primeiro.")
        return

    ix = open_dir("indexdir")

    with ix.searcher() as searcher:
        parser = QueryParser("content", ix.schema)
        query = parser.parse(consulta)
        resultados = searcher.search(query, limit=10)

        if resultados:
            print(f"Resultados para '{consulta}':\n")
            for i, resultado in enumerate(resultados):
                print(f"{i+1}. Documento: {resultado['title']}")
                print(f"Conteúdo: {resultado['content'][:200]}...\n")
        else:
            print(f"Nenhum resultado encontrado para '{consulta}'.")

if __name__ == "__main__":
    while True:
        consulta = input("Digite sua busca (ou 'sair' para encerrar): ")
        if consulta.lower() == "sair":
            break
        buscar_no_indice(consulta)
