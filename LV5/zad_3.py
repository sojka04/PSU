import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay, classification_report, accuracy_score

df = pd.read_csv("occupancy_processed.csv")

X = df[['S3_Temp', 'S5_CO2']].to_numpy()
y = df['Room_Occupancy_Count'].to_numpy()

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, stratify=y)

scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

tree = DecisionTreeClassifier(max_depth=3)
tree.fit(X_train, y_train)
y_pred = tree.predict(X_test)

cm = confusion_matrix(y_test, y_pred)
disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=['Slobodna', 'Zauzeta'])
disp.plot(cmap=plt.cm.Blues)
plt.title('Matrica zabune')
plt.show()

print(f"Točnost: {accuracy_score(y_test, y_pred):.4f}")
print(classification_report(y_test, y_pred, target_names=['Slobodna', 'Zauzeta']))

plt.figure(figsize=(12, 8))
plot_tree(tree, feature_names=['S3_Temp', 'S5_CO2'], class_names=['Slobodna', 'Zauzeta'], filled=True)
plt.title('Vizualizacija stabla odlučivanja')
plt.show()
