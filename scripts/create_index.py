import os
from whoosh import index
from whoosh.fields import Schema, TEXT, ID
from ingest import ler_documentos  # Importa sua função de ingestão

def criar_indice_local():
    schema = Schema(
        id=ID(stored=True, unique=True),
        nome_arquivo=TEXT(stored=True),
        conteudo=TEXT
    )

    if not os.path.exists("indexdir"):
        os.mkdir("indexdir")

    ix = index.create_in("indexdir", schema)
    writer = ix.writer()

    documentos = ler_documentos()

    for i, doc in enumerate(documentos):
        writer.add_document(
            id=str(i),
            nome_arquivo=doc['nome_arquivo'],
            conteudo=doc['conteudo']
        )
    writer.commit()
    print(f"Índice criado com {len(documentos)} documentos.")

if __name__ == "__main__":
    criar_indice_local()
