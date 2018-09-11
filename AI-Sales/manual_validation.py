import numpy as np
import scipy
import matplotlib
from sklearn.neural_network import MLPClassifier
from sklearn.svm import SVC
import dataloader
from sklearn.externals import joblib

local_path = "./Test_set/label_scene_4_train/" # trainning path
X, Y = dataloader.test(local_path)
#clf = SVC()
clf = MLPClassifier(solver='adam', alpha=1e-5, hidden_layer_sizes=(62,53,21,16), random_state=1)
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
    print(correct/(correct + wrong))
    print("================")
#save model
joblib.dump(clf,"nn_train_model_scene_4.m")
