import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from numpy import genfromtxt


# sphinx_gallery_thumbnail_number = 2


def func():
    for t in range(10):
        audiencia = genfromtxt('files/RungeKuttaT' + str(t) + '.csv', delimiter=',')

        fig, ax = plt.subplots()
        im = ax.imshow(audiencia)

        # We want to show all ticks...
        ax.set_ylabel("canales")
        ax.set_xlabel("horarios")

        cbarlabel = ""
        cbar_kw = {}
        cbar = ax.figure.colorbar(im, ax=ax, **cbar_kw)
        cbar.ax.set_ylabel(cbarlabel, rotation=-90, va="bottom")

        ax.set_title("Impacto de la publicidad en horario/canal con " + str(t) + " publicidades")
        fig.tight_layout()
        plt.show()


if __name__ == "__main__":
    func()
