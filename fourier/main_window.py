from matplotlib import pyplot as plt

from fourier.actors import Circle, SineWave, LineAxes

fig = plt.figure()
plt.subplots_adjust(left=0.045, right=1-0.045, top=0.95, bottom=0.06, wspace=0.15)

circle_graph = plt.subplot2grid((4, 10), (0, 0), rowspan=4, colspan=5)
sound_graph = plt.subplot2grid((4, 10), (0, 5), rowspan=2, colspan=5)
fourier_graph = plt.subplot2grid((4, 10), (2, 5), rowspan=2, colspan=5)

plt.draw()
