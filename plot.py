import ntpath
import sys
from matplotlib import pyplot as plt
import os

def plot(title, file=sys.argv[1]):
    with open(file) as f:
        output = 'plots/'
        if not os.path.exists(os.path.dirname(output)):
            try:
                os.makedirs(os.path.dirname(output))
            except OSError as exc:
                if exc.errno != errno.EEXIST:
                    raise 
        lines = f.readlines()
        n = [5, 15, 50, 100, 150, 200, 500]
        time = [float(i) for i in lines]

        plt.plot(n, time)
        plt.title(title)
        plt.xlabel('N')
        plt.ylabel(('Time'))
        plt.savefig(output+f'plot-{os.path.splitext(ntpath.basename(file))[0]}-mB.png')

if __name__ == '__main__':
    plot("Óptimizar Horas Algoritmo 3")