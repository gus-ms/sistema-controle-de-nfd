import os
import sys

# --- Caminhos ---
if getattr(sys, 'frozen', False):
    BASE_DIR = os.path.dirname(sys.executable)
else:
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))

PASTA_XML = os.path.join(BASE_DIR, "xmls")
PASTA_PROCESSADOS = os.path.join(PASTA_XML, "processados")
ARQUIVO_EXCEL = os.path.join(BASE_DIR, "Nota_Devolucao.xlsx")

# --- Status ---
STATUS_COLETA = "Em Coleta,Coletado"

# --- Cabeçalhos e largura das colunas ---
CABECALHOS = [
    "N. Nota", "Emissão", "Empresa Dest.", "Produto", "Volume",
    "Valor Un. Produto", "Valor T. Produto", "Valor T. Nota",
    "Referencia", "Status Coleta"
]
COL_WIDTHS = [12, 12, 25, 40, 10, 18, 18, 18, 15, 15]
