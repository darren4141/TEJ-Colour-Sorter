import tkinter as tk
import time
from time import sleep
import RPi.GPIO as GPIO
from gpiozero import Servo
 
 
GPIO.setmode(GPIO.BCM)
 
#Declare the rampServoPin as 22
rampServoPin = 22
# Declare servo on GPIO pin
rampServo = Servo(rampServoPin)
# Set up GPIO pin of servo as an output
GPIO.setup(rampServoPin, GPIO.OUT)
 
#Declare the loaderServoPin as 23
loaderServoPin = 27
loaderServo = Servo(loaderServoPin)
GPIO.setup(loaderServoPin, GPIO.OUT)
 
class Application(tk.Frame):
 
    def __init__(self, master=None):
        super().__init__(master)
        self.colourCount = [0, 0, 0, 0, 0] #declare 5 counters for the amount of each colour
        self.master = master
        self.pack()
        self.create_widgets()
 
 
    def create_widgets(self):
        # Column 1
        self.column1_label = tk.Label(self, text="Commands") #set text label
        self.column1_label.grid(row=0, column=0) #set position of text label
        self.column1_button = tk.Button(self) #declare a new button
        self.column1_button["text"] = "Load" #set the label on the button
        self.column1_button["command"] = self.load #set the method that will be called when the button is clicked
        self.column1_button.grid(row=1, column=0) #set the position of the button
        self.column1_button2 = tk.Button(self) #declare a new button
        self.column1_button2["text"] = "STOP" #set the label on the button
        self.column1_button2["command"] = self.stop #set the method that will be called when the button is clicked
        self.column1_button2.grid(row=2, column=0) #set the position of the button
 
        # Column 2
        self.column2_labels = []
        for i, color in enumerate(["Yellow", "Red", "Blue", "Green", "Purple"]): #loop through an array of strings and make 5 labels with each string as the content
            label = tk.Label(self, text=f"{color} count: 0")
            label.grid(row=i+1, column=1)
            self.column2_labels.append(label)
 
        # Column 3
        self.column3_label = tk.Label(self, text="Manual control mode")
        self.column3_label.grid(row=0, column=2)
 
        #Yellow button
        self.column3_button0 = tk.Button(self)
        self.column3_button0["text"] = "Yellow"
        self.column3_button0["command"] = lambda: self.servoTurnToAngle(-180, 0) #when yellow button is pressed, turn to this angle
        self.column3_button0.grid(row=1, column=2)
 
        #Red button
        self.column3_button1 = tk.Button(self)
        self.column3_button1["text"] = "Red"
        self.column3_button1["command"] = lambda: self.servoTurnToAngle(160, 1) #when red button is pressed, turn to this angle
        self.column3_button1.grid(row=2, column=2)
 
        #Blue button
        self.column3_button2 = tk.Button(self)
        self.column3_button2["text"] = "Blue"
        self.column3_button2["command"] = lambda: self.servoTurnToAngle(320, 2) #when blue button is pressed, turn to this angle
        self.column3_button2.grid(row=3, column=2)
 
        #Green button
        self.column3_button3 = tk.Button(self)
        self.column3_button3["text"] = "Green"
        self.column3_button3["command"] = lambda: self.servoTurnToAngle(540, 3) #when green button is pressed, turn to this angle
        self.column3_button3.grid(row=4, column=2)
 
        #Purple button
        self.column3_button4 = tk.Button(self)
        self.column3_button4["text"] = "Purple"
        self.column3_button4["command"] = lambda: self.servoTurnToAngle(660, 4) #when purple button is pressed, turn to this angle
        self.column3_button4.grid(row=5, column=2)
 
 
    def load(self): #load method
        global loaderServo
        print("Load button clicked!")
        loaderServo.value = 1 #set the servo to the loading value
        time.sleep(2) #wait a bit
        loaderServo.value = -1 #set the servo to the feeding value
 
    def stop(self):
        time.sleep(999999)
 
    def servoTurnToAngle(self, degrees, colour): # the servo turn to angle method will increment a counter and turn the servo motor to a specific angle
        global rampServo
        print(degrees)
        print(colour)
        self.colourCount[colour] += 1 #increment the colour selected
        self.column2_labels[colour]["text"] = f"{['Yellow', 'Red', 'Blue', 'Green', 'Purple'][colour]} count: {self.colourCount[colour]}" #print a column of labels
        rampServo.value = degrees/180 #set the rampServo to the degrees value
 
root = tk.Tk()
app = Application(master=root)
app.mainloop()