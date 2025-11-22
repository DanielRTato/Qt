import sys
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QWidget,
    QVBoxLayout, QHBoxLayout, QGridLayout,
    QLabel, QPushButton, QLineEdit, QTextEdit,
    QComboBox, QGroupBox, QTabWidget
)
from PyQt6.QtCore import Qt


# ============================================================
#  VENTANA SECUNDARIA (para ejemplos de "abrir otra ventana")
# ============================================================

class VentanaSecundaria(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Ventana Secundaria de Ejemplo")

        layout = QVBoxLayout()

        gpb = QGroupBox("Formulario dentro de ventana secundaria")
        grid = QGridLayout()

        lblTitulo = QLabel("Título")
        lblAutor = QLabel("Autor")
        lblCategoria = QLabel("Categoría")

        self.txtTitulo = QLineEdit()
        self.txtAutor = QLineEdit()
        self.cmbCategoria = QComboBox()
        self.cmbCategoria.addItems(["Programación", "Base de datos", "Redes", "Sistemas"])
        self.cmbCategoria.setCurrentIndex(-1)

        grid.addWidget(lblTitulo, 0, 0)
        grid.addWidget(self.txtTitulo, 0, 1)

        grid.addWidget(lblAutor, 1, 0)
        grid.addWidget(self.txtAutor, 1, 1)

        grid.addWidget(lblCategoria, 2, 0)
        grid.addWidget(self.cmbCategoria, 2, 1)

        gpb.setLayout(grid)

        self.lblInfo = QLabel("Rellena los datos y pulsa Mostrar info")
        btnMostrar = QPushButton("Mostrar info en label")
        btnCerrar = QPushButton("Cerrar solo esta ventana")

        btnMostrar.clicked.connect(self.mostrar_info)
        btnCerrar.clicked.connect(self.close)

        layout.addWidget(gpb)
        layout.addWidget(self.lblInfo)
        layout.addWidget(btnMostrar)
        layout.addWidget(btnCerrar)

        self.setLayout(layout)

    def mostrar_info(self):
        titulo = self.txtTitulo.text().strip()
        autor = self.txtAutor.text().strip()
        categoria = self.cmbCategoria.currentText().strip()
        self.lblInfo.setText(f"Título: {titulo} | Autor: {autor} | Categoría: {categoria}")


# ============================================================
#  PESTAÑA 1: EJEMPLOS BÁSICOS DE BOTONES + EXTRAS
# ============================================================

class TabBotonesBasicos(QWidget):
    def __init__(self):
        super().__init__()

        layout_principal = QVBoxLayout()

        self.lblMensaje = QLabel("Pulsa un botón para ver un ejemplo")
        layout_principal.addWidget(self.lblMensaje)

        # ----------------- Fila 1 -----------------
        fila1 = QHBoxLayout()

        btnHola = QPushButton("Decir Hola")
        btnHola.clicked.connect(self.decir_hola)
        fila1.addWidget(btnHola)

        btnAdios = QPushButton("Decir Adiós")
        btnAdios.clicked.connect(self.decir_adios)
        fila1.addWidget(btnAdios)

        btnSumar = QPushButton("Sumar 2 + 2")
        btnSumar.clicked.connect(self.sumar)
        fila1.addWidget(btnSumar)

        # ----------------- Fila 2 -----------------
        fila2 = QHBoxLayout()

        self.btnCambiarTexto = QPushButton("Cambiar Texto")
        self.btnCambiarTexto.clicked.connect(self.cambiar_texto)
        fila2.addWidget(self.btnCambiarTexto)

        btnLimpiar = QPushButton("Limpiar")
        btnLimpiar.clicked.connect(self.limpiar)
        fila2.addWidget(btnLimpiar)

        btnColorRojo = QPushButton("Texto Rojo")
        btnColorRojo.clicked.connect(self.texto_rojo)
        fila2.addWidget(btnColorRojo)

        # ----------------- Fila 3 -----------------
        fila3 = QHBoxLayout()

        btnColorAzul = QPushButton("Texto Azul")
        btnColorAzul.clicked.connect(self.texto_azul)
        fila3.addWidget(btnColorAzul)

        btnMayus = QPushButton("MAYÚSCULAS")
        btnMayus.clicked.connect(self.mayusculas)
        fila3.addWidget(btnMayus)

        btnMinus = QPushButton("minúsculas")
        btnMinus.clicked.connect(self.minusculas)
        fila3.addWidget(btnMinus)

        layout_principal.addLayout(fila1)
        layout_principal.addLayout(fila2)
        layout_principal.addLayout(fila3)

        # ====================================================
        #  BLOQUE EXTRA: colores, habilitar/deshabilitar, groupbox, grid
        # ====================================================

        # ---- GroupBox con grid de ejemplo ----
        gpbExtra = QGroupBox("Ejemplo de GroupBox + GridLayout")
        grid = QGridLayout()

        self.lblGrid1 = QLabel("Fila 0, Col 0")
        self.lblGrid2 = QLabel("Fila 0, Col 1")
        self.lblGrid3 = QLabel("Fila 1, Col 0")

        grid.addWidget(self.lblGrid1, 0, 0)
        grid.addWidget(self.lblGrid2, 0, 1)
        grid.addWidget(self.lblGrid3, 1, 0, 1, 2)

        gpbExtra.setLayout(grid)
        layout_principal.addWidget(gpbExtra)

        # ---- Botones extra de colores y habilitar/deshabilitar ----
        fila4 = QHBoxLayout()

        btnFondoGris = QPushButton("Fondo gris")
        btnFondoGris.clicked.connect(lambda: self.setStyleSheet("background-color: lightgray;"))
        fila4.addWidget(btnFondoGris)

        btnFondoBlanco = QPushButton("Fondo normal")
        btnFondoBlanco.clicked.connect(lambda: self.setStyleSheet(""))
        fila4.addWidget(btnFondoBlanco)

        btnDeshabilitar = QPushButton("Deshabilitar botones de texto")
        btnDeshabilitar.clicked.connect(self.deshabilitar_botones_texto)
        fila4.addWidget(btnDeshabilitar)

        btnHabilitar = QPushButton("Habilitar botones de texto")
        btnHabilitar.clicked.connect(self.habilitar_botones_texto)
        fila4.addWidget(btnHabilitar)

        layout_principal.addLayout(fila4)

        # Guardamos algunos botones para habilitar/deshabilitar
        self.botones_texto = [
            self.btnCambiarTexto,
            btnLimpiar,
            btnColorRojo,
            btnColorAzul,
            btnMayus,
            btnMinus
        ]

        self.setLayout(layout_principal)

    # ----- métodos de ejemplo -----

    def decir_hola(self):
        self.lblMensaje.setText("Hola! 😀")

    def decir_adios(self):
        self.lblMensaje.setText("Adiós! 👋")

    def sumar(self):
        self.lblMensaje.setText(f"2 + 2 = {2 + 2}")

    def cambiar_texto(self):
        self.lblMensaje.setText("El texto ha sido cambiado!")

    def limpiar(self):
        self.lblMensaje.setText("")

    def texto_rojo(self):
        self.lblMensaje.setStyleSheet("color: red;")

    def texto_azul(self):
        self.lblMensaje.setStyleSheet("color: blue;")

    def mayusculas(self):
        self.lblMensaje.setText(self.lblMensaje.text().upper())

    def minusculas(self):
        self.lblMensaje.setText(self.lblMensaje.text().lower())

    def deshabilitar_botones_texto(self):
        for b in self.botones_texto:
            b.setDisabled(True)

    def habilitar_botones_texto(self):
        for b in self.botones_texto:
            b.setDisabled(False)


# ============================================================
#  PESTAÑA 2: EJEMPLOS AVANZADOS + COMBO EXTRA + MOVER TEXTO + VENTANA
# ============================================================

class TabEjemplosAvanzados(QWidget):
    def __init__(self):
        super().__init__()

        self.ventana_secundaria = None  # referencia para ventana secundaria

        principal = QVBoxLayout()

        # ---------- Formulario avanzado tipo examen ----------
        self.lblID = QLabel("ID")
        self.lblNome = QLabel("Nome")
        self.lblApelidos = QLabel("Apelidos")
        self.lblCidade = QLabel("Cidade")

        self.txtID = QLineEdit()
        self.txtNome = QLineEdit()
        self.txtApelidos = QLineEdit()
        self.txtCidade = QLineEdit()

        self.cmbProvincia = QComboBox()
        self.cmbProvincia.addItems(["A Coruña", "Lugo", "Ourense", "Pontevedra"])
        self.cmbProvincia.setCurrentIndex(-1)

        self.txeDatos = QTextEdit()

        gpb = QGroupBox("Formulario Avanzado")
        grid = QGridLayout()

        grid.addWidget(self.lblID, 0, 0)
        grid.addWidget(self.txtID, 0, 1)

        grid.addWidget(self.lblNome, 1, 0)
        grid.addWidget(self.txtNome, 1, 1)

        grid.addWidget(self.lblApelidos, 2, 0)
        grid.addWidget(self.txtApelidos, 2, 1)

        grid.addWidget(self.lblCidade, 3, 0)
        grid.addWidget(self.txtCidade, 3, 1)

        grid.addWidget(QLabel("Provincia"), 4, 0)
        grid.addWidget(self.cmbProvincia, 4, 1)

        gpb.setLayout(grid)

        btnEngadir = QPushButton("Engadir")
        btnEngadir.clicked.connect(self.on_Engadir)

        btnBuscar = QPushButton("Buscar por ID")
        btnBuscar.clicked.connect(self.on_Buscar)

        btnEditar = QPushButton("Editar")
        btnEditar.clicked.connect(self.on_Editar)

        btnBorrar = QPushButton("Borrar por ID")
        btnBorrar.clicked.connect(self.on_Borrar)

        btnCount = QPushButton("Contar entradas")
        btnCount.clicked.connect(self.on_Contar)

        btnExport = QPushButton("Exportar a TXT")
        btnExport.clicked.connect(self.on_Exportar)

        btnLimpar = QPushButton("Limpar")
        btnLimpar.clicked.connect(self.limparCampos)

        fila_botones = QHBoxLayout()
        fila_botones.addWidget(btnEngadir)
        fila_botones.addWidget(btnBuscar)
        fila_botones.addWidget(btnEditar)
        fila_botones.addWidget(btnBorrar)
        fila_botones.addWidget(btnCount)
        fila_botones.addWidget(btnExport)
        fila_botones.addWidget(btnLimpar)

        principal.addWidget(gpb)
        principal.addLayout(fila_botones)
        principal.addWidget(self.txeDatos)

        # ---------- BLOQUE EXTRA: mover texto entre QTextEdit ----------

        gpbMover = QGroupBox("Mover texto entre cuadros")
        layoutMover = QHBoxLayout()

        self.txeOrigen = QTextEdit()
        self.txeOrigen.setPlaceholderText("Texto origen...")

        self.txeDestino = QTextEdit()
        self.txeDestino.setPlaceholderText("Texto destino...")

        layoutBtnMover = QVBoxLayout()
        btnMoverDerecha = QPushButton("→ mover →")
        btnMoverDerecha.clicked.connect(self.mover_derecha)
        btnMoverIzquierda = QPushButton("← mover ←")
        btnMoverIzquierda.clicked.connect(self.mover_izquierda)

        layoutBtnMover.addStretch()
        layoutBtnMover.addWidget(btnMoverDerecha)
        layoutBtnMover.addWidget(btnMoverIzquierda)
        layoutBtnMover.addStretch()

        layoutMover.addWidget(self.txeOrigen)
        layoutMover.addLayout(layoutBtnMover)
        layoutMover.addWidget(self.txeDestino)

        gpbMover.setLayout(layoutMover)
        principal.addWidget(gpbMover)

        # ---------- BLOQUE EXTRA: ComboBox avanzado (añadir/eliminar) ----------

        gpbComboExtra = QGroupBox("ComboBox avanzado (añadir / borrar)")
        layoutCombo = QHBoxLayout()

        self.cmbExtra = QComboBox()
        self.cmbExtra.addItems(["Opción 1", "Opción 2"])
        self.cmbExtra.setCurrentIndex(-1)

        self.txtNuevoItem = QLineEdit()
        self.txtNuevoItem.setPlaceholderText("Nuevo ítem para combo")

        btnAddItem = QPushButton("Añadir al combo")
        btnAddItem.clicked.connect(self.add_item_combo)

        btnDelItem = QPushButton("Borrar seleccionado")
        btnDelItem.clicked.connect(self.del_item_combo)

        layoutCombo.addWidget(self.cmbExtra)
        layoutCombo.addWidget(self.txtNuevoItem)
        layoutCombo.addWidget(btnAddItem)
        layoutCombo.addWidget(btnDelItem)

        gpbComboExtra.setLayout(layoutCombo)
        principal.addWidget(gpbComboExtra)

        # ---------- BLOQUE EXTRA: abrir ventana y cerrar app ----------

        filaVentana = QHBoxLayout()
        btnAbrirVentana = QPushButton("Abrir ventana secundaria")
        btnAbrirVentana.clicked.connect(self.abrir_ventana_secundaria)
        btnCerrarApp = QPushButton("Cerrar aplicación")
        btnCerrarApp.clicked.connect(self.cerrar_aplicacion)

        filaVentana.addWidget(btnAbrirVentana)
        filaVentana.addWidget(btnCerrarApp)

        principal.addLayout(filaVentana)

        self.setLayout(principal)

    # -------- validación --------
    def validar(self):
        ok = True
        widgets = [
            (self.txtID, self.lblID),
            (self.txtNome, self.lblNome),
            (self.txtApelidos, self.lblApelidos),
            (self.txtCidade, self.lblCidade),
        ]

        for txt, lbl in widgets:
            if txt.text().strip() == "":
                lbl.setStyleSheet("color: red;")
                ok = False
            else:
                lbl.setStyleSheet("color: black;")

        if self.cmbProvincia.currentIndex() == -1:
            self.cmbProvincia.setStyleSheet("color: red;")
            ok = False
        else:
            self.cmbProvincia.setStyleSheet("color: black;")

        return ok

    def crearLinea(self):
        return f"{self.txtID.text()}, {self.txtNome.text()}, {self.txtApelidos.text()}, " \
               f"{self.txtCidade.text()}, {self.cmbProvincia.currentText()}"

    def on_Engadir(self):
        if not self.validar():
            return
        linea = self.crearLinea()
        self.txeDatos.append(linea)
        self.limparCampos()

    def on_Buscar(self):
        id_buscar = self.txtID.text().strip()
        if id_buscar == "":
            return

        lineas = self.txeDatos.toPlainText().split("\n")
        for liña in lineas:
            if not liña.strip():
                continue
            partes = [p.strip() for p in liña.split(",")]
            if partes and partes[0] == id_buscar:
                if len(partes) >= 5:
                    self.txtNome.setText(partes[1])
                    self.txtApelidos.setText(partes[2])
                    self.txtCidade.setText(partes[3])
                    self.cmbProvincia.setCurrentText(partes[4])
                return

    def on_Editar(self):
        if not self.validar():
            return

        id_edit = self.txtID.text().strip()
        nueva_linea = self.crearLinea()

        lineas = self.txeDatos.toPlainText().split("\n")
        nuevas = []

        for liña in lineas:
            if not liña.strip():
                continue
            partes = liña.split(",")
            if partes[0].strip() == id_edit:
                nuevas.append(nueva_linea)
            else:
                nuevas.append(liña)

        self.txeDatos.setText("\n".join(nuevas))
        self.limparCampos()

    def on_Borrar(self):
        id_borrar = self.txtID.text().strip()
        if id_borrar == "":
            return

        lineas = self.txeDatos.toPlainText().split("\n")
        nuevas = []
        for liña in lineas:
            if not liña.strip():
                continue
            partes = liña.split(",")
            if partes[0].strip() != id_borrar:
                nuevas.append(liña)

        self.txeDatos.setText("\n".join(nuevas))
        self.limparCampos()

    def on_Contar(self):
        texto = self.txeDatos.toPlainText().strip()
        if texto == "":
            self.txeDatos.append("TOTAL: 0 entradas")
            return
        total = len([l for l in texto.split("\n") if l.strip() != ""])
        self.txeDatos.append(f"TOTAL: {total} entradas")

    def on_Exportar(self):
        with open("exportado.txt", "w", encoding="utf-8") as f:
            f.write(self.txeDatos.toPlainText())
        self.txeDatos.append(">> Archivo exportado como exportado.txt")

    def limparCampos(self):
        self.txtID.clear()
        self.txtNome.clear()
        self.txtApelidos.clear()
        self.txtCidade.clear()
        self.cmbProvincia.setCurrentIndex(-1)

    # ----- extras: mover texto entre QTextEdit -----

    def mover_derecha(self):
        texto = self.txeOrigen.toPlainText()
        self.txeDestino.setPlainText(texto)
        self.txeOrigen.clear()

    def mover_izquierda(self):
        texto = self.txeDestino.toPlainText()
        self.txeOrigen.setPlainText(texto)
        self.txeDestino.clear()

    # ----- extras: combo avanzado -----

    def add_item_combo(self):
        texto = self.txtNuevoItem.text().strip()
        if texto != "":
            self.cmbExtra.addItem(texto)
            self.txtNuevoItem.clear()

    def del_item_combo(self):
        index = self.cmbExtra.currentIndex()
        if index >= 0:
            self.cmbExtra.removeItem(index)

    # ----- extras: ventana secundaria y cerrar app -----

    def abrir_ventana_secundaria(self):
        if self.ventana_secundaria is None:
            self.ventana_secundaria = VentanaSecundaria()
        self.ventana_secundaria.show()
        self.ventana_secundaria.raise_()
        self.ventana_secundaria.activateWindow()

    def cerrar_aplicacion(self):
        QApplication.instance().quit()


# ============================================================
#  PESTAÑA 3: FORMULARIO CLIENTES (EXAMEN B) + EXTRAS
# ============================================================

class TabClientesGrupoB(QWidget):
    def __init__(self):
        super().__init__()

        layout_principal = QVBoxLayout()
        maia = QGridLayout()

        self.lista_provincias = ["A Coruña", "Lugo", "Ourense", "Pontevedra"]

        self.gpbCliente = QGroupBox("Cliente")

        self.lblNumeroCliente = QLabel("Número Cliente")
        self.lblNomeCliente = QLabel("Nome")
        self.lblApelidosCliente = QLabel("Apelidos")
        self.lblDireccion = QLabel("Dirección")
        self.lblCidade = QLabel("Cidade")
        self.lblProvinciaEstado = QLabel("Provincia")

        self.txtNumeroCliente = QLineEdit()
        self.txtNomeCliente = QLineEdit()
        self.txtApelidosCliente = QLineEdit()
        self.txtDireccion = QLineEdit()
        self.txtCidade = QLineEdit()

        self.cmbProvincia = QComboBox()
        self.cmbProvincia.addItems(self.lista_provincias)
        self.cmbProvincia.setCurrentIndex(-1)

        maia.addWidget(self.lblNumeroCliente, 0, 0)
        maia.addWidget(self.txtNumeroCliente, 0, 1)
        maia.addWidget(self.lblNomeCliente, 0, 2)
        maia.addWidget(self.txtNomeCliente, 0, 3)

        maia.addWidget(self.lblApelidosCliente, 1, 0)
        maia.addWidget(self.txtApelidosCliente, 1, 1, 1, 3)

        maia.addWidget(self.lblDireccion, 2, 0)
        maia.addWidget(self.txtDireccion, 2, 1, 1, 3)

        maia.addWidget(self.lblCidade, 3, 0)
        maia.addWidget(self.txtCidade, 3, 1)
        maia.addWidget(self.lblProvinciaEstado, 3, 2)
        maia.addWidget(self.cmbProvincia, 3, 3)

        self.gpbCliente.setLayout(maia)
        layout_principal.addWidget(self.gpbCliente)

        layout_medio = QHBoxLayout()
        layout_principal.addLayout(layout_medio)

        self.txeClientes = QTextEdit()
        layout_medio.addWidget(self.txeClientes)

        layout_botones = QVBoxLayout()

        btnEngadir = QPushButton("Engadir")
        btnEngadir.clicked.connect(self.btnEngadir_onClick)
        btnEditar = QPushButton("Editar (ejemplo)")
        btnBorrar = QPushButton("Borrar")
        btnBorrar.clicked.connect(self.btn_Borrar_onClick)

        layout_botones.addWidget(btnEngadir)
        layout_botones.addWidget(btnEditar)
        layout_botones.addWidget(btnBorrar)
        layout_botones.addStretch()

        layout_medio.addLayout(layout_botones)

        layout_abajo = QHBoxLayout()
        layout_principal.addLayout(layout_abajo)
        layout_abajo.addStretch()

        btnAceptar = QPushButton("Aceptar")
        btnCancelar = QPushButton("Cancelar")
        layout_abajo.addWidget(btnCancelar)
        layout_abajo.addWidget(btnAceptar)

        # --------- BLOQUE EXTRA CLIENTES ---------

        filaExtras = QHBoxLayout()

        btnBloquear = QPushButton("Bloquear formulario")
        btnBloquear.clicked.connect(self.bloquear_formulario)
        filaExtras.addWidget(btnBloquear)

        btnDesbloquear = QPushButton("Desbloquear formulario")
        btnDesbloquear.clicked.connect(self.desbloquear_formulario)
        filaExtras.addWidget(btnDesbloquear)

        btnColorGpb = QPushButton("Fondo cliente gris")
        btnColorGpb.clicked.connect(
            lambda: self.gpbCliente.setStyleSheet("background-color: #e0e0e0;")
        )
        filaExtras.addWidget(btnColorGpb)

        btnColorGpbReset = QPushButton("Fondo cliente normal")
        btnColorGpbReset.clicked.connect(
            lambda: self.gpbCliente.setStyleSheet("")
        )
        filaExtras.addWidget(btnColorGpbReset)

        btnContarClientes = QPushButton("Contar clientes")
        btnContarClientes.clicked.connect(self.contar_clientes)
        filaExtras.addWidget(btnContarClientes)

        layout_principal.addLayout(filaExtras)

        self.setLayout(layout_principal)

    def btnEngadir_onClick(self):
        if not self.comprobarCampos():
            return

        numero_cliente = self.txtNumeroCliente.text().strip()
        nome = self.txtNomeCliente.text().strip()
        apelidos = self.txtApelidosCliente.text().strip()
        direccion = self.txtDireccion.text().strip()
        cidade = self.txtCidade.text().strip()
        provincia = self.cmbProvincia.currentText().strip()

        linea = f"{numero_cliente}, {nome}, {apelidos}, {direccion}, {cidade}, {provincia}"
        self.txeClientes.append(linea)
        self.limpiarFormulario()

    def comprobarCampos(self):
        todo_cuberto = True

        if self.txtNumeroCliente.text().strip() == "":
            self.lblNumeroCliente.setStyleSheet("color: red;")
            todo_cuberto = False
        else:
            self.lblNumeroCliente.setStyleSheet("color: black;")

        if self.txtNomeCliente.text().strip() == "":
            self.lblNomeCliente.setStyleSheet("color: red;")
            todo_cuberto = False
        else:
            self.lblNomeCliente.setStyleSheet("color: black;")

        if self.txtApelidosCliente.text().strip() == "":
            self.lblApelidosCliente.setStyleSheet("color: red;")
            todo_cuberto = False
        else:
            self.lblApelidosCliente.setStyleSheet("color: black;")

        if self.txtDireccion.text().strip() == "":
            self.lblDireccion.setStyleSheet("color: red;")
            todo_cuberto = False
        else:
            self.lblDireccion.setStyleSheet("color: black;")

        if self.txtCidade.text().strip() == "":
            self.lblCidade.setStyleSheet("color: red;")
            todo_cuberto = False
        else:
            self.lblCidade.setStyleSheet("color: black;")

        if self.cmbProvincia.currentIndex() == -1:
            self.lblProvinciaEstado.setStyleSheet("color: red;")
            todo_cuberto = False
        else:
            self.lblProvinciaEstado.setStyleSheet("color: black;")

        return todo_cuberto

    def limpiarFormulario(self):
        self.txtNumeroCliente.clear()
        self.txtNomeCliente.clear()
        self.txtApelidosCliente.clear()
        self.txtDireccion.clear()
        self.txtCidade.clear()
        self.cmbProvincia.setCurrentIndex(-1)

    def btn_Borrar_onClick(self):
        numero_borrar = self.txtNumeroCliente.text().strip()
        if numero_borrar == "":
            return

        lineas = self.txeClientes.toPlainText().strip().split("\n")
        novas = []
        for liña in lineas:
            if not liña.strip():
                continue
            partes = liña.split(",")
            if partes[0].strip() != numero_borrar:
                novas.append(liña)

        self.txeClientes.setPlainText("\n".join(novas))
        self.limpiarFormulario()

    # ---- extras ----

    def bloquear_formulario(self):
        for w in [self.txtNumeroCliente, self.txtNomeCliente,
                  self.txtApelidosCliente, self.txtDireccion,
                  self.txtCidade, self.cmbProvincia]:
            w.setDisabled(True)

    def desbloquear_formulario(self):
        for w in [self.txtNumeroCliente, self.txtNomeCliente,
                  self.txtApelidosCliente, self.txtDireccion,
                  self.txtCidade, self.cmbProvincia]:
            w.setDisabled(False)

    def contar_clientes(self):
        texto = self.txeClientes.toPlainText().strip()
        if texto == "":
            self.txeClientes.append("TOTAL CLIENTES: 0")
        else:
            total = len([l for l in texto.split("\n") if l.strip() != ""])
            self.txeClientes.append(f"TOTAL CLIENTES: {total}")


# ============================================================
#  PESTAÑA 4: ALBARÁS (EXAMEN A) + EXTRAS
# ============================================================

class TabAlbarrasGrupoA(QWidget):
    def __init__(self):
        super().__init__()

        maia = QGridLayout()
        layout_principal = QVBoxLayout()

        self.gpbAlbara = QGroupBox("Albará")

        self.lista_Albarras = [
            ["1111nm", "02/11/2024", "1111", "Ana", "Ruiz"],
            ["2222io", "09/03/2024", "2222", "Pedro", "Diz"],
            ["3333qw", "23/10/2025", "3333", "Rosa", "Sanz"]
        ]

        self.lblNumeroAlbara = QLabel("Número Albará")
        lblDataAlbara = QLabel("Data")
        lblNumeroCliente = QLabel("Número cliente")
        lblNomeCliente = QLabel("Nome Cliente")
        lblApelidosCliente = QLabel("Apelidos")

        self.cmbNumeroAlbara = QComboBox()
        self.cmbNumeroAlbara.addItems([albara[0] for albara in self.lista_Albarras])
        self.cmbNumeroAlbara.setCurrentIndex(-1)
        self.cmbNumeroAlbara.currentIndexChanged.connect(self.on_cmbNumeroAlbara_changed)

        self.txtDataAlbara = QLineEdit()
        self.txtNumeroCliente = QLineEdit()
        self.txtNomeCliente = QLineEdit()
        self.txtApelidosCliente = QLineEdit()

        btnEngadir = QPushButton("Engadir (ejemplo)")
        btnEditar = QPushButton("Editar")
        btnEditar.clicked.connect(self.onClick_btnEditar)
        btnBorrar = QPushButton("Borrar (ejemplo)")

        self.txeCadroTexto = QTextEdit()

        btnAceptar = QPushButton("Aceptar")
        btnAceptar.setDisabled(True)
        btnCancelar = QPushButton("Cancelar")
        btnCancelar.clicked.connect(self.btnCancelar_onClick)

        maia.addWidget(self.lblNumeroAlbara, 0, 0)
        maia.addWidget(self.cmbNumeroAlbara, 0, 1)
        maia.addWidget(lblDataAlbara, 0, 2)
        maia.addWidget(self.txtDataAlbara, 0, 3)

        maia.addWidget(lblNumeroCliente, 1, 0)
        maia.addWidget(self.txtNumeroCliente, 1, 1)
        maia.addWidget(lblNomeCliente, 1, 2)
        maia.addWidget(self.txtNomeCliente, 1, 3)

        maia.addWidget(lblApelidosCliente, 2, 0)
        maia.addWidget(self.txtApelidosCliente, 2, 1, 1, 3)

        self.gpbAlbara.setLayout(maia)
        layout_principal.addWidget(self.gpbAlbara)

        btn_layout = QHBoxLayout()
        btn_layout.addWidget(btnEngadir)
        btn_layout.addWidget(btnEditar)
        btn_layout.addWidget(btnBorrar)

        layout_principal.addLayout(btn_layout)
        layout_principal.addWidget(self.txeCadroTexto)

        layout_abajo = QHBoxLayout()
        layout_abajo.addStretch()
        layout_abajo.addWidget(btnCancelar)
        layout_abajo.addWidget(btnAceptar)

        layout_principal.addLayout(layout_abajo)

        # --------- EXTRAS ALBARÁ ---------

        filaExtras = QHBoxLayout()

        self.txtNuevoNumero = QLineEdit()
        self.txtNuevoNumero.setPlaceholderText("Nuevo número albará")
        filaExtras.addWidget(self.txtNuevoNumero)

        btnAddAlbara = QPushButton("Añadir nº albará al combo")
        btnAddAlbara.clicked.connect(self.add_albara_combo)
        filaExtras.addWidget(btnAddAlbara)

        btnDelAlbara = QPushButton("Eliminar nº actual")
        btnDelAlbara.clicked.connect(self.del_albara_combo)
        filaExtras.addWidget(btnDelAlbara)

        btnDuplicar = QPushButton("Duplicar línea actual")
        btnDuplicar.clicked.connect(self.duplicar_linea)
        filaExtras.addWidget(btnDuplicar)

        btnLimpiarAlbara = QPushButton("Limpiar albará")
        btnLimpiarAlbara.clicked.connect(self.limpiar_albara)
        filaExtras.addWidget(btnLimpiarAlbara)

        btnValidar = QPushButton("Validar campos (color)")
        btnValidar.clicked.connect(self.validar_campos)
        filaExtras.addWidget(btnValidar)

        layout_principal.addLayout(filaExtras)

        self.setLayout(layout_principal)

    def btnCancelar_onClick(self):
        # cierra la ventana principal (toda la app)
        self.window().close()

    def onClick_btnEditar(self):
        if self.cmbNumeroAlbara.currentIndex() < 0:
            return

        nAlbara = self.cmbNumeroAlbara.currentText()
        data = self.txtDataAlbara.text()
        nCliente = self.txtNumeroCliente.text()
        nome = self.txtNomeCliente.text()
        apell = self.txtApelidosCliente.text()

        linea = f"{nAlbara}, {data}, {nCliente}, {nome}, {apell}"
        self.txeCadroTexto.append(linea)

    def on_cmbNumeroAlbara_changed(self, index: int):
        if index is None or index < 0 or index >= len(self.lista_Albarras):
            self.txtDataAlbara.clear()
            self.txtNumeroCliente.clear()
            self.txtNomeCliente.clear()
            self.txtApelidosCliente.clear()
            return

        albara = self.lista_Albarras[index]
        self.txtDataAlbara.setText(albara[1])
        self.txtNumeroCliente.setText(albara[2])
        self.txtNomeCliente.setText(albara[3])
        self.txtApelidosCliente.setText(albara[4])

    # -------- EXTRAS ALBARÁ --------

    def add_albara_combo(self):
        texto = self.txtNuevoNumero.text().strip()
        if texto != "":
            self.cmbNumeroAlbara.addItem(texto)
            self.txtNuevoNumero.clear()

    def del_albara_combo(self):
        index = self.cmbNumeroAlbara.currentIndex()
        if index >= 0:
            self.cmbNumeroAlbara.removeItem(index)
            self.txtDataAlbara.clear()
            self.txtNumeroCliente.clear()
            self.txtNomeCliente.clear()
            self.txtApelidosCliente.clear()

    def duplicar_linea(self):
        texto = self.txeCadroTexto.toPlainText().strip().split("\n")
        if texto and texto[-1].strip() != "":
            self.txeCadroTexto.append(texto[-1])

    def limpiar_albara(self):
        self.txtDataAlbara.clear()
        self.txtNumeroCliente.clear()
        self.txtNomeCliente.clear()
        self.txtApelidosCliente.clear()
        self.cmbNumeroAlbara.setCurrentIndex(-1)

    def validar_campos(self):
        # Colorea de rojo el label de número de albará si no hay selección
        if self.cmbNumeroAlbara.currentIndex() < 0:
            self.lblNumeroAlbara.setStyleSheet("color: red;")
        else:
            self.lblNumeroAlbara.setStyleSheet("color: black;")

        # Color de fondo del groupbox según si falta algo
        if (self.txtDataAlbara.text().strip() == "" or
                self.txtNumeroCliente.text().strip() == "" or
                self.txtNomeCliente.text().strip() == "" or
                self.txtApelidosCliente.text().strip() == ""):
            self.gpbAlbara.setStyleSheet("background-color: #ffdddd;")
        else:
            self.gpbAlbara.setStyleSheet("")


# ============================================================
#  VENTANA PRINCIPAL CON TODAS LAS PESTAÑAS
# ============================================================

class PracticaComleta(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PracticaComleta - Ejemplos Qt6")

        tabs = QTabWidget()

        tabs.addTab(TabBotonesBasicos(), "Botones básicos")
        tabs.addTab(TabEjemplosAvanzados(), "Avanzado tipo exame")
        tabs.addTab(TabClientesGrupoB(), "Clientes (Grupo B)")
        tabs.addTab(TabAlbarrasGrupoA(), "Albarás (Grupo A)")

        container = QWidget()
        layout = QVBoxLayout()
        layout.addWidget(tabs)
        container.setLayout(layout)

        self.setCentralWidget(container)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = PracticaComleta()
    ventana.show()
    sys.exit(app.exec())
