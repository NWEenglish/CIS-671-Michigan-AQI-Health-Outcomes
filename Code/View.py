from tkinter import ttk, font, messagebox
from functools import partial
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import math
import tkinter as tk

class View:
    def __init__(self, display, model):
        self.display = display
        self.model = model 
        self.bubble_counties = {} 
        self.column_counties = {}
        self.pie_counties = {} 
        self.notebook = self.setup_notebook()
        self.create_homepage() 
        self.add_visualizations()
    
    def setup_notebook(self):
        notebook = ttk.Notebook(self.display)
        notebook.pack(fill="both", expand=True)

        return notebook 

    def create_homepage(self):
        tab = ttk.Frame(self.notebook)

        self.notebook.add(tab, text='Home')

        label = ttk.Label(tab, text="Welcome", font=font.Font(size=30))
        label.grid(row=0, column=0, sticky='nsew')
        label.place(x=((self.notebook.winfo_screenwidth() / 2))-25, y=100, anchor='center')

        label1 = ttk.Label(tab, text="Visual #1: PFAS Occurances Per County", font=font.Font(size=20))
        label1.grid(row=0, column=0, sticky='nsew')
        label1.place(x=((self.notebook.winfo_screenwidth() / 2))-25, y=200, anchor='center')

        label2 = ttk.Label(tab, text="Visual #2: Percent AQI Days Per County", font=font.Font(size=20))
        label2.grid(row=0, column=0, sticky='nsew')
        label2.place(x=((self.notebook.winfo_screenwidth() / 2))-25, y=300, anchor='center')

        label3 = ttk.Label(tab, text="Visual #3: Pie Chart", font=font.Font(size=20))
        label3.grid(row=0, column=0, sticky='nsew')
        label3.place(x=((self.notebook.winfo_screenwidth() / 2))-25, y=400, anchor='center')

        label4 = ttk.Label(tab, text="Visual #4: Choropleth Map", font=font.Font(size=20))
        label4.grid(row=0, column=0, sticky='nsew')
        label4.place(x=((self.notebook.winfo_screenwidth() / 2))-25, y=500, anchor='center')

        label5 = ttk.Label(tab, text="Visual #5: Heat Map", font=font.Font(size=20))
        label5.grid(row=0, column=0, sticky='nsew')
        label5.place(x=((self.notebook.winfo_screenwidth() / 2))-25, y=600, anchor='center')

    def add_visualizations(self):
        for visual in self.model.get_visualizations().values():
            tab = ttk.Frame(self.notebook)
            self.notebook.add(tab, text=visual.get_name())

            figure_frame = ttk.Frame(tab)
            figure_frame.grid(row=0, column=0, sticky='nsew')

            canvas = FigureCanvasTkAgg(visual.get_visual(), master=figure_frame)
            canvas_widget = canvas.get_tk_widget()
            canvas_widget.grid(row=0, column=0, sticky="nsew")
            if visual.get_id() == 4: 
                canvas.figure.canvas.mpl_connect('button_press_event', partial(self.on_click, vis=visual))

            tab.grid_rowconfigure(0, weight=1)
            tab.grid_columnconfigure(0, weight=1)
            figure_frame.grid_rowconfigure(0, weight=1)
            figure_frame.grid_columnconfigure(0, weight=1)

            if visual.get_id() == 1:
                self.add_checkboxes(visual, tab, self.bubble_counties, figure_frame)
            if visual.get_id() == 2:
                self.add_checkboxes(visual, tab, self.column_counties, figure_frame)
            if visual.get_id() == 3:
                self.add_checkboxes(visual, tab, self.pie_counties, figure_frame)
                
    def add_checkboxes(self, visual, tab, dict, figure_frame):
        checkbox_frame = ttk.Frame(tab)
        checkbox_frame.grid(row=0, column=1, sticky='nsew')

        for county in visual.get_counties():
            checkbox = tk.IntVar(value=1)
            dict[county] = checkbox  
            button = tk.Checkbutton(checkbox_frame, text = county, 
                            variable = checkbox, 
                            onvalue = 1, 
                            offvalue = 0,
                            command=lambda county=county: self.update_data(visual, dict, county, figure_frame))
            button.grid(sticky="w") 

    def update_data(self, visual, dict, county, figure_frame):
        self.model.update_visualization(visual, county, dict[county].get())
        self.update_display(visual, figure_frame) 

    def update_display(self, visual, figure_frame):
        for figure in figure_frame.winfo_children():
            figure.destroy()

        canvas = FigureCanvasTkAgg(visual.get_visual(), master=figure_frame)
        canvas_widget = canvas.get_tk_widget()
        canvas_widget.grid(row=0, column=0, sticky="nsew")
        
        self.display.update()

    def on_click(self, event, vis):
        for location in vis.get_locations():
            distance = math.sqrt(((event.xdata - location['x']) ** 2 + (event.ydata - location['y']) ** 2))
            if distance < 0.1:  
                self.show_popup(location['County'], location['Health Outcome'], location['Health Factors'], location['Quality Of Life'], location['Health Score'])
                break 

    def show_popup(self, county_name, health_outcome, health_factors, quality_of_life, health_score):
        messagebox.showinfo("Information", f"County Name: {county_name}\nHealth Outcome: {health_outcome}\nHealth Factors: {health_factors}\nQuality of Life: {quality_of_life}\nHealth Score: {health_score}")

    def run_display(self):
        self.display.mainloop()
