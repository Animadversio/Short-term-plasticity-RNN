from parameters import *
import pyqtgraph as pg
from pyqtgraph.Qt import QtCore, QtGui
import model
import psutil
import sys
import os

global data
data = {
    'trials'    : [],
    'accuracy'  : []
}

def update(data_to_add):
    data['trials'].append(data_to_add['trial'])
    data['accuracy'].append(data_to_add['accuracy'])

    curve1.setData(x=data['trials'], y=data['accuracy'])
    app.processEvents()

def switch(iteration, prev_switch_iteration, savename):
    if iteration == (prev_switch_iteration + 10):
        if par['allowed_categories'] == [0]:
            par['allowed_categories'] = [1]
            print("Switching to category 1.\n")
            with open(savename, 'a') as f:
                f.write('Switching to category 1.\n')
            return iteration
        elif par['allowed_categories'] == [1]:
            par['allowed_categories'] = [0]
            print("Switching to category 0.\n")
            with open(savename, 'a') as f:
                f.write('Switching to category 0.\n')
            return iteration
        else:
            print("ERROR: Bad category.")
            quit()
    else:
        return prev_switch_iteration

def stop():
    sys.exit()

def start():
    par['df_num'] = '0004'
    model.main(switch, update)

app = QtGui.QApplication([])
w   = pg.GraphicsWindow()

w.setWindowTitle('Realtime Network Behavior!')

btn = QtGui.QPushButton('Start')
btn2 = QtGui.QPushButton('Quit')
txt = QtGui.QLabel('A Title, Perhaps')
txt.setStyleSheet("QLabel { color : white; }")
p1  = pg.PlotWidget()

layout = QtGui.QGridLayout()
w.setLayout(layout)

layout.addWidget(btn, 0, 0)
layout.addWidget(btn2, 1, 0)
layout.addWidget(txt, 0, 1)
layout.addWidget(p1, 1, 1)

w.show()

curve1 = p1.plot(x=trials, y=accuracy_array)

btn.clicked.connect(start)
btn2.clicked.connect(stop)

app.exec_()
