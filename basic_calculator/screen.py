from baseoper import Operations
import os
import tkinter as tk

# Constants for color and font styles
LARGE_FONT_STYLE = ("Arial", 40, "bold")
SMALL_FONT_STYLE = ("Arial", 16)
DIGITS_FONT_STYLE = ("Arial", 24, "bold")
DEFAULT_FONT_STYLE = ("Arial", 20)

# NEW
OFF_WHITE = "#F8FAFF"
WHITE = "#FFFFFF"
LIGHT_BLUE = "#CCEDFF"
LIGHT_GRAY = "#F5F5F5"
LABEL_COLOR = "#25265E"

class Interface:
    def __init__(self):
        self.oper = Operations(self.update_labels)
        # Initialize the Tkinter window, variables and UI elements
        self.window = tk.Tk() 
        self.setup_variables()
        self.setup_ui()
    
    def setup_variables(self):
        # Set window properties
        self.window.title("Calculator")
        self.window.geometry("375x667") # Size of the screen
        self.window.resizable(0,0)  # Unresizable
        # Get the absolute path of the icon and return it to be used on the window
        icon_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "icon.ico")
        self.window.iconbitmap(icon_path)
        
        #  Button and layout dictionaries key:(x,y)
        self.digits = {
            7: (1,1), 8: (1,2), 9: (1,3),
            4: (2,1), 5: (2,2), 6: (2,3),
            1: (3,1), 2: (3,2), 3: (3,3),
            0: (4,2), '.': (4,1), 
        }
        self.operations = {"/": "\u00F7", "*": "\u00d7", "-":"-", "+": "+"}
        self.functionalities = {"C": "C", "x^2": 'x²', 'sqr(x)': "\u221A2"}
        self.equal = {"=": '='}


    def setup_ui(self):
        # Create display labels and buttons frame
        self.total_label, self.current_label = self.create_display_labels()
        self.buttons_frame = self.create_buttons_frame()
        
        # Configure row and column weights to allow resize and upscaling
        self.buttons_frame.rowconfigure(0, weight=1)
        for x in range(1,5):
            self.buttons_frame.grid_rowconfigure(x, weight=1)
            self.buttons_frame.columnconfigure(x, weight=1)
            
        # Digit, operator and special buttons section
        self.create_digit_buttons()
        self.create_operator_button()
        self.create_special_buttons()
        self.create_equal()
        
    
    # Create total and current expression labels that expresses the values and operators in strings on screen
    def create_display_labels(self):
        # Previous
        total_label = tk.Label(self.window, text=self.oper.total_expression, anchor=tk.E,
                        background=LIGHT_GRAY, padx=24, width=20, foreground=LABEL_COLOR, font=SMALL_FONT_STYLE)
        total_label.pack(expand=True,fill='both')
        
        # Current
        current_label = tk.Label(self.window, text=self.oper.current_expression, anchor=tk.E,
                        background=LIGHT_GRAY, padx=24, foreground=LABEL_COLOR, font=LARGE_FONT_STYLE)
        current_label.pack(expand=True,fill='both')
        return total_label, current_label

    # Update the label above using a call back from the Operations class
    def update_labels(self):
            self.total_label.config(text=self.oper.total_expression)
            self.current_label.config(text=self.oper.current_expression)

    # Create digit buttons (numbers)
    def create_digit_buttons(self):
        for digit,grid_value in self.digits.items():
            button = tk.Button(self.buttons_frame, text=str(digit),background=LIGHT_GRAY, 
                               foreground=LABEL_COLOR, font=DEFAULT_FONT_STYLE, borderwidth=0,
                               command=lambda d=digit: self.digit_button_click(d))
            button.grid(row=grid_value[0], column=grid_value[1], sticky=tk.NSEW)

    # Digits buttons opperation handle
    def digit_button_click(self, digit):
            self.oper.main_loop_call(digit)
           
    # Create operator buttons (/, *, -, +)       
    def create_operator_button(self):
        i = 0
        for operator , symbol in self.operations.items():
            button = tk.Button(self.buttons_frame, text=str(symbol), background=OFF_WHITE, 
                               foreground=LABEL_COLOR, font=DEFAULT_FONT_STYLE, borderwidth=0,
                               command=lambda o=operator: self.operator_button_click(o))
            button.grid(row=i, column=4, stick=tk.NSEW)
            i+=1
    # Operator buttons opperation handle             
    def operator_button_click(self, operator):
        self.oper.main_loop_call(operator)
    
    # Create special buttons (C, x², sqr(x)
    def create_special_buttons(self):
        i = 1
        for special , symbol in self.functionalities.items():
            button = tk.Button(self.buttons_frame, text=str(symbol), background=OFF_WHITE, 
                               foreground=LABEL_COLOR, font=DEFAULT_FONT_STYLE, borderwidth=0,
                               command=lambda s = special: self.special_button_click(s))
            button.grid(column=i, row=0, sticky=tk.NSEW)
            i+=1
            
    # Special buttons opperation handle        
    def special_button_click(self,special):
        self.oper.main_loop_call(special)
    
    # Create equal button (=)        
    def create_equal(self):
        for equal, symbol in self.equal.items():
            button = tk.Button(self.buttons_frame, text=str(symbol), background=LIGHT_BLUE, 
                               foreground=LABEL_COLOR, font=DEFAULT_FONT_STYLE, borderwidth=0,
                               command=lambda e=equal: self.equal_button_click(e))
            button.grid(column=3,row=4,sticky=tk.NSEW,columnspan=2)
            
    def equal_button_click(self, equal):
        self.oper.main_loop_call(equal)
            
    # Create the buttons frame to fill        
    def create_buttons_frame(self):
        frame = tk.Frame(self.window, background=LIGHT_GRAY)
        frame.pack(expand=True,fill='both')
        return frame
    
    def run(self):
        # Run the main loop to start the interface
        self.window.mainloop()