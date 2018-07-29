#! python3
from sklearn.datasets import load_iris
from sklearn import tree
import graphviz
iris = load_iris()
clf = tree.DecisionTreeClassifier()
print(iris.target)

# clf = clf.fit(iris.data, iris.target)
# dot_data = tree.export_graphviz(clf, out_file=None)
# graph = graphviz.Source(dot_data)
# graph.render("iris")
# dot_data = tree.export_graphviz(clf, out_file=None,
#                                 feature_names=iris.feature_names,
#                                 class_names=iris.target_names,
#                                 filled=True, rounded=True,
#                                 special_characters=True)
# graph = graphviz.Source(dot_data)
# print(graph)
# # def entropy(m, n):
# #     return -m * math.log(m, 2) - n * math.log(n, 2)


# # print(entropy(2 / 5, 3 / 5))
