import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk, ImageDraw
import sys, os
from notas_app.ui.ui_main import main
from notas_app.config import ARQUIVO_EXCEL, PASTA_XML

def resource_path(relative_path):
    """Retorna o caminho do recurso, compatível com .exe e .py"""
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)


def splash_screen():
    splash = tk.Tk()
    splash.overrideredirect(True)
    splash.geometry("420x380+600+250")
    splash.config(bg="white")

    try:
        splash.iconbitmap(resource_path("icone.ico"))
    except Exception:
        pass

    try:
        icone = resource_path("icone.png")
        img = Image.open(icone).convert("RGBA")
        img = img.resize((128, 128), Image.LANCZOS)
        mask = Image.new("L", img.size, 0)
        draw = ImageDraw.Draw(mask)
        draw.ellipse((0, 0, img.size[0], img.size[1]), fill=255)
        img.putalpha(mask)
        logo = ImageTk.PhotoImage(img)
        label_img = tk.Label(splash, image=logo, bg="white")
        label_img.image = logo
        label_img.pack(pady=30)
    except Exception:
        label_img = tk.Label(splash, text="Importador de Notas",
                             font=("Segoe UI", 18, "bold"), bg="white", fg="black")
        label_img.pack(pady=60)

    label_nome = tk.Label(
        splash, text="Importador de Notas",
        font=("Segoe UI", 16, "bold"), bg="white", fg="black"
    )
    label_nome.pack(pady=5)

    status_label = tk.Label(splash, text="Inicializando...", font=("Segoe UI", 12),
                            bg="white", fg="gray")
    status_label.pack(pady=10)

    progress = ttk.Progressbar(splash, orient="horizontal", length=300, mode="determinate")
    progress.pack(pady=20)

    etapas = [
        ("Verificando planilha", lambda: os.path.exists(ARQUIVO_EXCEL)),
        ("Verificando pasta XML", lambda: os.makedirs(PASTA_XML, exist_ok=True) or True),
        ("Finalizando", lambda: True)
    ]
    progresso_total = 0
    etapa_atual = 0
    pontos_contador = 0
    progresso_por_etapa = 100 // len(etapas)

    def atualizar():
        nonlocal progresso_total, etapa_atual, pontos_contador

        # Aumenta progresso mais rápido (de 1 em 1 para 3 em 3)
        if progresso_total < 100:
            progresso_total += 3
            if progresso_total > 100:
                progresso_total = 100
            progress["value"] = progresso_total

        # Atualiza texto com pontos animados (ligeiramente mais rápido)
        if etapa_atual < len(etapas):
            texto_base, func = etapas[etapa_atual]
            if progresso_total % 3 == 0:  # reduz intervalo para pontos trocarem mais rápido
                pontos = "." * ((pontos_contador % 3) + 1)
                status_label.config(text=texto_base + pontos)
                pontos_contador += 1

            if progresso_total >= (etapa_atual + 1) * progresso_por_etapa:
                try:
                    func()
                except Exception as e:
                    messagebox.showerror("Erro", str(e))
                etapa_atual += 1

        else:
            status_label.config(text="Concluído!")
            if progresso_total >= 100:
                splash.after(300, lambda: (splash.destroy(), main()))  # reduz tempo antes de abrir main
                return

        splash.after(30, atualizar)  # atualiza mais rápido (de 50ms para 30ms)

    splash.after(100, atualizar)  # inicia atualização mais cedo
    splash.mainloop()
