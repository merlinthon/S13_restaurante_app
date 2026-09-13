import tkinter as tk
from pathlib import Path
from servicios.archivo_servicio import ArchivoServicio
from servicios.restaurante_servicio import RestauranteServicio
from ui.login_view import LoginView
from ui.main_view import MainView

# Único punto de entrada: prepara todo y controla el cambio de vistas
def main():
    # 1. Crear la ventana PRINCIPAL ÚNICA — un solo Tk() y un solo mainloop()
    ventana = tk.Tk()

    # 2. Preparar dependencias: cargar datos y crear servicio
    ruta = Path(__file__).resolve().parent / "datos"
    archivo = ArchivoServicio(str(ruta))
    productos = archivo.cargar_productos()
    usuarios = archivo.cargar_usuarios()
    servicio = RestauranteServicio(productos, usuarios)

    # 3. Preparar vistas, entregándoles el servicio
    vista_login = LoginView(ventana, servicio, al_ingresar)
    vista_principal = MainView(ventana, servicio, al_cerrar_sesion)

    # 4. Funciones de control de flujo entre vistas
    def al_ingresar(usuario_actual):
        vista_principal.mostrar(usuario_actual)

    def al_cerrar_sesion():
        vista_login.mostrar()

    # 5. Iniciar mostrando la pantalla de acceso
    vista_login.mostrar()

    # 6. Ejecutar el ciclo gráfico
    ventana.mainloop()

if __name__ == "__main__":
    main()