import numpy as np
import scipy
import matplotlib
from sklearn.neural_network import MLPClassifier
from sklearn import svm
import dataloader

X, Y = dataloader.test()

#single class training
for k in range(len(Y[0])):
    Y_single = []
    for i in Y:
        Y_single.append(i[k])
    test = svm.SVC()
    #clf = MLPClassifier(solver='adam', alpha=1e-5, hidden_layer_sizes=(62,53,21,16), random_state=1)
    test.fit(X, Y_single)
    Y_predict = test.predict(X)
    correct = 0
    wrong = 0
    for j in range(len(Y_single)):
        if Y_single[j] != Y_predict[j]:
            wrong += 1
        else:
            correct +=1
    print(k)
    print(correct/(correct + wrong))
    print("=========")

