# notas_app/singleton.py
import os
import sys
import tempfile
import tkinter.messagebox as messagebox

LOCKFILE = os.path.join(tempfile.gettempdir(), "importador_notas.lock")

def verificar_instancia_unica():
    """Impede que duas instâncias rodem ao mesmo tempo."""
    if os.path.exists(LOCKFILE):
        messagebox.showwarning("Aviso", "O Importador de Notas já está em execução.")
        sys.exit(0)
    with open(LOCKFILE, "w") as f:
        f.write("rodando")

def liberar_instancia():
    """Remove o lockfile ao sair do programa."""
    if os.path.exists(LOCKFILE):
        os.remove(LOCKFILE)
