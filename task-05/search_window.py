
from PySide6.QtWidgets import QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QDialog, QMessageBox
from PySide6.QtGui import QPixmap,QMovie
from PySide6.QtCore import  QRect, Qt, QDir
import requests 
from PIL import Image 
import os
from new_window import NewWindow

class SearchWindow(QWidget):
    """
    This "window" is a QWidget. If it has no parent, it
    will appear as a free-floating window as we want.
    """
    def __init__(self):
        super().__init__()
       
        self.w = None        
        #self.setFixedSize(850, 500)
        self.textbox = QLineEdit(self)
        self.textbox.move(20, 20) 
        self.textbox.setGeometry(50, 70, 280, 40)
      
        
        label1 = QLabel("Enter the name", self)
        label1.setGeometry(50, 5, 600, 70)

        self.label2 = QLabel(self) #i will use this as variable to display the data that i gather later on
        self.label2.setWordWrap(True)
        self.label2.setStyleSheet("color: white; font-size: 18px;")
        self.label2.setGeometry(550, 150, 400, 300)

        enter_button = QPushButton("Search", self)
        enter_button.setGeometry(50, 300, 160, 43)
        enter_button.clicked.connect(self.api_integration) #connecting button to a function
        
        
        capture_button = QPushButton("Capture", self)
        capture_button.setGeometry(50, 350, 160, 43)
        capture_button.clicked.connect(self.poke_capture)


        display_button = QPushButton("Display", self)
        display_button.setGeometry(50, 400, 160, 43)
        display_button.clicked.connect(self.open_search_window)



        self.setStyleSheet("""
            QPushButton {
                background-color: dark-grey;
                color: white;
                border: 1px solid #BA263E;
                font: bold 16px;
                text-align: center;
                border-radius: 10px;
            }
            QMessageBox QLabel {
                color: white;
                border: 10px solid #BA263E;
                background-color: dark-grey;
                width:200px;
                height: 200px;
                border-radius: 10px;    
            
            }
            QMainWindow {
                background-color: black;
            }
            SearchWindow {
                background-color: black;
            }
            QLabel {
                font-size: 32px;
                color:white;
                font: bold;
            }
            QPushButton:hover {
                background-color: #BA263E;
                color: dark-grey;
            }
        """)

    # 1 #
    # Fetch the data from from the API.
    # Display the name, official artwork (image), abilities, types and stats when queried with a Pokémon name.
    # Add the background provided in assets



        #labelmov = QLabel(self)      i used this initially, but then realised it is stupid and had to change the script...
        #labelmov.setScaledContents(True)
        #movie = QMovie("../assets/landing.jpg")
        #labelmov.setGeometry(QRect(0, 0, 900,478))
        #labelmov.setMovie(movie)
        #movie.start()
        #labelmov.lower()
        self.image_label = QLabel()
        self.image_label.setPixmap(QPixmap("../assets/landing.jpg"))
        self.image_label.setScaledContents(True)
        layout = QVBoxLayout()
        layout.addWidget(self.image_label)
        self.setLayout(layout)
        self.image_label.lower()

    def api_integration(self):

        pokemon_name = self.textbox.text().lower()

        url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name}"
        response = requests.get(url)
        if response.status_code == 200:
            pokemon_data = response.json()
            #print(pokemon_data)
            required_pokemon_info = f"""
                Name     : {pokemon_data["name"]}
                Abilities: {', '.join([i["ability"]["name"] for i in pokemon_data["abilities"]])}
                Types    : {', '.join([j["type"]["name"] for j in pokemon_data["types"]])}
                
                Stats:-
                hp       : {pokemon_data["stats"][0]["base_stat"]}
                attack   : {pokemon_data["stats"][1]["base_stat"]}
                defense  : {pokemon_data["stats"][2]["base_stat"]}
                special-attack  : {pokemon_data["stats"][3]["base_stat"]}
                special-defense : {pokemon_data["stats"][4]["base_stat"]}
                Speed    : {pokemon_data["stats"][5]["base_stat"]}"""
            print(required_pokemon_info)
            pokemon_id = pokemon_data["id"]
            image_url = f'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/{pokemon_id}.png'
            print(image_url)
            self.label2.setText(required_pokemon_info)

            display_image = requests.get(image_url).content
            pixmap = QPixmap()
            pixmap.loadFromData(display_image)
            self.image_label.setPixmap(pixmap)

            #return required_pokemon_info, image_url, display_image, pokemon_name
        else:
            print(f'{response.status_code} error')
            self.label2.setText("No Pokemon found with the given name.")
            

    # 2 #
    # Capture the Pokémon i.e. download the image.

    def poke_capture(self):
        pokemon_name = self.textbox.text().lower()
        url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name}"
        response = requests.get(url)
        
        if response.status_code == 200:
            pokemon_data = response.json()
            pokemon_id = pokemon_data["id"]
            image_url = f'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/{pokemon_id}.png'
            image_data = requests.get(image_url).content
            
            folder_path = 'pokemon_photos' #helpful for part-03
            if not os.path.exists(folder_path):
                os.makedirs(folder_path)

            f = open(os.path.join(folder_path, f'{pokemon_name}.jpg'), 'wb')
            f.write(image_data)
            f.close()
            print('done')

            dlg = QMessageBox(self)
            dlg.setWindowTitle("pokemon")
            dlg.setText("Captured!")
            capture_button = dlg.exec()

            if capture_button == QMessageBox.Ok:
                print("OK!")

        else:
            print(response.status_code)
        



    # 3 #
    # Display all the Pokémon captured with their respective names using a new window.
    def open_search_window(self):
        if self.w is None:
            self.w = NewWindow()
        self.w.show()

if __name__ == "__main__":
    import sys
    from PySide6.QtWidgets import QApplication

    app = QApplication(sys.argv)
    window = SearchWindow()
    window.show()
    sys.exit(app.exec())