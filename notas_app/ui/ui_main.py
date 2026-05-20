import os
import shutil
import tkinter as tk
from tkinter import Button, filedialog, messagebox

from notas_app.ui.ui_consulta import buscar_notas
from notas_app.utils.xml_utils import processar_xmls
from notas_app.utils.xml_utils import extrair_dados_xml
from notas_app.utils.files_utils import abrir_planilha
from notas_app.utils.excel_utils import salvar_planilha
from notas_app.config import PASTA_XML
from notas_app.config import ARQUIVO_EXCEL, STATUS_COLETA

import sys

# ---------------------------
# Função resource_path
# ---------------------------
def resource_path(relative_path):
    """Retorna o caminho do recurso, compatível com .exe e .py"""
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)


def importar_xmls_gui():
    arquivos = filedialog.askopenfilenames(title="Selecione os XMLs", filetypes=[("Arquivos XML", "*.xml")])
    if arquivos:
        os.makedirs(PASTA_XML, exist_ok=True)
        novos_caminhos = []
        for caminho in arquivos:
            try:
                novo_caminho = os.path.join(PASTA_XML, os.path.basename(caminho))
                shutil.move(caminho, novo_caminho)
                novos_caminhos.append(novo_caminho)
            except PermissionError:
                pass
        try:
            processar_xmls(novos_caminhos)
        except Exception as e:
            messagebox.showerror("Erro", str(e))

def abrir_planilha_gui():
    try:
        abrir_planilha(ARQUIVO_EXCEL)
    except Exception as e:
        messagebox.showerror("Erro", str(e))


def main():
    root = tk.Tk()
    root.title("Importador de Notas")
    root.geometry("400x250")
    root.resizable(False, False)

    # ---------------------------
    # Ícone da janela principal (.ico)
    # ---------------------------
    icone_janela = resource_path("icone.ico")
    if os.path.exists(icone_janela):
        try:
            root.iconbitmap(icone_janela)
        except Exception as e:
            print("Não foi possível carregar icone.ico na janela principal:", e)
    else:
        print("Arquivo icone.ico não encontrado.")

    # ---------------------------
    # Botões
    # ---------------------------
    Button(root, text="📥 Importar XMLs", command=importar_xmls_gui,
           width=20, height=2, bg="green", fg="white", font=("Segoe UI", 10, "bold")).pack(pady=8)

    Button(root, text="📂 Abrir Planilha", command=abrir_planilha_gui,
           width=20, height=2, bg="blue", fg="white", font=("Segoe UI", 10, "bold")).pack(pady=8)

    Button(root, text="🔍 Consultar Notas", command=buscar_notas,
           width=20, height=2, bg="orange", fg="white", font=("Segoe UI", 10, "bold")).pack(pady=8)

    Button(root, text="❌ Sair", command=lambda: (root.destroy(), exit()),
           width=20, height=2, bg="red", fg="white", font=("Segoe UI", 10, "bold")).pack(pady=8)

    root.mainloop()
