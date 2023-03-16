import csv
import numpy as np
import matplotlib.pyplot as plt


def graphs():
    arr = np.genfromtxt('data1.csv', delimiter=';')
    arr = arr[1:]

    time = np.float_(arr[:, 0])
    pol = np.int_(arr[:, 3])
    obor = np.int_(arr[:, 4])

    fig, (gr1, gr2) = plt.subplots(nrows=1, ncols=2, figsize=(16, 8))
    gr1.plot(time, pol * 70, 'b', time, obor, 'r')
    gr1.set_title('График')
    gr1.set_ylabel('ПДЗ(%* 70)        Об. двигателя(об/мин)')
    gr1.set_xlabel('Время (с)')

    plt.scatter(pol, obor)
    gr2.scatter(pol, obor, marker='o', c='green', edgecolor='lime')
    gr2.set_title('График кореляции')
    gr2.set_ylabel('Об. двигателя(об/мин)')
    gr2.set_xlabel('ПДЗ(%* 70)')
    plt.show()


graphs()
