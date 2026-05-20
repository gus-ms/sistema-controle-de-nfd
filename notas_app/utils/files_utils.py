import os
import platform
import subprocess
import shutil
from notas_app.config import PASTA_PROCESSADOS, PASTA_XML

def abrir_planilha(caminho):
    if platform.system() == "Windows":
        os.startfile(caminho)
    elif platform.system() == "Darwin":
        subprocess.call(["open", caminho])
    else:
        subprocess.call(["xdg-open", caminho])

def renomear_arquivo(caminho_original, numero_nota, nome_empresa):
    partes_nome = nome_empresa.split()
    primeiro_nome = partes_nome[0].strip()
    if len(primeiro_nome) <= 1 and len(partes_nome) > 1:
        primeiro_nome += f"_{partes_nome[1].strip()}"
    novo_nome = f"NFD_{numero_nota}_{primeiro_nome}.xml"
    novo_caminho = os.path.join(PASTA_PROCESSADOS, novo_nome)
    return novo_caminho
