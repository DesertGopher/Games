import PyQt5
from PyQt5 import *
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication
import random

Form, Window = uic.loadUiType("cards.ui")
Form2, Window2 = uic.loadUiType("rules.ui")
app = QApplication([])
window = Window()
window2 = Window2()
form = Form()
form2 = Form2()
form.setupUi(window)
form2.setupUi(window2)
window.show()

player_cards = []
computer_cards = []
player_count = 0
computer_count = 0
computer_points = int(0)
player_points = int(0)

def rules():
    window2.show()


def new_game():
    global player_points
    global computer_points
    computer_points = int(0)
    player_points = int(0)
    form.Player_count.setText(str(player_points))
    form.Computer_count.setText(str(player_points))
    form.rules.setDisabled(False)
    form.take_card.setDisabled(False)
    form.show_cards.setDisabled(False)
    form.next.setDisabled(True)
    global cards
    cards = ['Туз♢', '6♢', '7♢', '8♢', '9♢', '10♢', 'Валет♢', 'Дама♢', 'Король♢',
             'Туз♥', '6♥', '7♥', '8♥', '9♥', '10♥', 'Валет♥', 'Дама♥', 'Король♥',
             'Туз♤', '6♤', '7♤', '8♤', '9♤', '10♤', 'Валет♤', 'Дама♤', 'Король♤',
             'Туз♧', '6♧', '7♧', '8♧', '9♧', '10♧', 'Валет♧', 'Дама♧', 'Король♧']

    global player_cards
    player_cards = []
    global computer_cards
    computer_cards = []

    n = random.choice(cards)
    player_cards.append(n)
    cards.remove(n)
    n = random.choice(cards)
    player_cards.append(n)
    cards.remove(n)

    n = random.choice(cards)
    computer_cards.append(n)
    cards.remove(n)
    n = random.choice(cards)
    computer_cards.append(n)
    cards.remove(n)

    cards_str = str(player_cards)
    cards_str1 = cards_str.replace("'", "")
    cards_str2 = cards_str1.replace("]", "")
    cards_str3 = cards_str2.replace("[", "")
    print(cards_str3)
    form.label_3.setText(str(cards_str3))
    form.label_7.setText('')
    form.label_9.setText('')
    form.label_10.setText('')

def next():
    form.rules.setDisabled(False)
    form.take_card.setDisabled(False)
    form.show_cards.setDisabled(False)
    form.next.setDisabled(True)
    global cards
    cards = ['Туз♢', '6♢', '7♢', '8♢', '9♢', '10♢', 'Валет♢', 'Дама♢', 'Король♢',
             'Туз♥', '6♥', '7♥', '8♥', '9♥', '10♥', 'Валет♥', 'Дама♥', 'Король♥',
             'Туз♤', '6♤', '7♤', '8♤', '9♤', '10♤', 'Валет♤', 'Дама♤', 'Король♤',
             'Туз♧', '6♧', '7♧', '8♧', '9♧', '10♧', 'Валет♧', 'Дама♧', 'Король♧']

    global player_cards
    player_cards = []
    global computer_cards
    computer_cards = []

    n = random.choice(cards)
    player_cards.append(n)
    cards.remove(n)
    n = random.choice(cards)
    player_cards.append(n)
    cards.remove(n)

    n = random.choice(cards)
    computer_cards.append(n)
    cards.remove(n)
    n = random.choice(cards)
    computer_cards.append(n)
    cards.remove(n)

    cards_str = str(player_cards)
    cards_str1 = cards_str.replace("'", "")
    cards_str2 = cards_str1.replace("]", "")
    cards_str3 = cards_str2.replace("[", "")
    print(cards_str3)
    form.label_3.setText(str(cards_str3))
    form.label_7.setText('')
    form.label_9.setText('')
    form.label_10.setText('')


def take_card():
    n = random.choice(cards)
    player_cards.append(n)
    cards.remove(n)

    n = random.choice(cards)
    computer_cards.append(n)
    cards.remove(n)

    cards_str = str(player_cards)
    cards_str1 = cards_str.replace("'", "")
    cards_str2 = cards_str1.replace("]", "")
    cards_str3 = cards_str2.replace("[", "")
    print(cards_str3)
    form.label_3.setText(str(cards_str3))
    if len(player_cards) == 5:
        form.take_card.setEnabled(False)

