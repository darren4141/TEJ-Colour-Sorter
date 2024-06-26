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
        self.column2_label = tk.Label(self, text="Sorted Skittles")
        self.column2_label.grid(row=0, column=1)
        self.column2_label["text"] = text="Yellow count: " + str(self.colourCount[0])
        self.column2_label.grid(row=1, column=1)
        self.column2_label["text"] = text="Red count: " + str(self.colourCount[1])
        self.column2_label.grid(row=2, column=1)
        self.column2_label["text"] = text="Blue count: " + str(self.colourCount[2])
        self.column2_label.grid(row=3, column=1)
        self.column2_label["text"] = text="Green count: " + str(self.colourCount[3])
        self.column2_label.grid(row=4, column=1)
        self.column2_label["text"] = text="Purple count: " + str(self.colourCount[4])
        self.column2_label.grid(row=5, column=1)


        # Column 3
        self.column3_label = tk.Label(self, text="Manual control mode")
        self.column3_label.grid(row=0, column=2)

        #Yellow button
        self.column3_button0 = tk.Button(self)
        self.column3_button0["text"] = "Yellow"
        self.column3_button0["command"] = self.yellow_button_clicked
        self.column3_button0.grid(row=1, column=2)

        #Red button
        self.column3_button1 = tk.Button(self)
        self.column3_button1["text"] = "Red"
        self.column3_button1["command"] = self.red_button_clicked
        self.column3_button1.grid(row=2, column=2)

        #Blue button
        self.column3_button2 = tk.Button(self)
        self.column3_button2["text"] = "Blue"
        self.column3_button2["command"] = self.blue_button_clicked
        self.column3_button2.grid(row=3, column=2)

        #Green button
        self.column3_button3 = tk.Button(self)
        self.column3_button3["text"] = "Green"
        self.column3_button3["command"] = self.servoTurnToAngle(80, 3)
        self.column3_button3.grid(row=4, column=2)

        #Purple button
        self.column3_button4 = tk.Button(self)
        self.column3_button4["text"] = "Purple"
        self.column3_button4["command"] = self.servoTurnToAngle(100, 4)
        self.column3_button4.grid(row=5, column=2)


    def column1_button_clicked(self):
        print("Column 1 button clicked!")

    def column2_button_clicked(self):
        print("Column 2 button clicked!")

    def yellow_button_clicked(self):
        print("Yellow button clicked!")
        self.colourCount[0] += 1
        self.column2_label["text"] = text="Yellow count: " + str(self.colourCount[0])
        self.column2_label.grid(row=1, column=1)

    def red_button_clicked(self):
        print("Red button clicked!")
        self.colourCount[1] += 1
        self.column2_label["text"] = text="Red count: " + str(self.colourCount[1])
        self.column2_label.grid(row=2, column=1)

    def blue_button_clicked(self):
        print("Blue button clicked!")
        self.colourCount[2] += 1
        self.column2_label["text"] = text="Blue count: " + str(self.colourCount[2])
        self.column2_label.grid(row=3, column=1)

    def servoTurnToAngle(self, degrees, colour):
        print(degrees)
        print(colour)
        self.colourCount[colour] += 1
        

    def servoTurnToAngle1(self):
        self.colourCount[0] += 1

root = tk.Tk()
app = Application(master=root)
app.mainloop()