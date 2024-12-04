from Enums.Visualization import Visual
from Visualizations.BaseVisual import BaseVisual
from tkinter import ttk, font, messagebox
from functools import partial
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import math
import tkinter as tk

class View:
    def __init__(self, display, model):
        self.display = display
        self.model = model
        self.visualFilters = {}
        self.notebook = self.setup_notebook()
        self.create_homepage()
        self.add_visualizations()
    
    def setup_notebook(self) -> ttk.Notebook:
        notebook = ttk.Notebook(self.display)
        notebook.pack(fill="both", expand=True)

        return notebook 

    def create_homepage(self) -> None:
        tab = ttk.Frame(self.notebook)
        self.notebook.add(tab, text='Home')

        label = ttk.Label(tab, text="Welcome", font=font.Font(size=30))
        label.grid(row=0, column=0, sticky='nsew')
        label.place(x=((self.notebook.winfo_screenwidth() / 2))-25, y=100, anchor='center')

        yValue = 100
        textLabels = [
            "Visual #1: PFAS Occurances Per County",
            "Visual #2: Percent AQI Days Per County",
            "Visual #3: Pie Chart",
            "Visual #4: Choropleth Map",
            "Visual #5: Heat Map",
            "Visual #6: Scatter Plot"
        ]

        for textLabel in textLabels:
            yValue += 100
            label = ttk.Label(tab, text=textLabel, font=font.Font(size=20))
            label.grid(row=0, column=0, sticky='nsew')
            label.place(x=((self.notebook.winfo_screenwidth() / 2))-25, y=yValue, anchor='center')

    def add_visualizations(self) -> None:
        visual: BaseVisual
        for visual in self.model.get_visualizations().values():
            tab = ttk.Frame(self.notebook)
            self.notebook.add(tab, text=visual.get_name())

            figure_frame = ttk.Frame(tab)
            figure_frame.grid(row=0, column=0, sticky="nsew")

            canvas = FigureCanvasTkAgg(visual.get_visual(), master=figure_frame)
            canvas_widget = canvas.get_tk_widget()
            canvas_widget.grid(row=0, column=0, sticky="nsew")
            if visual.get_id() == Visual.ChoroplethMap:
                canvas.figure.canvas.mpl_connect('button_press_event', partial(self.on_click, vis=visual))
                tab.grid_rowconfigure(0, weight=1)
                tab.grid_columnconfigure(0, weight=1)
                figure_frame.grid_rowconfigure(0, weight=1)
                figure_frame.grid_columnconfigure(0, weight=1)
            else:
                tab.grid_rowconfigure(0, weight=1)
                tab.grid_columnconfigure(0, weight=0)
                tab.grid_columnconfigure(1, weight=1)

                figure_frame.grid_rowconfigure(0, weight=1)
                figure_frame.grid_columnconfigure(0, weight=1)

                right_frame = ttk.Frame(tab)
                right_frame.grid(row=0, column=1, sticky="ns")

                checkbox_frame = self.add_scrollbar(right_frame)

            if visual.has_filtering():
                filter = self.visualFilters.get(visual.get_id())
                if not filter:
                    filter = {}
                
                self.add_checkboxes(visual, checkbox_frame, filter, figure_frame)

            elif visual.has_radio():
                filter = self.visualFilters.get(visual.get_id())
                if not filter:
                    filter = {}

                self.add_radio(visual, checkbox_frame, filter, figure_frame)

            elif visual.has_sorting():
                filter = self.visualFilters.get(visual.get_id())
                if not filter:
                    filter = {}

                self.add_sort(visual, checkbox_frame, filter, figure_frame)

    #https://stackoverflow.com/questions/73095063/adding-a-scrollbar-to-a-canvas-with-figures-tkinter
    def add_scrollbar(self, right_frame):
        canvas = tk.Canvas(right_frame)
        canvas.grid(row=0, column=0, sticky="nsew")
        scrollbar = ttk.Scrollbar(right_frame, orient='vertical', command=canvas.yview)
        scrollbar.grid(row=0, column=1, sticky="ns")
        canvas.configure(yscrollcommand=scrollbar.set)
        checkbox_frame = ttk.Frame(canvas)
        canvas.create_window((0, 0), window=checkbox_frame, anchor="nw")
        checkbox_frame.bind('<Configure>', lambda e: canvas.config(scrollregion=canvas.bbox('all')))

        right_frame.grid_rowconfigure(0, weight=1)
        right_frame.grid_columnconfigure(0, weight=1)
        right_frame.grid_columnconfigure(1, weight=0)

        return checkbox_frame

    def add_checkboxes(self, visual, frame, filtering, figure_frame) -> None:
        label = tk.Label(frame, text="Display Selected")
        label.grid(sticky="w") 

        for county in visual.get_counties():
            checkbox = tk.IntVar(value=1)
            filtering[county] = checkbox
            button = tk.Checkbutton(frame, text = county,
                            variable = checkbox,
                            onvalue = 1,
                            offvalue = 0,
                            command=lambda county=county: self.update_data(visual, filtering, county, figure_frame))
            button.grid(sticky="w") 

    def add_radio(self, visual, frame, filtering, figure_frame) -> None:
        selected_county = tk.StringVar(value=visual.get_counties()[0])  # Default to first value
        label = tk.Label(frame, text="Display Selected")
        label.grid(sticky="w")

        for county in visual.get_counties():
            filtering[county] = selected_county
            button = tk.Radiobutton(frame, text=county,
                                    variable=selected_county,
                                    value=county,
                                    command=lambda county=county: self.update_data(visual, filtering, county, figure_frame))
            button.grid(sticky="w")

    def add_sort(self, visual, frame, filtering, figure_frame) -> None:
        selected_option = tk.StringVar(value=visual.get_sort_options()[0])  # Default to first value
        label = tk.Label(frame, text="Sort By")
        label.grid(sticky="w")

        for option in visual.get_sort_options():
            filtering[option] = selected_option
            button = tk.Radiobutton(frame, text=option,
                                    variable=selected_option,
                                    value=option,
                                    command=lambda county=option: self.update_data(visual, filtering, county, figure_frame))
            button.grid(sticky="w")

    def update_data(self, visual, filtering, value, figure_frame) -> None:
        self.model.update_visualization(visual, value, filtering[value].get())
        self.update_display(visual, figure_frame)

    def update_display(self, visual, figure_frame) -> None:
        for figure in figure_frame.winfo_children():
            figure.destroy()

        canvas = FigureCanvasTkAgg(visual.get_visual(), master=figure_frame)
        canvas_widget = canvas.get_tk_widget()
        canvas_widget.grid(row=0, column=0, sticky="nsew")
        
        self.display.update()

    def on_click(self, event, vis) -> None:
        for location in vis.get_locations():
            distance = math.sqrt(((event.xdata - location['x']) ** 2 + (event.ydata - location['y']) ** 2))
            if distance < 0.1:  
                self.show_popup(location['County'], location['Health Outcome'], location['Health Factors'], location['Quality Of Life'], location['Health Score'])
                break 

    def show_popup(self, county_name, health_outcome, health_factors, quality_of_life, health_score) -> None:
        messagebox.showinfo("Information", f"County Name: {county_name}\nHealth Outcome: {health_outcome}\nHealth Factors: {health_factors}\nQuality of Life: {quality_of_life}\nHealth Score: {health_score}")

    def run_display(self) -> None:
        self.display.mainloop()