def show_cards():
    global player_points
    global computer_points

    if 'Туз♢' in player_cards:
        player_cards.remove('Туз♢')
        player_cards.append(11)
    if 'Туз♥' in player_cards:
        player_cards.remove('Туз♥')
        player_cards.append(11)
    if 'Туз♤' in player_cards:
        player_cards.remove('Туз♤')
        player_cards.append(11)
    if 'Туз♧' in player_cards:
        player_cards.remove('Туз♧')
        player_cards.append(11)

    if 'Король♢' in player_cards:
        player_cards.remove('Король♢')
        player_cards.append(4)
    if 'Король♥' in player_cards:
        player_cards.remove('Король♥')
        player_cards.append(4)
    if 'Король♤' in player_cards:
        player_cards.remove('Король♤')
        player_cards.append(4)
    if 'Король♧' in player_cards:
        player_cards.remove('Король♧')
        player_cards.append(4)

    if 'Дама♢' in player_cards:
        player_cards.remove('Дама♢')
        player_cards.append(3)
    if 'Дама♥' in player_cards:
        player_cards.remove('Дама♥')
        player_cards.append(3)
    if 'Дама♤' in player_cards:
        player_cards.remove('Дама♤')
        player_cards.append(3)
    if 'Дама♧' in player_cards:
        player_cards.remove('Дама♧')
        player_cards.append(3)

    if 'Валет♢' in player_cards:
        player_cards.remove('Валет♢')
        player_cards.append(2)
    if 'Валет♥' in player_cards:
        player_cards.remove('Валет♥')
        player_cards.append(2)
    if 'Валет♤' in player_cards:
        player_cards.remove('Валет♤')
        player_cards.append(2)
    if 'Валет♧' in player_cards:
        player_cards.remove('Валет♧')
        player_cards.append(2)

    if '10♢' in player_cards:
        player_cards.remove('10♢')
        player_cards.append(10)
    if '10♥' in player_cards:
        player_cards.remove('10♥')
        player_cards.append(10)
    if '10♤' in player_cards:
        player_cards.remove('10♤')
        player_cards.append(10)
    if '10♧' in player_cards:
        player_cards.remove('10♧')
        player_cards.append(10)

    if '9♢' in player_cards:
        player_cards.remove('9♢')
        player_cards.append(9)
    if '9♥' in player_cards:
        player_cards.remove('9♥')
        player_cards.append(9)
    if '9♤' in player_cards:
        player_cards.remove('9♤')
        player_cards.append(9)
    if '9♧' in player_cards:
        player_cards.remove('9♧')
        player_cards.append(9)

    if '8♢' in player_cards:
        player_cards.remove('8♢')
        player_cards.append(8)
    if '8♥' in player_cards:
        player_cards.remove('8♥')
        player_cards.append(8)
    if '8♤' in player_cards:
        player_cards.remove('8♤')
        player_cards.append(8)
    if '8♧' in player_cards:
        player_cards.remove('8♧')
        player_cards.append(8)

    if '7♢' in player_cards:
        player_cards.remove('7♢')
        player_cards.append(7)
    if '7♥' in player_cards:
        player_cards.remove('7♥')
        player_cards.append(7)
    if '7♤' in player_cards:
        player_cards.remove('7♤')
        player_cards.append(7)
    if '7♧' in player_cards:
        player_cards.remove('7♧')
        player_cards.append(7)

    if '6♢' in player_cards:
        player_cards.remove('6♢')
        player_cards.append(6)
    if '6♥' in player_cards:
        player_cards.remove('6♥')
        player_cards.append(6)
    if '6♤' in player_cards:
        player_cards.remove('6♤')
        player_cards.append(6)
    if '6♧' in player_cards:
        player_cards.remove('6♧')
        player_cards.append(6)

    player_count = int(sum(player_cards))
    form.label_9.setText("Счет: " + str(player_count))
    computer_count = int(random.uniform(16, 24))
    form.label_10.setText("Счет: " + str(computer_count))

    if player_count < 22 and computer_count < 22:
        if player_count > computer_count:
            form.label_7.setText('VICTORY')
            player_points = player_points + 1
            form.Player_count.setText(str(player_points))
        elif computer_count > player_count:
            form.label_7.setText('LOSE')
            computer_points = computer_points + 1
            form.Computer_count.setText(str(computer_points))
    elif computer_count > 21 and player_count <= 21:
        form.label_7.setText('VICTORY')
        player_points = player_points + 1
        form.Player_count.setText(str(player_points))
    elif player_count > 21 and computer_count <= 21:
        form.label_7.setText('LOSE')
        computer_points = computer_points + 1
        form.Computer_count.setText(str(computer_points))
    elif player_count > 21 and computer_count > 21:
        form.label_7.setText('DRAW')
    elif computer_count == player_count:
        form.label_7.setText('DRAW')

    sub()


def sub():
    form.next.setDisabled(False)
    form.rules.setDisabled(True)
    form.take_card.setDisabled(True)
    form.show_cards.setDisabled(True)


form.rules.clicked.connect(rules)
form.next.setDisabled(True)
form.rules.setDisabled(True)
form.take_card.setDisabled(True)
form.show_cards.setDisabled(True)
form.action.triggered.connect(new_game)
form.next.clicked.connect(next)
form.take_card.clicked.connect(take_card)
form.show_cards.clicked.connect(show_cards)
app.exec_()
