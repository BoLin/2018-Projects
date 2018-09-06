import numpy as np
import scipy
import matplotlib
from sklearn.neural_network import MLPClassifier
import dataloader

X, Y = dataloader.test()
clf = MLPClassifier(solver='adam', alpha=1e-5, hidden_layer_sizes=(l, k, j, i), random_state=1)
clf.fit(X, Y)
Y_predict = clf.predict(X)
Y_predict = Y_predict.tolist()

for i in range(len(Y[0])):
    correct = 0
    wrong = 0
    for j in range(len(Y)):
        if Y[j][i] == Y_predict[j][i]:
            correct += 1
        else:
            wrong += 1
    print(i)
    print(correct/(correct + wronng))
    print("================")
