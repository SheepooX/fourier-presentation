#!/bin/env python

import tkinter
from fractions import Fraction
from tkinter import *

import matplotlib
import numpy as np
from matplotlib import pyplot, style
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,
                                               NavigationToolbar2TkAgg)

from actors import Circle, MultiSineWave, SineWave
from scrollable_side_panel import ScrollableSidePanel

matplotlib.use('TkAgg')


def average_point_location(x, y):
    """
    Calculates an average location of points.

    Args:
        x: X values.
        y: Y values.

    Returns: Tuple - X_avg, Y_avg.

    Raises:
        ValueError: The length of x-values != length of y-values.
    """
    if len(x) != len(y):
        raise ValueError("The length of x-values != length of y-values.")
    return sum(x) / len(x), sum(y) / len(y)


def get_shape(sine_wave, winding_frequency, a, b, step=0.1):
    """
    Winds a part of a sine wave around a circle with a winding frequency.

    Args:
        sine_wave: Instance of fourier.actors.SineWave
        winding_frequency: Winding frequency.
        a: Left boundary.
        b: Right boundary.
        (optional)
        step: Step of the calculation.
    
    Returns: Instance of numpy.ndarray with imaginary part.

    Raises:
        ValueError: Winding Frequency must be positive.
        ValueError: The following condition must be true: a < b.
    """
    if winding_frequency <= 0:
        raise ValueError("Winding Frequency must be positive.")
    if a >= b:
        raise ValueError("The following condition must be true: a < b.")
    x = np.arange(a, b + step, step)
    omega = 2 * np.pi * winding_frequency
    sine_wave_data_y = sine_wave.data(a, b, step=step)[1]
    shape_x = sine_wave_data_y * np.sin(omega * x)
    shape_y = sine_wave_data_y * np.cos(omega * x)
    return shape_x, shape_y


