import os
from docx import Document
from fpdf import FPDF

# Cria a pasta data/ se não existir
os.makedirs("data", exist_ok=True)

# === exemplo1.txt ===
with open("data/exemplo1.txt", "w", encoding="utf-8") as f:
    f.write("Inteligência Artificial (IA) é um campo da ciência da computação que foca na criação de sistemas capazes de simular a inteligência humana. Entre suas aplicações estão assistentes virtuais, carros autônomos e diagnósticos médicos automatizados.")

# === exemplo2.pdf ===
class PDF(FPDF):
    pass

pdf = PDF()
pdf.add_page()
pdf.set_font("Arial", size=12)
pdf.multi_cell(0, 10, "A mineração de textos é uma técnica usada para extrair informações úteis de grandes volumes de texto. Isso inclui tarefas como análise de sentimentos, extração de palavras-chave e resumo automático.")
pdf.output("data/exemplo2.pdf")

# === exemplo3.docx ===
doc = Document()
doc.add_paragraph("Ferramentas como o Whoosh permitem a criação de mecanismos de busca locais, sem necessidade de servidores externos. São úteis em projetos pequenos e médios, especialmente para aprendizado.")
doc.save("data/exemplo3.docx")

print("Arquivos de exemplo criados com sucesso em /data ✅")
