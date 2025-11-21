import sys

from PyQt6.QtWidgets import (QApplication, QMainWindow, QGridLayout, QVBoxLayout, QHBoxLayout, QWidget,
                             QLabel, QListWidget, QPushButton, QComboBox, QLineEdit,
                             QRadioButton, QGroupBox, QTableView, QAbstractItemView, QTextEdit)

class FiestraPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Examen 16-11-2025 group B")

        layout_principal = QVBoxLayout()
        maia = QGridLayout()

        gpbCliente = QGroupBox("Cliente")

        lblNumeroCliente = QLabel("Número Cliente")
        lblNomeCliente = QLabel("Nome")
        lblApelidosCliente = QLabel("Apelidos")
        lblDirección = QLabel("Dirección")
        lblCidade = QLabel("Cidade")
        lblProvinciaEstado = QLabel("Provincia")

        txtNumeroCliente = QLineEdit()
        txtNomeCliente = QLineEdit()
        txtApelidosCliente = QLineEdit()
        txtDireccion = QLineEdit()
        txtCidade = QLineEdit()
        cmbProvincia = QComboBox()

        maia.addWidget(lblNumeroCliente, 0, 0)
        maia.addWidget(txtNumeroCliente, 0, 1)
        maia.addWidget(lblNomeCliente, 0, 2)
        maia.addWidget(txtNomeCliente, 0, 3)
        maia.addWidget(lblApelidosCliente, 1, 0)
        maia.addWidget(txtApelidosCliente, 1, 1, 1, 3)
        maia.addWidget(lblDirección, 2, 0)
        maia.addWidget(txtDireccion, 2, 1, 1, 3)
        maia.addWidget(lblCidade, 3, 0)
        maia.addWidget(txtCidade, 3, 1)
        maia.addWidget(lblProvinciaEstado, 3, 2)
        maia.addWidget(cmbProvincia, 3, 3)

        gpbCliente.setLayout(maia)
        layout_principal.addWidget(gpbCliente)


        self.txeClientes = QTextEdit()

        btnEngadir = QPushButton("Engadir")
        btnEditar = QPushButton("Editar")
        btnBorrar = QPushButton("Borrar")

        btnAceptar = QPushButton("Aceptar")
        btnCancelar = QPushButton("Cancelar")


        container = QWidget()
        container.setLayout(layout_principal)
        self.setCentralWidget(container)


if __name__ == "__main__":
    aplicacion = QApplication(sys.argv)
    fiestra = FiestraPrincipal()
    fiestra.show()
    sys.exit(aplicacion.exec())

    aplicacion.exec()