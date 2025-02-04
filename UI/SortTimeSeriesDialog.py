import tkinter as tk
from UI.ViewerDialog import ViewerDialog

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt

#https://github.com/yuma-m/matplotlib-draggable-plot/blob/master/draggable_plot.py

class SortTimeSeriesDialog(ViewerDialog):
    def __init__(self, parent, title, sets):
        self.sets = sets
        self.submit = False
        super().__init__(parent, title, width=600, height=600)

    def body(self, frame):

        self._figure_frame = tk.Frame(frame, padx=20, pady=20)
        self._figure_frame.pack(fill=tk.BOTH, expand = tk.TRUE)

        self._figure, self._axes, self._line = None, None, None
        self._dragging_point = None
        self._points = {}

        self._figure = plt.Figure(figsize=(7,5))

        self._figure.canvas.mpl_connect('button_press_event', self._on_click)
        self._figure.canvas.mpl_connect('button_release_event', self._on_release)
        self._figure.canvas.mpl_connect('motion_notify_event', self._on_motion)

        self._axes = self._figure.add_subplot(111)

        self._axes.set_xlabel("Set")
        self._axes.set_ylabel("Intensity")

        # Rotate labels so do overlap
        for tick in self._axes.get_xticklabels():
            tick.set_rotation(305)


        self._axes.set_ylim(0,1)

        for set in self.sets:
            self._add_point(set, 0.5)

        self._update_plot()

        canvas = FigureCanvasTkAgg(self._figure, self._figure_frame)
        canvas.get_tk_widget().pack(side="top", fill ='both', expand=True)
        canvas.draw()

        # option_set_int_list = [
        #     "IPA_Beard",
        #     "IPA_Bust",
        #     "IPA_Green",
        #     "IPA_Hob",
        #     "IPA_Old",
        #     "IPA_Punk",
        #     "IPA_Thorn",
        #     "Lag_Beck",
        #     "Lag_Bud",
        #     "Lag_Cob",
        #     "Lag_Est",
        #     "Lag_Hob",
        #     "Lag_Per",
        #     "Lag_San",
        #     "Port_Brew",
        #     "Port_Coffee",
        #     "Port_Drag",
        #     "Port_Guin",
        #     "Port_Lond",
        #     "Port_Rob",
        #     "Port_White",
        #     "IPA",
        #     "Lager",
        #     "Porter"
        #     ]

        # self.option_set_int_selected = tk.StringVar(frame)
        # self.option_set_int_selected.set("IPA_Beard")

        # #self.lbl_annotation_relation = tk.Label(frame, width=10)
        # self.option_annotation_relation = tk.OptionMenu(frame, self.option_set_int_selected, *option_set_int_list)
        # self.option_annotation_relation.grid(row=0, column=0)


    def buttonbox(self):
        self.btn_cancel = tk.Button(self, text='Cancel', width=5, command=self.cancel_btn_clicked)
        self.btn_cancel.pack(side="right", padx=(5,10), pady=(5,10))
        self.btn_ok = tk.Button(self, text='OK', width=5, command=self.ok_btn_clicked)
        self.btn_ok.pack(side="right", padx=(5,10), pady=(5,10))
        self.bind("<Return>", lambda event: self.ok_btn_clicked())
        self.bind("<Escape>", lambda event: self.cancel_btn_clicked())

    def ok_btn_clicked(self):
       # option_int_selected = self.option_set_int_selected.get()

        # if option_int_selected == "IPA_Beard":
        #     self.set_values = [0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        # elif option_int_selected == "IPA_Bust":
        #     self.set_values = [0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        # elif option_int_selected == "IPA_Green":
        #     self.set_values = [0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        # elif option_int_selected == "IPA_Hob":
        #     self.set_values = [0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        # elif option_int_selected == "IPA_Old":
        #     self.set_values = [0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        # elif option_int_selected == "IPA_Punk":
        #     self.set_values = [0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        # elif option_int_selected == "IPA_Thorn":
        #     self.set_values = [0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        # elif option_int_selected == "Lag_Beck":
        #     self.set_values = [0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        # elif option_int_selected == "Lag_Bud":
        #     self.set_values = [0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0]
        # elif option_int_selected == "Lag_Cob":
        #     self.set_values = [0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0]
        # elif option_int_selected == "Lag_Est":
        #     self.set_values = [0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0]
        # elif option_int_selected == "Lag_Hob":
        #     self.set_values = [0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0]
        # elif option_int_selected == "Lag_Per":
        #     self.set_values = [0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0]
        # elif option_int_selected == "Lag_San":
        #     self.set_values = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0]
        # elif option_int_selected == "Port_Brew":
        #     self.set_values = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0]
        # elif option_int_selected == "Port_Coffee":
        #     self.set_values = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0]
        # elif option_int_selected == "Port_Drag":
        #     self.set_values = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0]
        # elif option_int_selected == "Port_Guin":
        #     self.set_values = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0]
        # elif option_int_selected == "Port_Lond":
        #     self.set_values = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0]
        # elif option_int_selected == "Port_Rob":
        #     self.set_values = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0]
        # elif option_int_selected == "Port_White":
        #     self.set_values = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0]
        # elif option_int_selected == "IPA":
        #     self.set_values = [0,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        # elif option_int_selected == "Lager":
        #     self.set_values = [0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0]
        # elif option_int_selected == "Porter":
        #     self.set_values = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,0]

        self.set_values = self._read_values_from_points()
        self.submit = True
        self.destroy()

    def cancel_btn_clicked(self):
        self.destroy()

    def _read_values_from_points(self):

        set_values = []
        for set in self.sets:
            set_values.append(self._points[set])

        return set_values

    def _update_plot(self):

        x, y = zip(*sorted(self._points.items()))

        if not self._line:
            self._line, = self._axes.plot(x, y, "b", marker="o", markersize=10)
        else:
            self._line.set_data(x, y)

        self._figure.canvas.draw()


    def _add_point(self, x, y):

        self._points[x] = y

        return x, y

    def _remove_point(self, x, _):

        if x in self._points:
            self._points.pop(x)

    def _find_nearest_point(self, event):

        # Find nearest point along the x axis
        for x, y in self._points.items():

            if x == self.sets[round(event.xdata)]:
                return (x, y)

        return None

    def _on_click(self, event):

        # On click within range of plot
        if event.button == 1 and event.inaxes in [self._axes]:

            # Get nearest point to coordinates of click
            point = self._find_nearest_point(event)

            # Add this to dragging point.
            if point:
                self._dragging_point = point

    def _on_release(self, event):

        # On click within range of plot and dragging point selected.
        if event.button == 1 and event.inaxes in [self._axes] and self._dragging_point:

            # Prevent movement out the line of the draggable point
            self._add_point(self._dragging_point[0], event.ydata)
            self._dragging_point = None
            self._update_plot()

    def _on_motion(self, event):

        # If dragging point selected.
        if not self._dragging_point:
            return

        if event.ydata:

            self._remove_point(*self._dragging_point)

            if event.ydata > 1:
                y = 1
            elif event.ydata < 0:
                y = 0
            else:
                y = event.ydata

            # Prevent movement out the line of the draggable point
            self._dragging_point = self._add_point(self._dragging_point[0], y)
            self._update_plot()

