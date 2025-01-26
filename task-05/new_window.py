from PySide6.QtWidgets import QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QDialog, QApplication
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt
import requests
from PIL import Image
import os
from os import listdir


class NewWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(850, 500)
        main_layout = QVBoxLayout()

        self.label1 = QLabel("Captured Pokemon", self)
        self.label1.setGeometry(350, 25, 280, 40)


        self.label2 = QLabel(self)
        self.label2.setGeometry(250,45,300,500)
        self.label2.setScaledContents(True)
        main_layout.addWidget(self.label2)


        self.setStyleSheet("""
            QLabel{
                           color:black;

                           font: 18px bold;}
        """) 

        folder_dir = "/home/sravan-kota/Poke-Search/src/pokemon_photos"
        
        self.image_paths = []
        self.pokemon_names = []

        for image_name in os.listdir(folder_dir):
            if image_name.endswith(".jpg"):
                image_path = os.path.join(folder_dir, image_name)
                self.image_paths.append(image_path)
                self.pokemon_names.append(image_name[:-4])
        
        self.image_index = 0
        self.show_pokemon()
        



        next_button = QPushButton("next", self)
        next_button.setGeometry(50, 300, 160, 43)
        next_button.clicked.connect(self.next_button) #connecting button to a function
        
        
        previous_button = QPushButton("previous", self)
        previous_button.setGeometry(50, 350, 160, 43)
        previous_button.clicked.connect(self.previous_button)

    def previous_button(self):
        if self.image_index == 0:
            self.image_index = len(self.image_paths) - 1
        else:
            self.image_index -= 1
        self.show_pokemon()

    def next_button(self):
        if self.image_index == len(self.image_paths) - 1:
            self.image_index = 0
        else:
            self.image_index += 1
        self.show_pokemon()

    def show_pokemon(self):
        pixmap = QPixmap(self.image_paths[self.image_index])
        self.label2.setPixmap(pixmap)
        self.label1.setText(self.pokemon_names[self.image_index])



if __name__ == "__main__":
    app = QApplication([])
    window = NewWindow()
    window.show()
    app.exec()
