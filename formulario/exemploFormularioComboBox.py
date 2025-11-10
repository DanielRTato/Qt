# python
import sys
from PyQt6.QtWidgets import QWidget, QGridLayout, QVBoxLayout, QLineEdit, QApplication, QComboBox, QMainWindow, QTextEdit

class exemploFormularioComboBox(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Exemplo de formulario con ComboBox")

        maia = QGridLayout()
        caixaV = QVBoxLayout()

        self.nome_dni = [["Ana", "Pepe", "Juan"], ["3333R", "4444S", "5555T"]]

        txtCadro1 = QLineEdit()
        txtCadro2 = QLineEdit()
        self.cmbComboBox = QComboBox()
        self.cmbComboBox.addItems(self.nome_dni[0])
        self.cmbComboBox.currentIndexChanged.connect(self.on_cmbComboBox_currentIndexChanged)
        self.cmbComboBox.currentTextChanged.connect(self.on_ComboBox_currentTextChanged)


        caixaV.addWidget(txtCadro1)
        caixaV.addWidget(txtCadro2)
        caixaV.addWidget(self.cmbComboBox)

        maia.addLayout(caixaV,1, 0, 1,1)

        self.txtAreaTexto = QTextEdit()
        maia.addWidget(self.txtAreaTexto, 1, 1, 1, 1)

        container = QWidget()
        container.setLayout(maia)
        self.setCentralWidget(container)

    def on_cmbComboBox_currentIndexChanged(self, indice):
        print(self.cmbComboBox.currentText())
        self.txtAreaTexto.setPlainText("Selecionaste el usuario: " + self.cmbComboBox.itemText(indice) + " con dni: " + self.nome_dni[1][indice])

    def on_ComboBox_currentTextChanged(self, texto):
        print("O combo ten seleccionado o texto: " + texto)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = exemploFormularioComboBox()
    ventana.show()
    sys.exit(app.exec())