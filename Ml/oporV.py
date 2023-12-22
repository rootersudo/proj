import sklearn as sc
import matplotlib.pyplot as plt
import numpy as np
from sklearn.svm import SVC # "Классификатор на основе метода опорных
 # векторов"

data_x = np.array([[5.3, 2.3], [5.7, 2.5], [4.0, 1.0], [5.6, 2.4], [4.5, 1.5], [5.4, 2.3], [4.8, 1.8], [4.5, 1.5], [5.1, 1.5], [6.1, 2.3], [5.1, 1.9], [4.0, 1.2], [5.2, 2.0], [3.9, 1.4], [4.2, 1.2], [4.7, 1.5], [4.8, 1.8], [3.6, 1.3], [4.6, 1.4], [4.5, 1.7], [3.0, 1.1], [4.3, 1.3], [4.5, 1.3], [5.5, 2.1], [3.5, 1.0], [5.6, 2.2], [4.2, 1.5], [5.8, 1.8], [5.5, 1.8], [5.7, 2.3], [6.4, 2.0], [5.0, 1.7], [6.7, 2.0], [4.0, 1.3], [4.4, 1.4], [4.5, 1.5], [5.6, 2.4], [5.8, 1.6], [4.6, 1.3], [4.1, 1.3], [5.1, 2.3], [5.2, 2.3], [5.6, 1.4], [5.1, 1.8], [4.9, 1.5], [6.7, 2.2], [4.4, 1.3], [3.9, 1.1], [6.3, 1.8], [6.0, 1.8], [4.5, 1.6], [6.6, 2.1], [4.1, 1.3], [4.5, 1.5], [6.1, 2.5], [4.1, 1.0], [4.4, 1.2], [5.4, 2.1], [5.0, 1.5], [5.0, 2.0], [4.9, 1.5], [5.9, 2.1], [4.3, 1.3], [4.0, 1.3], [4.9, 2.0], [4.9, 1.8], [4.0, 1.3], [5.5, 1.8], [3.7, 1.0], [6.9, 2.3], [5.7, 2.1], [5.3, 1.9], [4.4, 1.4], [5.6, 1.8], [3.3, 1.0], [4.8, 1.8], [6.0, 2.5], [5.9, 2.3], [4.9, 1.8], [3.3, 1.0], [3.9, 1.2], [5.6, 2.1], [5.8, 2.2], [3.8, 1.1], [3.5, 1.0], [4.5, 1.5], [5.1, 1.9], [4.7, 1.4], [5.1, 1.6], [5.1, 2.0], [4.8, 1.4], [5.0, 1.9], [5.1, 2.4], [4.6, 1.5], [6.1, 1.9], [4.7, 1.6], [4.7, 1.4], [4.7, 1.2], [4.2, 1.3], [4.2, 1.3]])
data_y=np.array([1, 1, -1, 1, -1, 1, 1, -1, 1, 1, 1, -1, 1, -1, -1, -1, -1, -1, -1, 1, -1, -1, -1, 1, -1, 1, -1, 1, 1, 1, 1, -1, 1, -1, -1, -1, 1, 1, -1, -1, 1, 1, 1, 1, -1, 1, -1, -1, 1, 1, -1, 1, -1, -1, 1, -1, -1, 1, 1, 1, -1, 1, -1, -1, 1, 1, -1, 1, -1, 1, 1, 1, -1, 1, -1, 1, 1, 1, 1, -1, -1, 1, 1, -1, -1, -1, 1, -1, -1, 1, -1, 1, 1, -1, 1, -1, -1, -1, -1, -1])

#print(data_y)
plt.scatter(data_x[:,0],data_x[:,1],c=data_y,s=50)


model = SVC(kernel='linear', C=1000000000)
model.fit(data_x, data_y)
plt.scatter(data_x[:,0],data_x[:,1],c=data_y,s=50)
plt.show()
def plot_svc_decision_function(model, ax=None, plot_support=True):
 """Строим график решающей функции для двумерной SVC"""
 if ax is None:
    ax = plt.gca()
 xlim = ax.get_xlim()
 ylim = ax.get_ylim()
 # Создаем координатную сетку для оценки модели
 x = np.linspace(xlim[0], xlim[1], 30)
 y = np.linspace(ylim[0], ylim[1], 30)
 Y, X = np.meshgrid(y, x)
 xy = np.vstack([X.ravel(), Y.ravel()]).T
 P = model.decision_function(xy).reshape(X.shape)
 # Рисуем границы принятия решений и отступы
 ax.contour(X, Y, P, colors='k',
     levels=[-1, 0, 1], alpha=0.5,
     linestyles=['--', '-', '--'])

 # Рисуем опорные векторы
 if plot_support:
    ax.scatter(model.support_vectors_[:, 0],
        model.support_vectors_[:, 1],
        s=300, linewidth=1, facecolors='none')
 ax.set_xlim(xlim)
 ax.set_ylim(ylim)

j=0
print(model.support_vectors_)
plt.scatter(data_x[:, 0], data_x[:, 1], c=data_y, s=50, cmap='autumn')
plot_svc_decision_function(model)
plt.show()

for i in range(0,99):

    if data_x[i,1]<np.min(model.support_vectors_[:,1]) and data_x[i,0]<np.min(model.support_vectors_[:,0]):
        j=+1
    if data_x[i,1]>np.max(model.support_vectors_[:,1]) and data_x[i,0]>np.max(model.support_vectors_[:,0]):
        j=+1

print(j)