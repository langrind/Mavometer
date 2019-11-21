#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""Table of Message Statistics"""
from PyQt5.QtWidgets import QWidget, QTableView, QVBoxLayout, QAbstractItemView
from PyQt5.QtCore    import Qt, QAbstractTableModel, QEvent
from PyQt5           import QtCore
from uqtie           import UqtWin
from mavometer       import MessageStats

import operator      # used for sorting
#import pdb

class MessageTableView(QTableView):

    def __init__(self, dataList, *args):
        QTableView.__init__(self, *args)

        self.header = ['Type', 'Received', 'Frequency', 'Bandwidth' ]
        self.setContentsMargins(0, 0, 0, 0)

        self.setSelectionMode(QAbstractItemView.SingleSelection)
        self.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.setSortingEnabled(True)

        self.update_model(dataList)

        self.clicked.connect(self.showSelection)
        self.clicked.connect(self.selectRow)
        #self.changeEvent.connect(self.on_change_event)

    def changeEvent(self, event):
        """When font changes, resize the rows and columns so things fit OK"""

        # Can't resize the window from here unless we kept a parent ref, but it's
        # better that way anyway, since many users will want to manually resize the window
        # Also, we might not be the only widget in the window

        # So anyway, just size the rows and columns
        if event.type() == QEvent.FontChange:
            self.resizeRowsToContents()
            self.resizeColumnsToContents()
            self.update()
        QTableView.changeEvent(self, event)

    def update_model(self, dataList):

        self.table_model = MessageTableModel(self, dataList, self.header)
        self.setModel(self.table_model)
        self.resizeRowsToContents()
        self.resizeColumnsToContents()
        self.update()

    def showSelection(self, item):
        cellContent = item.data()
        # print(cellContent)  # test
        #sf = "You clicked on {}".format(cellContent)
        # display in title bar for convenience
        #self.setWindowTitle(sf)

    def selectRow(self, index):
        # print("current row is %d", index.row())
        pass

class MessageTableModel(QAbstractTableModel):
    '''
    Most method names are inherited so they can't be changed
    '''
    def __init__(self, parent, mylist, header, *args):
        QAbstractTableModel.__init__(self, parent, *args)
        self.mylist = mylist
        self.header = header

    def setDataList(self, mylist):
        self.mylist = mylist
        self.layoutAboutToBeChanged.emit()
        self.dataChanged.emit(self.createIndex(0, 0), self.createIndex(self.rowCount(0), self.columnCount(0)))
        self.layoutChanged.emit()

    def rowCount(self, parent):
        return len(self.mylist)

    def columnCount(self, parent):
        if not self.mylist or len(self.mylist) == 0:
            return 0
        return len(self.mylist[0])

    def data(self, index, role):
        if not index.isValid():
            return None
        value = self.mylist[index.row()][index.column()]
        if role == QtCore.Qt.EditRole:
            return value
        elif role == QtCore.Qt.DisplayRole:
            return value
        elif role == QtCore.Qt.CheckStateRole:
            return None

    def headerData(self, col, orientation, role):
        if orientation == Qt.Horizontal and role == Qt.DisplayRole:
            return self.header[col]
        return None

    def sort(self, col, order):
        """sort table by given column number col"""
        self.layoutAboutToBeChanged.emit()
        self.mylist = sorted(self.mylist, key=operator.itemgetter(col))
        if order == Qt.DescendingOrder:
            self.mylist.reverse()
        self.layoutChanged.emit()

    def flags(self, index):
        if not index.isValid():
            return None
        return QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsSelectable

    def setData(self, index, value, role):
        if not index.isValid():
            return False
        # self.emit(SIGNAL("dataChanged(QModelIndex,QModelIndex)"), index, index)
        self.dataChanged.emit(index, index)
        return True


# TEST CODE
from uqtie           import UqtWin
from PyQt5.QtWidgets import QApplication

import sys

class TestAppMainWindow(UqtWin.MainWindow):

    def __init__(self, args, **kwargs ):
        super(TestAppMainWindow, self).__init__(args, **kwargs)
        self.setup_ui()
        self.show()

    def setup_ui(self):
        vbox = QVBoxLayout(self.centralWidget())
        vbox.setSpacing(0)
        vbox.setContentsMargins(0, 0, 0, 0)

        dataList = [ ]

        self.messageTableView = MessageTableView ( dataList )
        vbox.addWidget(self.messageTableView)
        QtCore.QTimer.singleShot(1500, self.after_show)

    def after_show(self):
        dataList = [
            ['0x3001', 0, '0x1000', '4096'],
            ['0x4002', 1, '0x1001', '4097'],
            ['0x5003', 2, '0x1002', '4098'],
            ['0x6004', 3, '0x1003', '4099'],
            ['0x7005', 4, '0x1004', '4100'],
        ]

        self.messageTableView.update_model(dataList)

if __name__ == '__main__':

    app = QApplication(sys.argv)

    mainw = TestAppMainWindow(sys.argv, app=app, organizationName='Craton', appName='MessageTableViewTest')

    sys.exit(app.exec_())
