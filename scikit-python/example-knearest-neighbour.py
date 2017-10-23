import pandas as pd;
from sklearn import neighbors
import numpy as np

# training_data = pd.DataFrame()

# training_data['test_1'] = [0.3051, 0.4949, 0.6974, 0.3769, 0.2231, 0.341, 0.4436, 0.5897, 0.6308, 0.5]
# training_data['test_2'] = [0.5846, 0.2654, 0.2615, 0.4538, 0.4615, 0.8308, 0.4962, 0.3269, 0.5346, 0.6731]
# training_data['outcome'] = ['win', 'win', 'win', 'win', 'win', 'loss', 'loss', 'loss', 'loss', 'loss']

# X = training_data.as_matrix(columns=['test_1', 'test_2'])
# y = np.array(training_data['outcome'])

# clf_weight = neighbors.KNeighborsClassifier(3, weights='uniform')
# clf_distance = neighbors.KNeighborsClassifier(3, weights='distance')

# trained_model_weight = clf_weight.fit(X, y)
# trained_model_distance = clf_distance.fit(X, y)

# print trained_model_weight.score(X, y)
# print trained_model_distance.score(X, y)

# x_test = np.array([[.4,.6]])

# print trained_model_weight.predict(x_test)
# print trained_model_weight.predict_proba(x_test)

############################################################################################################################
training_data = pd.DataFrame()

training_data['hour'] = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15 , 16 , 17 , 18, 19, 20, 21, 22, 23];
training_data['count'] = [34, 57, 127, 85, 49, 3, 77, 37, 91, 55, 22, 88, 12, 9, 0, 44, 65, 2, 58, 6, 33, 49, 61, 27];
training_data['status'] = ['unnormal', 'unnormal', 'unnormal', 'unnormal', 'unnormal', 'unnormal', 'unnormal', 'unnormal'
, 'normal', 'normal', 'normal', 'normal', 'normal', 'normal', 'normal', 'normal', 'normal', 'normal'
, 'unnormal', 'unnormal', 'unnormal', 'unnormal', 'unnormal', 'unnormal'];

X = training_data.as_matrix(columns=['hour', 'count']);
y = np.array(training_data['status']);

trained_model = neighbors.KNeighborsClassifier(3, weights='distance').fit(X, y);

x_test = np.array([[4.3, 90]]);
print trained_model.predict(x_test);
print trained_model.predict_proba(x_test);
