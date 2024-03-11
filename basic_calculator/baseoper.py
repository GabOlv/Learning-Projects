import numpy as np

class Operations:
    def __init__(self, callback):
        self.lock = False
        self.value_1 = ''
        self.operator = ''
        self.value_2 = ''
        self.total_expression = "0"
        self.current_expression = "0"
        self.callback = callback
    
    def basic_operation_handle(self):
        try:
            final_expression = ''
            self.total_expression = (self.total_expression+self.current_expression)
            final_expression = eval(self.total_expression)                             
            self.current_expression = round(final_expression, 12)
            self.lock = True
        except Exception as e:
            self.lock = True
            self.current_expression = 'Error'
            print(e)
                
    def clear_handle(self):
        self.total_expression, self.current_expression, self.value_1, self.value_2, self.operator = '0', '0', '', '', ''
        print('Cleared')
    
    def square_root(self):
        value = np.sqrt(float(self.value_1))
        self.current_expression = round(value, 5)
        self.total_expression = f'\u221A{round(float(self.value_1), 5)}'
        self.lock = True
    
    def power_of_two(self):
        value = np.power(float(self.value_1), 2)
        self.current_expression = round(value, 5)
        self.total_expression = f'({round(float(self.value_1), 5)})²'
        self.lock = True
    
    def operator_handle(self, element):
        self.operator = element
        self.total_expression = self.current_expression+self.operator
    
    def digits_handle(self,element):
        if self.total_expression == '0':
            self.value_1 = self.value_1+str(element)
        else:
            self.value_2 =self.value_2+str(element)
            
    def main_loop_call(self, element):
        print(f'input: {element}, type: {type(element)}')
        # Clear Method
        if (element == 'C'):
            self.clear_handle()
            self.lock = False
        if self.lock == False:
            # Value 1 Method
            if (isinstance(element, (int, float)) and (self.operator == '') and (element not in ('/', '*', '-', '+', '=', 'C'))) or (element == '.'):
                self.digits_handle(element)
                self.current_expression = self.value_1
            # Operator Method
            if element in ('/', '*', '-', '+'):
                self.operator_handle(element)
            # Value 2 Method
            if (isinstance(element, (int, float)) or element == '.') and (self.operator != '') and (element not in ('/', '*', '-', '+', '=', 'C')):
                self.digits_handle(element)
                self.current_expression = self.value_2
            if (element == 'sqr(x)' and self.operator == '' and self.value_1 != ''):   
                self.square_root()
            if (element == 'x^2' and self.operator == '' and self.value_1 != ''):   
                self.power_of_two()
            # Result Method
            if ((element == '=' and self.operator != '') and (element not in ('/', '*', '-', '+', 'C', 'sqr(x)') and self.value_1 != '')):
                self.basic_operation_handle()  
        self.callback()