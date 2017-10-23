import pandas as pd;
import numpy as np
import pydotplus
from sklearn import tree

# features = [[140,1],[130,1],[150,0],[170,0]]
# labels = [0,0,1,1]
# clf = tree.DecisionTreeClassifier()
# clf = clf.fit(features,labels)
# print clf.predict([[150,0]])

#######################################################################
training_data = pd.DataFrame()

training_data['hour'] = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15 , 16 , 17 , 18, 19, 20, 21, 22, 23];
# training_data['count'] = [34, 1, 127, 85, 49, 3, 77, 37, 91, 55, 22, 88, 12, 9, 0, 44, 65, 2, 58, 6, 33, 49, 61, 27];
training_data['status_to_int'] = [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0]
training_data['status'] = ['unnormal', 'unnormal', 'unnormal', 'unnormal', 'unnormal', 'unnormal', 'unnormal', 'unnormal'
, 'normal', 'normal', 'normal', 'normal', 'normal', 'normal', 'normal', 'normal', 'normal', 'normal'
, 'unnormal', 'unnormal', 'unnormal', 'unnormal', 'unnormal', 'unnormal'];

columns = ["hour"]
# training_data['status'] = [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0];
status = training_data[['status_to_int', 'status']].copy();

X = training_data.as_matrix(columns=['hour']);
y = np.array(status['status_to_int']);

trained_model = tree.DecisionTreeClassifier().fit(X, y);

x_test = np.array([[20]]);
print trained_model.predict(x_test);
print trained_model.predict_proba(x_test);

tree.export_graphviz(trained_model, out_file="tree.dot",
                         feature_names=columns,
                        #  class_names=status['status'],
                         filled=True, rounded=True)

# dot_data = tree.export_graphviz(trained_model , out_file = None , feature_names=training_data.columns[:2], class_names=y, filled = True , rounded = True , special_characters = True)
# graph = pydotplus.graph_from_dot_data(dot_data)
# graph.write_png("graph.png")
