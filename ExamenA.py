import sys
from PyQt6.QtWidgets import (QApplication, QMainWindow, QLabel, QPushButton,
                             QComboBox, QLineEdit, QGroupBox, QTextEdit,
                             QGridLayout, QWidget, QVBoxLayout, QHBoxLayout)


class FiestraPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Examen 16-11-2025 group A")

        maia = QGridLayout()
        layout_principal = QVBoxLayout()

        gpbAlbara = QGroupBox("Albará")

        self.lista_Albarras = [
            ["1111nm", "02/11/2024", "1111", "Ana", "Ruiz"],
            ["2222io", "09/03/2024", "2222", "Pedro", "Diz"],
            ["3333qw", "23/10/2025", "3333", "Rosa", "Sanz"]
        ]

        lblNumeroAlbara = QLabel("Número Albará")
        lblDataAlbara = QLabel("Data")
        lblNumeroCliente = QLabel("Número cliente")
        lblNomeCliente = QLabel("Nome Cliente")
        lblApelidosCliente = QLabel("Apelidos")

        self.cmbNumeroAlbara = QComboBox()
        self.cmbNumeroAlbara.addItems([albara[0]for albara in self.lista_Albarras]) # Engadir números de albarás ao combo box
        self.cmbNumeroAlbara.setCurrentIndex(-1)  # que no seleccione ningún elemento por defecto

        self.txtDataAlbara = QLineEdit()
        self.txtNumeroCliente = QLineEdit()
        self.txtNomeCliente = QLineEdit()
        self.txtApelidosCliente = QLineEdit()

        btnEngadir = QPushButton("Engadir")
        btnEngadir.clicked.connect(self.onClick_btnEngadir)
        btnEditar = QPushButton("Editar")
        btnBorrar = QPushButton("Borrar")

        txtCodigoProducto = QLineEdit()
        txtCantidade = QLineEdit()
        txtPrezoUnitario = QLineEdit()

        self.txeCadroTexto = QTextEdit()

        btnAceptar = QPushButton("Aceptar")
        btnAceptar.setDisabled(True) # Botón deshabilitado
        btnCancelar = QPushButton("Cancelar")
        btnCancelar.clicked.connect(self.btnCancelar_onClick) # Conectar o evento de clic ao método

        maia.addWidget(lblNumeroAlbara, 0, 0)
        maia.addWidget(self.cmbNumeroAlbara, 0, 1)
        maia.addWidget(lblDataAlbara, 0, 2)
        maia.addWidget(self.txtDataAlbara, 0, 3)

        maia.addWidget(lblNumeroCliente, 1, 0)
        maia.addWidget(self.txtNumeroCliente, 1, 1)
        maia.addWidget(lblNomeCliente, 1, 2)
        maia.addWidget(self.txtNomeCliente, 1, 3)

        maia.addWidget(lblApelidosCliente, 2, 0)
        maia.addWidget(self.txtApelidosCliente, 2, 1, 1, 3)
        gpbAlbara.setLayout(maia)
        layout_principal.addWidget(gpbAlbara)

        btn_layout = QHBoxLayout()
        btn_layout.addWidget(btnEngadir)
        btn_layout.addWidget(btnEditar)
        btn_layout.addWidget(btnBorrar)

        layout_principal.addLayout(btn_layout)
        layout_principal.addWidget(self.txeCadroTexto)

        layout_abajo = QHBoxLayout()
        layout_abajo.addStretch() # Engadir un espazo flexible á esquerda

        layout_abajo.addWidget(btnAceptar)
        layout_abajo.addWidget(btnCancelar)
        #layout_abajo.addStretch() # Engadir un espazo flexible á dereita

        layout_principal.addLayout(layout_abajo)

        container = QWidget()
        container.setLayout(layout_principal)
        self.setCentralWidget(container)


    # funcion que cieera la aplicacion
    def btnCancelar_onClick(self):
        self.close()

    def onClick_btnEngadir(self):
        nAlbara = self.cmbNumeroAlbara.currentText()
        data = self.txtDataAlbara.text()
        nCliente = self.txtNumeroCliente.text()
        nome = self.txtNomeCliente.text()
        apell = self.txtApelidosCliente.text()

        texto = f" {nAlbara}, {data}, {nCliente}, {nome}, {apell}"
        self.txeCadroTexto.append(texto)

if __name__ == "__main__":
    aplicacion = QApplication(sys.argv)
    fiestra = FiestraPrincipal()
    fiestra.show()
    sys.exit(aplicacion.exec())
