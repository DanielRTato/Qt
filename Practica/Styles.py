import sys
from PyQt6.QtWidgets import QMainWindow, QPushButton, QHBoxLayout, QWidget, QApplication, QLabel, QComboBox, QCheckBox, \
    QRadioButton, QGroupBox, QVBoxLayout, QTabWidget, QTextEdit, QButtonGroup


class Styles(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Styles")

        lbl_style = QLabel("Style:")
        cmbComboBox = QComboBox()
        cmbComboBox.addItems(["Fusion", "Windows", "Macintosh"])
        checkBox1 = QCheckBox("Use style`s standar palette")
        checkBox2 = QCheckBox("Disable widgets")
        h1layout = QHBoxLayout()
        h1layout.addWidget(lbl_style)
        h1layout.addWidget(cmbComboBox)
        h1layout.addWidget(checkBox1)
        h1layout.addWidget(checkBox2)


        rboton1 = QRadioButton("Radio button 1")
        rboton2 = QRadioButton("Radio button 2")
        rboton3 = QRadioButton("Radio button 3")
        tri_check = QCheckBox("Tri-state check box")
        tri_check.setTristate(True)                         # Set the checkbox to be tri-state
        group1 = QGroupBox("Group 1")
        grupoBotones1 = QButtonGroup(self)
        grupoBotones1.addButton(rboton1)
        grupoBotones1.addButton(rboton2)
        grupoBotones1.addButton(rboton3)
        grupoBotones1.addButton(tri_check)
        grupoBotones1.setExclusive(True)                          # Make the radio buttons exclusive within the group
        group1_layout = QVBoxLayout()
        group1_layout.addWidget(rboton1)
        group1_layout.addWidget(rboton2)
        group1_layout.addWidget(rboton3)
        group1_layout.addWidget(tri_check)
        group1.setLayout(group1_layout)


        group2 = QGroupBox("Group 2")
        group2_layout = QVBoxLayout()
        btnon1_normal = QPushButton("Default Push Button")      # Default push button
        btnon2_toggle = QPushButton("Toggle Push Button")
        btnon2_toggle.setCheckable(True)                        # Make the button checkable
        btnon3_flat = QPushButton("Flat Push Button")
        btnon3_flat.setFlat(True)                               # Make the button flat
        group2_layout.addWidget(btnon1_normal)
        group2_layout.addWidget(btnon2_toggle)
        group2_layout.addWidget(btnon3_flat)
        group2.setLayout(group2_layout)

        # Nuevo layout horizontal para poner group1 y group2 lado a lado
        h_groups = QHBoxLayout()
        h_groups.addWidget(group1)
        h_groups.addWidget(group2)


        tabbed_stack = QTabWidget()
        tabbed_stack.addTab(QWidget(), "Table")
        tabbed_stack.addTab(QWidget(), "Text Edit")

        txtAreaTexto = QTextEdit()








        layout_vertical = QVBoxLayout()
        layout_vertical.addLayout(h1layout)
        layout_vertical.addLayout(h_groups)
        layout_vertical.addWidget(cmbComboBox)




        container = QWidget()
        container.setLayout(layout_vertical)
        self.setCentralWidget(container)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = Styles()
    ventana.show()
    sys.exit(app.exec())
