import tkinter as tk
from tkinter import ttk

import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure

from plot.graph import InSightsPlot

import pandas as pd

class InSights (tk.Frame):
    def __init__ (self, master=None):
        # Parent Constructor
        tk.Frame.__init__ (self, master)
        # Instance Variables
        self.master = master
        self.plot_api = InSightsPlot ()
        self.data = None
        self.file_name = None
        self.file_entry = None
        self.path = ''
        self.data_x = None
        self.data_y = None
        self.data_x_vector = []
        self.data_y_vector = []
        self.choices = ['-- NA --']
        self.dropdown_x = None
        self.dropdown_y = None
        # Setup window
        self.root = tk.Tk ()
        self.root.title ('InSights')
    
    def quit (self):
        self.root.quit()
    
    def setup (self):
        # Setup default plot_frame
        self.plot_api.set_figure ()
        self.plot_api.simple_plot ([1,2,3,4,5,6,7,8], [5,6,1,3,8,9,3,5])
        self.plot_api.update_canvas (tk.TOP, tk.BOTTOM, tk.BOTH, self.root)

        # Setup Options
    
        # File Name
        self.file_name = tk.StringVar ()
        self.file_entry = tk.Entry (self.root, text='Enter File Name', textvariable=self.file_name)
        self.file_entry.pack (fill=tk.BOTH, expand=True)
        tk.Button (self.root, text="Load", command=self.load).pack ()

        # DropDown
        self.data_x = tk.StringVar ()
        self.data_y = tk.StringVar ()
        self.data_x.set (self.choices [0])
        self.data_y.set (self.choices [0])
        self.dropdown_x = tk.OptionMenu(self.root, self.data_x, *self.choices)
        self.dropdown_x.pack (fill=tk.BOTH, expand=True)
        tk.Button(self.root, text="Plot X", command=self.update_plot).pack ()


        tk.Button(self.root, text="Quit", command=self.quit).pack ()
        # start gui instance
        self.root.mainloop ()
    
    def load (self):
        print (self.file_entry.get ())
        # D:\Documents\Data\Cleansed_data_ui1.xlsx
        self.path = self.file_entry.get ()
        print (type (self.path))
        
        self.data = pd.read_excel (self.path)
        self.choices = list(self.data.columns.values)
        self.data_x.set (self.choices [0])
        print (self.choices [0])
        # print (self.choices)
        # Update Widget
        self.dropdown_x['menu'].delete(0, 'end')
        for choice in self.choices:
            self.dropdown_x['menu'].add_command(label=choice, command=tk._setit(self.data_x, choice))
        
        # Add Map types


    def update_plot (self):
        # print (self.data_x.get ())
        self.data_x_vector = self.data [self.data_x.get ()].tolist ()
        self.data_y_vector = [tmp for tmp in range (len (self.data_x_vector))]

        self.plot_api.update_simple_plot (self.data_y_vector, self.data_x_vector)
        # self.plot_api.set_figure ()
        # self.plot_api.update_canvas (tk.TOP, tk.BOTTOM, tk.BOTH, self.root)
        return

def driver ():
    app = InSights ()
    app.setup ()

if __name__ == '__main__':
    driver ()