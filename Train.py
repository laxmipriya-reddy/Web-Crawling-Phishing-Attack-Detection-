import sys
import pandas as pd
from sklearn.pipeline import Pipeline
import numpy as np
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import classification_report, f1_score, accuracy_score, confusion_matrix
import pickle

from PyQt5 import QtCore, QtGui, QtWidgets
from DBConnection import DBConnection
from sklearn.neural_network import MLPClassifier

import sys
import time
from sklearn import metrics
from sklearn.ensemble import RandomForestClassifier


class Train:

    def detecting():

        try:
            fn = [1, 0, 0, 1, 0, 0, 1, 1, 1, 0]
            # list=[f1,f2,f3,f4,f5,f6,f8,f9,f10,f15]

            trainset = []
            database = DBConnection.getConnection()
            cursor = database.cursor()
            cursor.execute(
                "select * from dataset ")
            row = cursor.fetchall()
            y_train = []
            trainset.clear()
            y_train.clear()
            train = len(row)
            for r in row:
                x_train = []
                x_train.clear()
                x_train.append(float(r[0]))
                x_train.append(float(r[1]))
                x_train.append(float(r[3]))
                x_train.append(float(r[1]))
                x_train.append(float(r[1]))
                x_train.append(float(r[6]))
                x_train.append(float(r[7]))
                x_train.append(float(r[8]))
                x_train.append(float(r[9]))
                x_train.append(float(r[14]))
                y_train.append(r[28])
                trainset.append(x_train)
            print("y=", y_train)
            # print("trd=", trainset)
            trainset = np.array(trainset)
            print("trd=", trainset)
            y_train = np.array(y_train)
            elm = MLPClassifier()

            filename = 'elm_model.sav'
            pickle.dump(elm.fit(trainset, y_train),open(filename, 'wb'))


        except Exception as e:
            print("Error=" + e.args[0])
            tb = sys.exc_info()[2]
            print(tb.tb_lineno)


if __name__ == "__main__":
    Train.detecting()

