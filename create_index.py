import os
from whoosh import index
from whoosh.fields import Schema, TEXT, ID

def criar_indice_local():
    schema = Schema(id=ID(stored=True, unique=True),
                    nome_arquivo=TEXT(stored=True),
                    conteudo=TEXT)

    if not os.path.exists("indexdir"):
        os.mkdir("indexdir")

    ix = index.create_in("indexdir", schema)
    writer = ix.writer()

    # Exemplo para adicionar um documento
    writer.add_document(id="1", nome_arquivo="exemplo.txt", conteudo="Este é o conteúdo do documento")
    writer.commit()
    print("Índice criado localmente em 'indexdir'.")

if __name__ == "__main__":
    criar_indice_local()
