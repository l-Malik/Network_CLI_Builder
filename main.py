import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QComboBox


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Définition des proportions de la fenêtre par rapport à l'écran
        WINDOW_WIDTH_RATIO = 2 / 5
        WINDOW_HEIGHT_RATIO = 4 / 5

        # Récupération des dimensions de l'écran
        screen_geometry = QApplication.primaryScreen().availableGeometry()
        screen_width = screen_geometry.width()
        screen_height = screen_geometry.height()

        # Calcul de la taille de la fenêtre en fonction des proportions
        window_width = int(screen_width * WINDOW_WIDTH_RATIO)
        window_height = int(screen_height * WINDOW_HEIGHT_RATIO)

        # Redimensionnement de la fenêtre
        self.resize(window_width, window_height)

        # Calcul de la position de la fenêtre pour la centrer
        window_x = (screen_width - window_width) // 2
        window_y = (screen_height - window_height) // 2
        self.move(window_x, window_y)

        # Définition du titre de la fenêtre
        self.setWindowTitle("Network CLI Builder")

        # Création d'un label
        label = QLabel("Bienvenue dans le configurateur réseau !", self)
        label.setGeometry(20, 20, 250, 25)  # Positionnement du label

        # Création du bouton "Choix d'équipement"
        self.equipment_button = QPushButton("Choix d'équipement", self)
        self.equipment_button.setGeometry(20, 65, 150, 25)  # Positionnement du bouton
        self.equipment_button.clicked.connect(self.show_equipment_options)

        # Création du QComboBox pour les options de configuration
        self.config_options_combobox = QComboBox(self)
        self.config_options_combobox.setGeometry(220, 100, 150, 30)  # Positionnement du combobox
        self.config_options_combobox.hide()  # Cache le combobox initialement

        # Ajout des boutons "Retour" et "Quitter"
        self.back_button = QPushButton("Retour", self)
        self.back_button.setGeometry(20, window_height - 50, 150, 30)
        self.back_button.hide()  # Caché initialement, sera affiché après sélection d'un équipement
        self.back_button.clicked.connect(self.go_back)

        self.quit_button = QPushButton("Quitter", self)
        self.quit_button.setGeometry(window_width - 170, window_height - 50, 150, 30)
        self.quit_button.clicked.connect(self.close_application)

    def show_equipment_options(self):
        # Cacher le bouton "Choix d'équipement"
        self.equipment_button.hide()

        # Créer et afficher les boutons "Routeur" et "Commutateur"
        self.router_button = QPushButton("Routeur", self)
        self.router_button.setGeometry(20, 65, 150, 25)  # Positionnement manuel du bouton "Routeur"
        self.router_button.clicked.connect(self.select_router)
        self.router_button.show()

        self.switch_button = QPushButton("Commutateur", self)
        self.switch_button.setGeometry(190, 65, 150, 25)  # Positionnement manuel du bouton "Commutateur"
        self.switch_button.clicked.connect(self.select_switch)
        self.switch_button.show()

        self.back_button.show()

    def select_router(self):
        self.display_config_options(["Option routeur 1", "Option routeur 2", "Option routeur 3"])
        self.config_options_combobox.setGeometry(20, 65, 150, 25)

    def select_switch(self):
        self.display_config_options(["Option commutateur 1", "Option commutateur 2", "Option commutateur 3"])
        self.config_options_combobox.setGeometry(20, 65, 150, 25)

    def display_config_options(self, options):
        # Supprimer les boutons après sélection de l'équipement
        self.router_button.hide()
        self.switch_button.hide()

        # Afficher les options de configuration dans le combobox
        self.config_options_combobox.clear()
        self.config_options_combobox.addItems(options)
        self.config_options_combobox.show()

    def go_back(self):
        # Cacher les options et réinitialiser l'interface
        self.config_options_combobox.hide()
        self.config_options_combobox.clear()

        # Réafficher les boutons d'équipement
        self.equipment_button.show()
        self.back_button.hide()

    def close_application(self):
        # Fermer l'application
        self.close()


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
