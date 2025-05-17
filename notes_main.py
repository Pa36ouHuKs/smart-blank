#начни тут создавать приложение с умными заметками
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QTextEdit, QLabel, QListWidget, QLineEdit, QPushButton, QInputDialog
import json
def show_note():
    key = list_zametok.selectedItems()[0].text()
    text_zametki.setText(notes[key]['текст'])
    list_tegs.clear()
    list_tegs.addItems(notes[key]['теги'])
def add_note():
    notes_name, result = QInputDialog.getText(
        main_win, 'Создать новую заметку', 'Название заметки:'
    )
    if result:
        notes[notes_name] = {
            'текст': '',
            'теги': []
        }
        list_zametok.addItem(notes_name)
        with open('notes_data.json', 'w') as file:
            json.dump(notes, file, sort_keys=True, ensure_ascii=False)
def del_note():
    if list_zametok.selectedItems():
        key = list_zametok.selectedItems()[0].text()
        del notes[key]
        list_zametok.clear()
        list_zametok.addItems(notes)
        text_zametki.clear()
        list_tegs.clear()
        with open('notes_data.json', 'w') as file:
            json.dump(notes, file, sort_keys=True, ensure_ascii=False)
def save_note():
    if list_zametok.selectedItems():
        key = list_zametok.selectedItems()[0].text()
        text = text_zametki.toPlainText()
        notes[key]['текст'] = text
        with open('notes_data.json', 'w') as file:
            json.dump(notes, file, sort_keys=True, ensure_ascii=False)
def add_teg_def():
    if list_zametok.selectedItems():
        key = list_zametok.selectedItems()[0].text()
        tag = searcher_teg.text()
        if tag and not tag in notes[key]['теги']:
            notes[key]['теги'].append(tag)
            list_tegs.addItem(tag)
            searcher_teg.clear()
            with open('notes_data.json', 'w') as file:
                json.dump(notes, file, sort_keys=True, ensure_ascii=False)
def del_teg_def():
    if list_tegs.selectedItems():
        key = list_zametok.selectedItems()[0].text()
        teg = list_tegs.selectedItems()[0].text()
        notes[key]['теги'].remove(teg)
        list_tegs.clear()
        list_tegs.addItems(notes[key]['теги'])
        with open('notes_data.json', 'w') as file:
            json.dump(notes, file, sort_keys=True, ensure_ascii=False)
def search_teg_def():
    tag = searcher_teg.text()
    if tag and search_teg.text() == 'Искать заметки по тегу':
        notes_filtered = {}
        for key in notes:
            if tag in notes[key]['теги']:
                notes_filtered[key] = notes[key]
        text_zametki.clear()
        list_zametok.clear()
        list_tegs.clear()
        search_teg.setText('Сбросить поиск')
        list_zametok.addItems(notes_filtered)
    else:
        text_zametki.clear()
        list_zametok.clear()
        list_tegs.clear()
        searcher_teg.clear()
        list_zametok.addItems(notes)
        search_teg.setText('Искать заметки по тегу')
app = QApplication([])
main_win = QWidget()
main_win.setWindowTitle('Заметки')
main_win.resize(900, 600)
#2
#создание виджетов
list_zametok_label = QLabel('Список заметок')
create_zametka = QPushButton('Создать заметку')
remove_zametka = QPushButton('Удалить заметку')
save_zametka = QPushButton('Сохранить заметку')
list_tegs_label = QLabel('Список тегов')
add_teg = QPushButton('Добавить к заметке')
remove_teg = QPushButton('Открепить от заметки')
search_teg = QPushButton('Искать заметки по тегу')
text_zametki = QTextEdit()
list_zametok = QListWidget()
list_tegs = QListWidget()
searcher_teg = QLineEdit()
searcher_teg.setPlaceholderText('Здесь должен быть тег')

#создание лайаутов
H_Layout1_main = QHBoxLayout()
H_Layout2 = QHBoxLayout()
H_Layout3 = QHBoxLayout()
V_Layout1 = QVBoxLayout()
V_Layout2 = QVBoxLayout()
#добавление виджетов к лайаутам
H_Layout1_main.addLayout(V_Layout1)#лайауты
H_Layout1_main.addLayout(V_Layout2)#лайауты
V_Layout2.addWidget(list_zametok_label)#список заметок(текст)
V_Layout2.addWidget(list_zametok)#список заметок!!!
V_Layout2.addLayout(H_Layout2)#лайауты
H_Layout2.addWidget(create_zametka)#создать заметку
H_Layout2.addWidget(remove_zametka)#удалить заметку
V_Layout2.addWidget(save_zametka)#сохранить заметку
V_Layout1.addWidget(text_zametki)#текст заметки
V_Layout2.addWidget(list_tegs_label)#спиисок тегов(текст)
V_Layout2.addWidget(list_tegs)#спиисок тегов


V_Layout2.addWidget(searcher_teg)#введите тег
H_Layout3.addWidget(add_teg)#добавить тег к заметке
H_Layout3.addWidget(remove_teg)#открепить тег от заметки


V_Layout2.addLayout(H_Layout3)#лайауты
V_Layout2.addWidget(search_teg)#искать заметки по тегу



#закреп лайаутов к окну
main_win.setLayout(H_Layout1_main)
#1
with open('notes_data.json', 'r') as file:
    notes = json.load(file)
    list_zametok.addItems(notes)
list_zametok.itemClicked.connect(show_note)
create_zametka.clicked.connect(add_note)
remove_zametka.clicked.connect(del_note)
save_zametka.clicked.connect(save_note)
add_teg.clicked.connect(add_teg_def)
remove_teg.clicked.connect(del_teg_def)
search_teg.clicked.connect(search_teg_def)
#1
main_win.show()
app.exec()