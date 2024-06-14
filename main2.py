import tkinter as tk

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)

        self.colourCount = [0, 0, 0, 0, 0]

        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        # Column 1
        self.column1_label = tk.Label(self, text="Column 1")
        self.column1_label.grid(row=0, column=0)
        self.column1_button = tk.Button(self)
        self.column1_button["text"] = "Button 1"
        self.column1_button["command"] = self.column1_button_clicked
        self.column1_button.grid(row=1, column=0)

        # Column 2
        self.column2_labels = []
        for i, color in enumerate(["Yellow", "Red", "Blue", "Green", "Purple"]):
            label = tk.Label(self, text=f"{color} count: 0")
            label.grid(row=i+1, column=1)
            self.column2_labels.append(label)

        # Column 3
        self.column3_label = tk.Label(self, text="Manual control mode")
        self.column3_label.grid(row=0, column=2)

        #Yellow button
        self.column3_button0 = tk.Button(self)
        self.column3_button0["text"] = "Yellow"
        self.column3_button0["command"] = lambda: self.servoTurnToAngle(0, 0)
        self.column3_button0.grid(row=1, column=2)

        #Red button
        self.column3_button1 = tk.Button(self)
        self.column3_button1["text"] = "Red"
        self.column3_button1["command"] = lambda: self.servoTurnToAngle(40, 1)
        self.column3_button1.grid(row=2, column=2)

        #Blue button
        self.column3_button2 = tk.Button(self)
        self.column3_button2["text"] = "Blue"
        self.column3_button2["command"] = lambda: self.servoTurnToAngle(60, 2)
        self.column3_button2.grid(row=3, column=2)

        #Green button
        self.column3_button3 = tk.Button(self)
        self.column3_button3["text"] = "Green"
        self.column3_button3["command"] = lambda: self.servoTurnToAngle(80, 3)
        self.column3_button3.grid(row=4, column=2)

        #Purple button
        self.column3_button4 = tk.Button(self)
        self.column3_button4["text"] = "Purple"
        self.column3_button4["command"] = lambda: self.servoTurnToAngle(100, 4)
        self.column3_button4.grid(row=5, column=2)


    def column1_button_clicked(self):
        print("Column 1 button clicked!")

    def column2_button_clicked(self):
        print("Column 2 button clicked!")

    def column3_button_clicked(self):
        print("Column 3 button clicked!")

    def servoTurnToAngle(self, degrees, colour):
        print(degrees)
        print(colour)
        self.colourCount[colour] += 1
        self.column2_labels[colour]["text"] = f"{['Yellow', 'Red', 'Blue', 'Green', 'Purple'][colour]} count: {self.colourCount[colour]}"

root = tk.Tk()
app = Application(master=root)
app.mainloop()