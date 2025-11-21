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

        self.lista_provincias = ["A Coruña", "Lugo", "Ourense", "Pontevedra"] # Lista de provincias


        gpbCliente = QGroupBox("Cliente")

        lblNumeroCliente = QLabel("Número Cliente")
        lblNomeCliente = QLabel("Nome")
        lblApelidosCliente = QLabel("Apelidos")
        lblDirección = QLabel("Dirección")
        lblCidade = QLabel("Cidade")
        lblProvinciaEstado = QLabel("Provincia")

        self.txtNumeroCliente = QLineEdit()
        self.txtNomeCliente = QLineEdit()
        self.txtApelidosCliente = QLineEdit()
        self.txtDireccion = QLineEdit()
        self.txtCidade = QLineEdit()

        self.cmbProvincia = QComboBox()
        self.cmbProvincia.addItems(self.lista_provincias) # Engadir provincias ao combo box
        self.cmbProvincia.setCurrentIndex(-1) # que no seleccione ningún elemento por defecto

        maia.addWidget(lblNumeroCliente, 0, 0)
        maia.addWidget(self.txtNumeroCliente, 0, 1)
        maia.addWidget(lblNomeCliente, 0, 2)
        maia.addWidget(self.txtNomeCliente, 0, 3)
        maia.addWidget(lblApelidosCliente, 1, 0)
        maia.addWidget(self.txtApelidosCliente, 1, 1, 1, 3)
        maia.addWidget(lblDirección, 2, 0)
        maia.addWidget(self.txtDireccion, 2, 1, 1, 3)
        maia.addWidget(lblCidade, 3, 0)
        maia.addWidget(self.txtCidade, 3, 1)
        maia.addWidget(lblProvinciaEstado, 3, 2)
        maia.addWidget(self.cmbProvincia, 3, 3)

        gpbCliente.setLayout(maia)
        layout_principal.addWidget(gpbCliente)

        layout_medio = QHBoxLayout()
        layout_principal.addLayout(layout_medio)


        self.txeClientes = QTextEdit()
        layout_medio.addWidget(self.txeClientes)

        layout_botones = QVBoxLayout()

        btnEngadir = QPushButton("Engadir")
        btnEngadir.clicked.connect(self.btnEngadir_onClick)
        btnEditar = QPushButton("Editar")
        btnBorrar = QPushButton("Borrar")

        layout_botones.addWidget(btnEngadir)
        layout_botones.addWidget(btnEditar)
        layout_botones.addWidget(btnBorrar)
        layout_botones.addStretch() # Engadir un espazo flexible para empurrar os botóns cara arriba

        layout_medio.addLayout(layout_botones)


        layout_abajo = QHBoxLayout()
        layout_principal.addLayout(layout_abajo)
        layout_abajo.addStretch() # Engadir un espazo flexible á esquerda

        btnAceptar = QPushButton("Aceptar")
        btnCancelar = QPushButton("Cancelar")
        layout_abajo.addWidget(btnCancelar)
        layout_abajo.addWidget(btnAceptar)


        container = QWidget()
        container.setLayout(layout_principal)
        self.setCentralWidget(container)

    def btnEngadir_onClick(self):
        numero_cliente = self.txtNumeroCliente.text()
        nome = self.txtNomeCliente.text()
        apelidos = self.txtApelidosCliente.text()
        direccion = self.txtDireccion.text()
        cidade = self.txtCidade.text()
        provincia = self.cmbProvincia.currentText()

        linea = f"{numero_cliente}, {nome}, {apelidos}, {direccion}, {cidade}, {provincia}"

        self.txeClientes.append(linea)
        self.limpiarFormulario()

    def limpiarFormulario(self):
        self.txtNumeroCliente.clear()
        self.txtNomeCliente.clear()
        self.txtApelidosCliente.clear()
        self.txtDireccion.clear()
        self.txtCidade.clear()
        self.cmbProvincia.setCurrentIndex(-1) # Deseleccionar o combo box



if __name__ == "__main__":
    aplicacion = QApplication(sys.argv)
    fiestra = FiestraPrincipal()
    fiestra.show()
    sys.exit(aplicacion.exec())

    aplicacion.exec()