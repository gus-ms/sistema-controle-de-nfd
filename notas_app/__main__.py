from notas_app.splash import splash_screen
from notas_app.singleton import verificar_instancia_unica, liberar_instancia

if __name__ == "__main__":
    verificar_instancia_unica()
    try:
        splash_screen()
    finally:
        liberar_instancia()
