import time

from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation

from fourier.actors import Circle, LineAxes, SineWave, MultiSineWave
from fourier.fourier import average_point_location, get_shape

def main_window(show=True):
    fig = plt.figure()
    plt.subplots_adjust(left=0.045, right=1-0.045, top=0.95, bottom=0.06, wspace=0.15)

    circle_graph = plt.subplot2grid((4, 10), (0, 0), rowspan=4, colspan=5)
    sound_graph = plt.subplot2grid((4, 10), (0, 5), rowspan=2, colspan=5)
    fourier_graph = plt.subplot2grid((4, 10), (2, 5), rowspan=2, colspan=5)


    line_axes = LineAxes(x_lim1=-1.1, x_lim2=1.1, y_lim1=-1.1, y_lim2=1.1)
    circle_graph.plot(*line_axes.data())

    circle = Circle(radius=1)
    circle_graph.plot(*circle.data())

    wave1 = SineWave.init_frequency(3, y0=0)
    wave2 = SineWave.init_frequency(6, y0=0)
    wave3 = SineWave.init_frequency(3, amplitude=2, y0=0)

    wave = MultiSineWave()
    wave.append(wave1)
    # wave.append(wave2)
    # wave.append(wave3)

    sound_graph.plot(*wave.data(x1=0, x2=5, step=0.01))

    shape = get_shape(wave, 1, 0, 2, step=0.005)
    avg_point = average_point_location(*shape)

    shape_g = circle_graph.plot(*shape)[0]
    avg_point_g = circle_graph.plot(avg_point[0], avg_point[1], 'or')[0]

    circle_graph.axis('equal')
    sound_graph.axis('equal')
    fourier_graph.axis('equal')

    stop_freqs = [7, 12]

    def animate(i):  # pragma: no cover
        nonlocal shape_g, avg_point_g
        d = 250
        winding_freq = 6 + i / d

        if winding_freq - 1 / d % 1 == 0:
            time.sleep(5)

        new_shape = get_shape(wave, winding_freq, 0, 3, step=0.0025)
        new_avg_point = average_point_location(*new_shape)

        shape_g.set_data(new_shape[0], new_shape[1])
        avg_point_g.set_data([new_avg_point[0]], [new_avg_point[1]])

        if winding_freq in stop_freqs:
            print(winding_freq)
            plt.savefig("D:\\img_{!r}_{!r}.png".format(wave, winding_freq))

        return shape_g, avg_point_g


    ani = FuncAnimation(fig, animate, interval=10, blit=True)
    if show:  # pragma: no cover
        plt.show()
    
    del ani
