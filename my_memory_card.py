#подключение библиотек
schore = 1
from random import shuffle,randint
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QRadioButton, QLabel, QVBoxLayout, QHBoxLayout, QGroupBox,QPushButton,QButtonGroup

app = QApplication([]) 
main = QWidget()


class Question():
    def __init__(
     self, question, right_answer, 
     wrong1, wrong2, wrong3):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3

question_list = []
question_list.append(Question('Как зовут хоббита из властелина колец?','Бильбо','Смог','Хоби','Доби' ))
question_list.append(Question('Как зовут дракона из властелина колец?','Смог','Бильбо','Хоби','Доби' ))
question_list.append(Question('Как зовут мага из властелина колец?','Гэндальф','Смог','Хоби','Доби' ))
question_list.append(Question('Как зовут брата Кили из властелина колец?','Фили','Смог','Хоби','Доби' ))
question_list.append(Question('Сколько гномов пошло в поход из властелина колец?','13','1','14','15' ))
question_list.append(Question('Сколько фильмов про хобита вышло?','3','13','1','2' ))
question_list.append(Question('Сколько колец сушествует во вселенной властелина колец?','7','13','бесконечно','3' ))
question_list.append(Question('Как зовут "дубощита" в фильме про хобита?','Торин','Смог','Глоин','Траин' ))
question_list.append(Question('Где живет хобит из властелина колец?','в норе','в горе','в дворце','в Эсгарде' ))


hbox1 = QHBoxLayout()
hbox2 = QHBoxLayout()
hbox3 = QHBoxLayout()
vbox = QVBoxLayout()
lb_Question = QLabel("")
hbox1.addWidget(lb_Question, alignment=(Qt.AlignHCenter | Qt.AlignVCenter))
btn_OK = QPushButton('ответить')
RadioGroupBox = QGroupBox("Варианты ответов")
ansGroup = QGroupBox('Результат')
hbox_ans = QVBoxLayout()
lb_result = QLabel()
lb_correct = QLabel()

hbox_ans.addWidget(lb_result)
hbox_ans.addWidget(lb_correct)
ansGroup.setLayout(hbox_ans)

rbtn_1 = QRadioButton('Хоби')
rbtn_2 = QRadioButton('Бильбо')
rbtn_3 = QRadioButton('Смог')
rbtn_4 = QRadioButton('Доби')
layout_ans1 = QHBoxLayout()
layout_ans2 = QVBoxLayout()
layout_ans3 = QVBoxLayout()
layout_ans2.addWidget(rbtn_1)
layout_ans2.addWidget(rbtn_2)
layout_ans3.addWidget(rbtn_3)
layout_ans3.addWidget(rbtn_4)
layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3)
RadioGroupBox.setLayout(layout_ans1)

#создать вопроc 36
hbox2.addWidget(RadioGroupBox)
hbox2.addWidget(ansGroup)
ansGroup.hide()
layout_line3 = QHBoxLayout()
layout_line3.addStretch(1)
layout_line3.addWidget(btn_OK, stretch=2)
layout_line3.addStretch(1)
layout_card = QVBoxLayout()
layout_card.setSpacing(5)
layout_card.addLayout(hbox1)
layout_card.addLayout(hbox2)
layout_card.addLayout(layout_line3)


def ask(q: Question):
    shuffle(buttons)
    buttons[0].setText(q.right_answer)
    buttons[1].setText(q.wrong1)
    buttons[2].setText(q.wrong2)
    buttons[3].setText(q.wrong3)
    lb_Question.setText(q.question)
    lb_correct.setText(q.right_answer)

def check_answer():
    if buttons[0].isChecked():
        schore == schore + 1
        print("Правильных ответов:" )
        show_correct('Правильно')

        
    else:
        show_correct('Неправильно')



def start_test():
    if btn_OK.text() == 'ответить':
        show_result()
    else:
        show_question()
buttons = [rbtn_1,rbtn_2,rbtn_3,rbtn_4]


def show_correct(res):
    lb_correct.setText(res)
    show_result()


def show_result():
    RadioGroupBox.hide()
    ansGroup.show()
    btn_OK.setText('Следующий вопрос')

def show_question():
    ansGroup.hide()
    RadioGroupBox.show()
    RadioGroup = QButtonGroup()
    RadioGroup.addButton(rbtn_1)
    RadioGroup.addButton(rbtn_2)
    RadioGroup.addButton(rbtn_3)
    RadioGroup.addButton(rbtn_4)
    RadioGroup.setExclusive(False)
    rbtn_1.setChecked(False)
    rbtn_2.setChecked(False)
    rbtn_3.setChecked(False)
    rbtn_4.setChecked(False)
    RadioGroup.setExclusive(True)
    btn_OK.setText('Ответить')

def next_question():
    cur_question = randint(0,len(question_list)-1)
    ask(question_list[cur_question])
    show_question()

def click_ok():
    if btn_OK.text() == "Ответить":
        check_answer()
    else:
        next_question()

btn_OK.clicked.connect(click_ok)
next_question()
#отображение окна приложения 
main.setLayout(layout_card)
main.show()
app.exec_()








