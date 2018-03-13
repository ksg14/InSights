import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure
import matplot

class InSightsPlot():
    
    def __init__ (self, subplot_args=111):
        self.subplot_args = subplot_args
        self.figure_pane = None
        self.plot_axes = None
        self.plot_canvas = None
        self.toolbar = None
    
    def set_figure (self, width=5, heigth=5):
        self.figure_pane = Figure(figsize=(width, heigth), dpi=100)
        self.plot_axes = self.figure_pane.add_subplot( self.subplot_args )

    def bar_plot (self, vector_x, vector_y):
        self.plot_axes = self.plot_canvas.figure.axes[0]
        self.plot_axes.bar (vector_x, vector_y)
        self.plot_axes.set_xlim(min(vector_x), max(vector_x))
        self.plot_axes.set_ylim(min(vector_y), max(vector_y))        
        self.plot_canvas.draw()

    def simple_plot (self, vector_x, vector_y):
        self.line, = self.plot_axes.plot(vector_x, vector_y)
    
    def update_simple_plot (self, vector_x, vector_y):
        self.line.set_data (vector_x, vector_y)
        self.plot_axes = self.plot_canvas.figure.axes[0]
        self.plot_axes.set_xlim(min(vector_x), max(vector_x))
        self.plot_axes.set_ylim(min(vector_y), max(vector_y))        
        self.plot_canvas.draw()
        
    def update_canvas (self, TOP, BOTTOM, BOTH, window):
        self.plot_canvas = FigureCanvasTkAgg (self.figure_pane, window)
        self.plot_canvas.show ()
        self.plot_canvas.get_tk_widget ().pack (side=BOTTOM, fill=BOTH, expand=True)

        self.toolbar = NavigationToolbar2TkAgg (self.plot_canvas, window)
        self.toolbar.update ()
        self.plot_canvas._tkcanvas.pack (side=TOP, fill=BOTH, expand=True)
        