"""
#/#######################\#
        MrDaniLLka
#\#######################/#
"""
from PyQt5 import QtWidgets, QtCore, QtGui
from functools import partial
from decimal import Decimal
import numpy as np
import matplotlib.pyplot as plt
import math
import random
import time
import re
import os


class MyWindow(QtWidgets.QWidget):

    
    def keyPressEvent(self, event):
        '''
        #dictonary for button press 
        keys = {}
        for key, value in vars(QtCore.Qt).items():
            if isinstance(value, QtCore.Qt.Key):
                keys[value] = key
        print(keys[event.key()])
        print(event.key())
        '''
        if str(event.key()) in self.dictionary:
            self.CheckDisplay(self.dictionary[str(event.key())])


    def DialogRandom(self, name):
        self.numbersRD = [0,1,1]
        __listDR = ['Start','Stop','Step']
        self.dialogRandom = QtWidgets.QDialog()
        self.dialogRandom.setWindowFlags(QtCore.Qt.WindowCloseButtonHint)
        self.dialogRandom.setWindowTitle(name)
        self.dialogRandom.setWindowIcon(self.image)
        vboxd = QtWidgets.QVBoxLayout()
        hboxd = QtWidgets.QHBoxLayout()
        for element in range(3):
                label =  QtWidgets.QLabel(f'{__listDR[element]}', self)
                hboxd.addWidget(label)
            
        vboxd.addLayout(hboxd)
        hboxd = QtWidgets.QHBoxLayout()

        self.startline = QtWidgets.QLineEdit('0', self)
        self.stopline = QtWidgets.QLineEdit('1', self)
        self.stepline = QtWidgets.QLineEdit('1', self)

        i = 0
        for line in self.startline, self.stopline, self.stepline:
            line.setValidator(QtGui.QIntValidator())
            line.textEdited.connect(partial(self.ChangelineRandom, __listDR[i]))
            i += 1
            hboxd.addWidget(line)

            
        vboxd.addLayout(hboxd)
        self.buttond = QtWidgets.QPushButton('Result!')
        self.buttond.clicked.connect(self.ClickedRandomButton)
        vboxd.addWidget(self.buttond)
        self.dialogRandom.setLayout(vboxd)
        return self.dialogRandom.exec()

    
    def ChangelineRandom(self, name, number):
        if name == 'Start':
            self.numbersRD[0] = number
        if name == 'Stop':
            self.numbersRD[1] = number
        if name == 'Step':
            self.numbersRD[2] = number

            
    def ClickedRandomButton(self):
        if len(str(self.numbersRD[0])) == 0:
            self.numbersRD[0] = 0
            self.startline.setText(str(self.numbersRD[0]))
        
        if len(str(self.numbersRD[1])) == 0:
            self.numbersRD[1] = 1
            self.stopline.setText(str(self.numbersRD[1]))
        if len(str(self.numbersRD[2])) == 0:
            self.numbersRD[2] = 1
            self.stepline.setText(str(self.numbersRD[2]))
        start = int(self.numbersRD[0])
        stop = int(self.numbersRD[1])
        step = int(self.numbersRD[2])
        try:
            number = str(random.randrange(start, stop+1, step))
            self.buttond.setText("Random number = " + number)
            self.display.display(number)
        except ValueError:
            pass

    def DialogProgrammer(self, name):
        self.dialogProgrammer = QtWidgets.QDialog()
        self.dialogProgrammer.setWindowTitle(name)
        self.dialogProgrammer.setWindowIcon(self.image)
        self.dialogProgrammer.setWindowFlags(QtCore.Qt.WindowCloseButtonHint)
        
        self.lineProgram = QtWidgets.QLineEdit('0')
        self.lineProgram.returnPressed.connect(self.ChangeProgrammer)
        self.lineProgram.setInputMask('>nnnnnnnn')
        
        self.displayProgram = QtWidgets.QLineEdit('0')
        self.displayProgram.setReadOnly(True)
        
        self.spinLineProgram = QtWidgets.QSpinBox()
        self.spinLineProgram.editingFinished.connect(self.ChangeProgrammer)
        self.spinLineProgram.setRange(2, 36)
        
        self.spinDisplayProgram = QtWidgets.QSpinBox()
        self.spinDisplayProgram.editingFinished.connect(self.ChangeProgrammer)
        self.spinDisplayProgram.setRange(2, 36)
        
        self.labelProrgam = QtWidgets.QLabel('change the number system to')
        
        vbox = QtWidgets.QVBoxLayout()
        hbox = QtWidgets.QHBoxLayout()
        hbox.addWidget(self.lineProgram)
        hbox.addWidget(self.displayProgram)

        vbox.addLayout(hbox)
        hbox = QtWidgets.QHBoxLayout()
        
        hbox.addWidget(self.spinLineProgram)
        hbox.addWidget(self.labelProrgam)
        hbox.addWidget(self.spinDisplayProgram)
        vbox.addLayout(hbox)
      
        self.dialogProgrammer.setLayout(vbox)
        return self.dialogProgrammer.exec()

    def ChangeProgrammer(self):
        numberOne = str(self.lineProgram.text())
        systemOne = int(self.spinLineProgram.text())
        systemTwo = int(self.spinDisplayProgram.text())
        try:
            numberTwo = int(numberOne, systemOne)
        except ValueError:
            self.displayProgram.setText('Error')
            return
        systemNumber = ["0","1","2","3","4","5","6","7",
             "8","9","A","B","C","D","E","F",
             "G","H","I","J","K","L","M","N",
             "O","P","Q","R","S","T","U","V",
             "W","X","Y","Z"]
        systemOne = numberTwo
        listNum = []
        strNum = ''
        while systemOne > 0:
            listNum.append(str(systemOne % systemTwo))
            systemOne //= systemTwo
        if numberTwo == 0:
            self.displayProgram.setText('0')
        if numberTwo > 0:
            for i in listNum:
                strNum += systemNumber[int(i)]
            self.displayProgram.setText(strNum[::-1])
            
        


    def CheckCombobox(self, index):
        nt = self.combobox.currentText()
        ct = self.label.toPlainText()
        if nt == 'Save':
            t = time.localtime()
            with open(f'Saved files\\Time({t[3]}h.{t[4]}m) Date({t[2]}.{t[1]}.{t[0]}).txt','w') as file:
                d = ["понедельник","вторник","среда","четверг","пятница","суббота","воскресенье"]
                m = ["января","февраля","марта","апреля","мая","июня","июля","августа","сентября","октября","ноября","декабря"]
                file.write(("Дата запуска: %02d.%02d.%02d \n%s %s %s %s\nВремя запуска: %02d:%02d:%02d\n")%
                  (t[2],t[1],t[0],d[t[6]],t[2],m[t[1]-1],t[0],t[3],t[4],t[5]))
                if len(ct):
                    file.write('\n'+ct)
                else:
                    file.write('\n'+'Empty')
                self.dialogSave.exec()
        if nt == 'Randomizer':
            self.DialogRandom(nt)
        if nt == 'Programmer':
            self.DialogProgrammer(nt)
            
    def Error(self, l):
        for i in range(l):
            self.CheckDisplay('CE')
        dialogError = QtWidgets.QMessageBox(QtWidgets.QMessageBox.Information,
                                                         'Error',
                                                         'Неверный ввод.',
                                                         QtWidgets.QMessageBox.Ok)
        dialogError.setWindowIcon(self.image)
        return dialogError.exec()
    
    def CheckDisplay(self, nt):
        ct = self.label.toPlainText()#calculator text / new text
        number = re.compile(r"((\b|(?=\W))(\d+(\.\d*)?|\.\d+)([eE][+-]?\d{1,3})?)")
        deciexpr = lambda s: number.sub(r"Decimal('\1')", s)


        if nt in self.specialSymbols1:
            if len(ct) == 0:
                ct += nt
                self.label.setText(ct)
            elif ct[-1] in self.specialSymbols1:
                    ct = ct[0:len(ct)-1]
                    ct += nt
                    self.label.setText(ct)
            else:
                ct += nt
                self.label.setText(ct)


        if nt in self.specialSymbols2:
            if len(ct) != 0:
                if ct[-1] not in self.specialSymbols1:
                    if ct[-1]  in self.specialSymbols2:
                        ct = ct[0:len(ct)-1]
                        ct += nt
                        self.label.setText(ct)
                    else:
                        ct += nt
                        self.label.setText(ct)


        if str(nt).isdigit():
            if len(ct) == 0:
                self.label.setText('+'+str(nt))
            elif ct[-1] in self.specialSymbols2:
                self.label.setText(ct+'+'+str(nt))
            elif ct[-1] == '(':
                self.label.setText(str(ct) + "+" + str(nt))
            else:
                self.label.setText(str(ct) + str(nt))

                
        if nt == '=' or nt == '!=':
            while ct.count('(') != ct.count(')'):
                ct += ')'
            ct = ct.replace('^','**')
            try:
                answer0 = ct.split('\n')[-1]
                if 'E' in str(eval(deciexpr(answer0))):
                    self.Error(len(ct))
                    return
                answer = eval(deciexpr(answer0))
            except BaseException as e:
                print(e)
                self.Error(len(ct))
                return
            if nt == '!=':
                return answer
            if str(answer) == answer0 or ('+' + str(answer)) == answer0:
                return
            if answer > 0:
                self.label.setText(str(ct)+'\n'+'+'+str(answer))
            else:
                self.label.setText(str(ct)+'\n'+str(answer))
            if len(str(answer)) > 6:
                self.display.display(str(answer)[0:6]+'..')
            else:
                self.display.display(str(answer))

        
        if nt in ['(',')']:
            if nt == '(':
                if len(ct) == 0:
                    ct += nt
                    self.label.setText(ct)
                elif not ct[-1].isdigit() and ct[-1] != ')' and ct[-1] != '.':
                    ct += nt
                    self.label.setText(ct)
            if nt == ')':
                if ct.count('(') > ct.count(')'):
                    if ct[-1] not in (self.specialSymbols + ['.']) and ct.rpartition('(')[2] != '':
                        ct += nt
                        self.label.setText(ct)

                        
        if nt == 'П':
            self.label.setText(str(ct)+'+'+str(np.pi))
           
        if nt == 'CE':
            try:
                if ct[len(ct)-1] != '\n':
                    ct = ct[0:len(ct)-1]
                    self.label.setText(ct)
            except BaseException as e:
                pass

            
        if nt == '&C':
            self.label.clear()
            
        if nt == '+/-' and len(ct) > 0:
            if ct[-1] not in self.specialSymbols:
                ct1 = ''
                for d in ct:
                    if d.isdigit() or d in ['(',')','.']:
                        if  d in ['(',')']:
                            continue
                        ct1 += d
                    else:
                        ct1 = ''
                
                symbol = ct[ct.rfind(ct1)-1]
                ct = ct[0:ct.rfind(ct1)-1]
                if symbol in ['+','-']:
                    ct1 = float(symbol+str(ct1)) * (-1)
                    if ct1 >= 0: 
                        self.label.setText(str(ct)+'+'+str(ct1))
                    else:
                        self.label.setText(str(ct) + str(ct1))

                        
        if nt == '!':
            try:
                ct1 = self.CheckDisplay('!=')
                self.label.setText(str(ct)+'\n'+'+'+str(math.factorial(ct1)))
            except BaseException as e:
                self.Error(len(ct))
                pass
            
        if nt == '.' and len(ct) != 0:
            if ct[-1].isdigit():
                ct1 = ''
                for d in ct:
                    if d.isdigit() or d == '.':
                        ct1 += d
                    else:
                        ct1 = ''
                if ct1.count('.') == 0:
                    ct += nt
                    self.label.setText(str(ct))
        if nt in self.graph :
            try:
                answer = float(self.CheckDisplay('!='))
                self.DrawGraphiks(answer, nt)
            except BaseException as e:
                pass
            

    def DrawGraphiks(self, x1, func):
        try:
            x2 = x1
            if func == 'sin(x)':
                print(x1)
                print(round(np.sin(x1),5))
                x = np.linspace(0, 2.0*np.pi, 101)
                y = np.sin(x)
                y1 = round(np.sin(x1),5)
                plt.plot(x, y)
                answer = y1
            if func == 'cos(x)':
                x = np.linspace(0, 2.0*np.pi, 101)
                y = np.cos(x)
                y1 = round(np.cos(x1), 5)
                plt.plot(x, y)
                answer = y1
            if func == 'tan(x)':
                x = np.linspace(-2.0*np.pi, 2.0*np.pi, 101)
                y = np.tan(x)
                y[:-1][np.diff(y) < 0] = np.nan
                y1 = round(np.tan(x1), 5)
                plt.plot(x, y)
                plt.ylim(-5, 5)
                answer = y1
            if func == 'ctan(x)':
                x = np.linspace(-2.0*np.pi, 2.0*np.pi, 101)
                y = 1/np.tan(x)
                y[:-1][np.diff(y) > 0] = np.nan
                y1 = round(round(np.cos(x1), 5)/round(np.sin(x1), 5), 5)
                plt.plot(x, y)
                plt.ylim(-5, 5)
                answer = y1
            if x1 > 2.0*np.pi:
                x2 %= 2.0*np.pi
            
            plt.scatter(x2, y1, color='orange', s=40, marker='o')
            plt.show()
            dialog = QtWidgets.QMessageBox(QtWidgets.QMessageBox.Information,
                                                         'Answer',
                                                         f'x = {x1}\ny = {y1}',
                                                         QtWidgets.QMessageBox.Ok)
            dialog.setWindowIcon(self.image)
            if answer > 0:
                self.label.append('+'+str(answer))
                self.display.display(str(answer))
            elif answer <= 0:
                self.label.append(str(answer))
                self.display.display(str(answer))
            return dialog.exec()

    
        except BaseException as e:
            pass

    
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)

        self.path = os.makedirs('Saved files', exist_ok = True)
        
        self.setWindowTitle('Calculator')
        self.image = QtGui.QIcon(r'C:\Users\Danil\OneDrive\Рабочий стол\Бразильское\Projects\Calculator\Icon\Ico.ico')
        self.setWindowIcon(self.image)
        self.resize(500, 400)
        
        
        self.display = QtWidgets.QLCDNumber(8)
        self.hbox = QtWidgets.QHBoxLayout()
        self.vbox = QtWidgets.QVBoxLayout()
        self.label = QtWidgets.QTextEdit()
        
        self.label.setTextInteractionFlags(QtCore.Qt.TextSelectableByMouse)
        self.vbox.addWidget(self.label)


        self.specialSymbols1 = ['+','-']
        self.specialSymbols2 = ['*','/','^']
        self.graph = ['sin(x)','cos(x)','tan(x)','ctan(x)']
        self.specialSymbols = self.specialSymbols1 + self.specialSymbols2
        self.dictionary = {'43':'+','45':'-','48':0,'49':1,'50':2,'51':3,'52':4,'53':5,'54':6,'55':7,'56':8,'57':9,
                      '61':'=','94':'^','46':'.','47':'/','42':'*','40':'(','41':')','16777219':'CE'}
        self.numbers = [1,2,3,4,5,6,7,8,9,0]
        __list = ['display','CE','&C','П','...',
                  '^','(',')','+','cos(x)',
                  1,2,3,'-','sin(x)',
                  4,5,6,'/','tan(x)',
                  7,8,9,'*','ctan(x)',
                  '+/-',0,'.','!','=']

        
        

        self.dialogSave = QtWidgets.QMessageBox(QtWidgets.QMessageBox.Information,'Message','File saved')
        self.dialogSave.setWindowIcon(self.image)
        self.combobox = QtWidgets.QComboBox()
        self.combobox.addItems(('Save','Randomizer','Programmer'))




        i = 0
        for row in range(6):
            for column in range(5):
                if __list[i] == 'display':
                    self.hbox.addWidget(self.display)
                elif __list[i] == '...':
                    self.combobox.activated.connect(self.CheckCombobox)
                    self.hbox.addWidget(self.combobox)
                else:
                    button = QtWidgets.QPushButton(f'{__list[i]}', self)
                    button.clicked.connect(partial(self.CheckDisplay, __list[i]))
                    self.hbox.addWidget(button)
                i += 1
                if i == len(__list):
                    break
            self.vbox.addLayout(self.hbox)
            self.hbox = QtWidgets.QHBoxLayout()
            
        
        self.setLayout(self.vbox)
        self.show()


if __name__ ==  "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    sys.exit(app.exec_())
