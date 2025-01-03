# -*- coding: utf-8 -*-
"""
Created on Sat Aug  3 23:04:09 2024

@author: Carlos Luco Montofré
"""

from tkinter import Tk

class Root(Tk):
    
    def __init__(self):
        super().__init__()

        start_width  = 500
        min_width    = 400
        start_height = 550
        min_height   = 250

        self.geometry(f"{start_width}x{start_height}")
        self.minsize(width=min_width, height=min_height)
        self.title("TKinter MVC Multi-frame GUI")
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)