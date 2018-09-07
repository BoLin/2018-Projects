import numpy as np
import scipy
import matplotlib
from sklearn.neural_network import MLPClassifier
from sklearn.externals import joblib
import dataloader

X, Y = dataloader.test()

max = 0
match = []
for i in range(10,60):
    for j in range(10,60):
        for k in range(10,60):
            for l in range(1,60):
                clf = MLPClassifier(solver = 'adam',alpha = 1e-5, hidden_layer_sizes = (i, j, k, l), random_state = 1)
                clf.fit(X,Y)
                Y = np.array(Y)
                if clf.score(X,Y) > max:
                    max = clf.score(X,Y)
                    match = [i,j,k,l]
                    print(max)
                    print([i, j, k, l])
                    print("============")

print(max)
print(match)
#save model
clf = MLPClassifier(solver = 'adam',alpha = 1e-5, hidden_layer_sizes = (match[0],match[1],match[2],match[3]), random_state = 1)
                clf.fit(X,Y)
joblib.dump(clf,"nn_train_model.m")
