


from datetime import datetime
import os
import sys
import csv
import tkinter as tk
from tkinter import ttk

sys.path.extend([r"C:\Users\paul\OneDrive\Documents\__PyThOn\08_PyP"])
from Cap8_28_pymysql_oop import Db

class LabelInput(tk.Frame):
    """A widget containing a label and input together."""

    def __init__(self, parent,                          # all widgets take this argument
                 label='',                              # text for the label part of the witget
                 input_class=ttk.Entry,                 # the class of the widget we want to create or ttk.Entry default
                 input_var=None,                        # tk var to assign to the input (optional)
                 input_args=None,                       # opt dict with arg for the input constructor (optional)
                 label_args=None,                       # opt dict with arg for the label constructor (optional)
                 **kwargs):                             # any other for the frame constructor
        super().__init__(parent, **kwargs)
        input_args = input_args or {}
        label_args = label_args or {}
        self.variable = input_var

        if input_class in (ttk.Checkbutton, ttk.Button, ttk.Radiobutton):
            input_args["text"] = label
            input_args["variable"] = input_var
        else:
            self.label = ttk.Label(self, text=label, **label_args)
            self.label.grid(row=0, column=0, sticky=(tk.W + tk.E))
            input_args["textvariable"] = input_var

        self.input = input_class(self, **input_args)
        self.input.grid(row=1, column=0, sticky=(tk.W + tk.E))
        self.columnconfigure(0, weight=1)

    def grid(self, sticky=(tk.E + tk.W), **kwargs):
        super().grid(sticky=sticky, **kwargs)  # suprascrie metoda grid

    def get(self):
        if self.variable:
            return self.variable.get()
        elif type(self.input) == tk.Text:
            return self.input.get('1.0', tk.END)
        else:
            return self.input.get()

    def set(self, value, *args, **kwargs):
        if type(self.variable) == tk.BooleanVar:
                self.variable.set(bool(value))
        elif self.variable:
                self.variable.set(value, *args, **kwargs)
        elif type(self.input).__name__.endswith('button'):
            if value:
                self.input.select()
            else:
                self.input.deselect()
        elif type(self.input) == tk.Text:
            self.input.delete('1.0', tk.END)
            self.input.insert('1.0', value)
        else:
            self.input.delete(0, tk.END)
            self.input.insert(0, value)


class Command_form(tk.Frame, Db):
    """The input form for our widgets"""

    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
            # A dict to keep track of input widgets
        self.inputs = {}

        persoane = tk.LabelFrame(self, text="Persoane")

        # line 1
        self.inputs['Nume'] = LabelInput(
            persoane, "Nume",
            input_var=tk.StringVar()
        )
        self.inputs['Nume'].grid(row=0, column=0)

        self.inputs['Prenume'] = LabelInput(
            persoane, "Prenume",
            input_var=tk.StringVar()
        )
        self.inputs['Prenume'].grid(row=0, column=1)

        self.inputs['DataN'] = LabelInput(
            persoane, "DataN",
            input_class=ttk.Combobox,
            input_var=tk.StringVar(),
            input_args={"values": datetime.strftime(datetime.today(), '%Y-%m-%d')}
            )
        self.inputs['DataN'].grid(row=0, column=2)

        self.inputs['Inaltime'] = LabelInput(
            persoane, "Inaltime",
            input_class=tk.Spinbox,
            input_var=tk.IntVar(),
            input_args={"from_": 50, "to": 250, "increment": 1}
            )
        self.inputs['Inaltime'].grid(row=1, column=0)

        self.inputs['Greutate'] = LabelInput(
            persoane, "Greutate",
            input_class=tk.Spinbox,
            input_var=tk.IntVar(),
            input_args={"from_": 10, "to": 150, "increment": 1}
        )
        self.inputs['Greutate'].grid(row=1, column=1)

        persoane.grid(row=0, column=0, sticky=(tk.W + tk.E))      # close the first group
        # default the form
        self.reset()

    def get(self):
        """Retrieve data from form as a dict"""

        # We need to retrieve the data from Tkinter variables
        # and place it in regular Python objects

        data = {}
        for key, widget in self.inputs.items():
            data[key] = widget.get()
        return data

    def reset(self):
        """Resets the form entries"""

        # clear all values
        for widget in self.inputs.values():
            widget.set('')


class Application(tk.Tk, Db):
    """Application root window"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.title("Insert persoane")
        self.resizable(width=True, height=True)

        ttk.Label(
            self,
            text="Command Entry Form",
            font=("TkDefaultFont", 16)
        ).grid(row=0)

        self.recordform = Command_form(self)
        self.recordform.grid(row=1, padx=10)    # padx adauga margini stanga, dreapta

        self.savebutton = ttk.Button(self, text="Save", command=self.on_save)
        self.savebutton.grid(sticky=tk.E, row=2, padx=10)

        """When writing methods or functions to be callbacks for a GUI event, 
        it's conventional to use the format on_EVENTNAME, where EVENTNAME is a string 
        describing the event triggering it. We could also name this method 
        on_save_button_click(), but for now on_save() is adequate.
        """

        # status bar
        self.status = tk.StringVar()
        self.statusbar = ttk.Label(self, textvariable=self.status)
        self.statusbar.grid(sticky=(tk.W + tk.E), row=3, padx=10)
        """
        We start by creating a string variable called self.status and use this as textvariable 
        for ttk.Label. All our application will need to do to update the status is call 
        self.status.set() anywhere inside the class. Our GUI is completed by adding the status bar 
        to the bottom of the application widget.
        """
        self.records_saved = 0

    def on_save(self):
        """Handles save button clicks"""

        # For now, we save to a hardcoded filename with a datestring.
        # If it doesnt' exist, create it,
        # otherwise just append to the existing file
        datestring = datetime.today().strftime("%Y-%m-%d")
        filename = "command{}.csv".format(datestring)
        newfile = not os.path.exists(filename)

        data = self.recordform.get()
        var_insert = "insert into ppl(nume, prenume, datan, inaltime, greutate) \
            values({0},{1},{2},{3},{4})".format(
            "'" + data['Nume'] + "'",
            "'" + data['Prenume'] + "'",
            "'" + data['DataN'] + "'",
            data['Inaltime'],
            data['Greutate'])

        self.query("test_python", var_insert)

        with open(filename, 'a') as fh:
            csvwriter = csv.DictWriter(fh, fieldnames=data.keys())
            if newfile:
                csvwriter.writeheader()
            csvwriter.writerow(data)

        self.records_saved += 1
        self.status.set(
            "{} records saved this session".format(self.records_saved))
        self.recordform.reset()


if __name__ == "__main__":
    app = Application()
    app.mainloop()