class PlotManager:

    def __init__(self, canvas, figure, side_panel):
        self.canvas = canvas
        self.circle_axes = pyplot.subplot2grid((2, 10), (0, 0), rowspan=1, colspan=4)
        self.sound_axes = pyplot.subplot2grid((2, 10), (0, 5), rowspan=1, colspan=5)
        self.freq_axes = pyplot.subplot2grid((2, 10), (1, 0), rowspan=1, colspan=10)
        #self.circle_axes = figure.add_subplot(211)
        #self.freq_axes = figure.add_subplot(212)

        self.circle_axes.format_coord = lambda x, y: ''
        self.sound_axes.format_coord = lambda x, y: ''
        self.freq_axes.format_coord = lambda x, y: ''

        input_freq_strength = StringVar()
        input_freq_strength_entry = Entry(side_panel, textvariable=input_freq_strength)
        input_freq_strength_entry.bind('<Return>',
                    lambda event: self._freq_amplitude_update(event, input_freq_strength.get()))
        input_freq_strength_entry.grid(row=side_panel.next_row(), column=0)

        self.winding_frequency = DoubleVar()
        winding_frequency_slider = Scale(side_panel, from_=1, to=100, orient=HORIZONTAL,
                                       variable=self.winding_frequency, length=180)
        winding_frequency_slider.bind('<B1-Motion>', lambda event: self._winding_frequency_update(event, self.winding_frequency.get()))
        winding_frequency_slider.grid(row=side_panel.next_row(), column=0)

        winding_frequency_entry = Entry(side_panel, textvariable=self.winding_frequency)
        winding_frequency_entry.bind('<Return>',
                    lambda event: self._winding_frequency_update(event, self.winding_frequency.get()))
        winding_frequency_entry.grid(row=side_panel.next_row(), column=0)

        self.freqs_start = DoubleVar()
        self.freqs_start.set(1)
        freqs_start_entry = Entry(side_panel, textvariable=self.freqs_start)
        freqs_start_entry.bind('<Return>', lambda event: self._set_freqs())
        freqs_start_entry.grid(row=side_panel.next_row(), column=0)

        
        self.freqs_end = DoubleVar()
        self.freqs_end.set(10)
        freqs_end_entry = Entry(side_panel, textvariable=self.freqs_end)
        freqs_end_entry.bind('<Return>', lambda event: self._set_freqs())
        freqs_end_entry.grid(row=side_panel.next_row(), column=0)
        
        self.sound_graph = self.sound_axes.plot([0], [0])[0]

        circle = Circle(radius=1)
        self.circle_axes.plot(*circle.data())
        self.shape_graph = self.circle_axes.plot([0], [0])[0]
        self.avg_point = self.circle_axes.plot([0], [0], 'ro')[0]

        self.fourier_graph1 = self.freq_axes.plot([0], [0])[0]
        self.fourier_graph2 = self.freq_axes.plot([0], [0])[0]

        self.circle_axes.axis('equal')
        self.sound_axes.axis('equal')
        self.freq_axes.axis('equal')

        self.circle_axes.grid()
        self.sound_axes.grid()
        self.freq_axes.grid()

        self.shape = None
        self.multi_sine_wave = None
    
    def _set_sound_graph(self, x, y):
        self.sound_graph.set_xdata(x)
        self.sound_graph.set_ydata(y)
        self.sound_axes.relim()
        self.sound_axes.autoscale_view()
    
    def _set_shape_avg_point_graphs(self):
        self.shape = get_shape(self.multi_sine_wave, Fraction(self.winding_frequency.get()), 0, 10, step=0.01)
        avg_point = average_point_location(*self.shape)

        self.shape_graph.set_xdata(self.shape[0])
        self.shape_graph.set_ydata(self.shape[1])
        self.avg_point.set_xdata([avg_point[0]])
        self.avg_point.set_ydata([avg_point[1]])

        self.circle_axes.relim()
        self.circle_axes.autoscale_view()
    
    def _calculate_fourier(self, start, end, step=0.01):
        fqs = np.arange(start, end + step, step)
        fyr = []
        fyi = []
        for fq in fqs:
            shape = get_shape(self.multi_sine_wave, fq, start, end, step=step)
            avg_point = average_point_location(*shape)
            fyr.append(avg_point[0])
            fyi.append(avg_point[1])
        return fqs, fyr, fyi
    
    def _set_freqs(self):
        x, y1, y2 = self._calculate_fourier(self.freqs_start.get(), self.freqs_end.get())
        self.fourier_graph1.set_xdata(x)
        self.fourier_graph1.set_ydata(y1)
        
        self.fourier_graph2.set_xdata(x)
        self.fourier_graph2.set_ydata(y2)

        self.freq_axes.relim()
        self.freq_axes.autoscale_view()
        self.canvas.draw()
    
    def _winding_frequency_update(self, event, value):
        self._set_shape_avg_point_graphs()
        self.canvas.draw()
    
    def _freq_amplitude_update(self, event, values):
        self.multi_sine_wave = self._get_multi_sine_wave(values)

        self.sound_values = self.multi_sine_wave.data(x1=0, x2=10, step=0.01)
        self._set_sound_graph(self.sound_values[0], self.sound_values[1])

        self._set_shape_avg_point_graphs()
        self._set_freqs()

        self.canvas.draw()

    def _get_multi_sine_wave(self, values):
        spl = values.split(';')
        multi_sine_wave = MultiSineWave()
        for pair in spl:
            spl2 = pair.split(',')
            if len(spl2) == 2:
                freq = Fraction(spl2[0])
                amplitude = Fraction(spl2[1])
                sine_wave = SineWave.init_frequency(freq, amplitude=amplitude)
                multi_sine_wave.append(sine_wave)
        return multi_sine_wave        


def run():
    pyplot.style.use('default')
    tk_root = tkinter.Tk()

    tk_root.wm_title("Fourier Visualization")

    figure = pyplot.figure()

    canvas = FigureCanvasTkAgg(figure, master=tk_root)
    canvas.get_tk_widget().pack(side=tkinter.LEFT, fill=tkinter.BOTH, expand=0.95)

    toolbar = NavigationToolbar2TkAgg(canvas, tk_root)

    canvas.draw()
    toolbar.update()

    side_frame = Frame(tk_root, width=180)
    side_frame.pack(side=RIGHT, fill=BOTH)
    side_panel = ScrollableSidePanel(side_frame)

    plot_mngr = PlotManager(canvas, figure, side_panel)

    tkinter.mainloop()


if __name__ == '__main__':
    run()
