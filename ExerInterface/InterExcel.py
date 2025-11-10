import sys
from PyQt6.QtWidgets import QApplication, QWidget, QMainWindow, QGridLayout, QPushButton, QLabel, QListWidget
import modeloLista


class InterExcel(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("EXCELeINFO - HOJAS")
        self.setMinimumSize(1000, 700)

        # Contenedor central y layout
        contenedor = QWidget()
        cuadricula = QGridLayout()
        contenedor.setLayout(cuadricula)
        self.setCentralWidget(contenedor)

        listaFollas = ["F1", "f2", "f3"]
        self.modelo = modeloLista.ModeloFollas(listaFollas)

        # Etiquetas
        lbl_visible = QLabel("Hojas visibles")
        lbl_oculta = QLabel("Hojas ocultas")

        # Listas
        lista_visible = QListWidget()
        lista_oculta = QListWidget()

        # Botones
        bton_ocultar = QPushButton("<< Ocultar")
        bton_mostrar = QPushButton(">> Mostrar")
        bton_cerrar = QPushButton("Cerrar")

        bton_mostrar.clicked.connect(self.on_bton_mostar_cliked)
        bton_ocultar.clicked.connect(self.on_bton_ocultar_cliked)


        # Ajustes de tamaño
        for boton in (bton_ocultar, bton_mostrar, bton_cerrar):
            boton.setFixedWidth(60)

        # Distribución correcta en la cuadrícula
        cuadricula.addWidget(lbl_visible, 0, 0)
        cuadricula.addWidget(lbl_oculta, 0, 2, 1, 1)
        cuadricula.addWidget(lista_visible, 1, 0, 5, 1)
        lista_visible.setModel(self.modelo)
        cuadricula.addWidget(lista_oculta, 1, 2, 5, 1)
        cuadricula.addWidget(bton_ocultar, 1, 1, 1, 1)
        cuadricula.addWidget(bton_mostrar,3,1,1,1)
        cuadricula.addWidget(bton_cerrar, 8, 2, 1, 1)

        # Ejemplo de datos
        lista_visible.addItems(["Hoja1", "Hoja2", "Hoja3"])
        lista_oculta.addItems(["Hoja4", "Hoja5"])

    def on_bton_mostar_cliked(self):
        indices = self.listaOcultar.selectIndexes()



if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = InterExcel()
    ventana.show()
    sys.exit(app.exec())
