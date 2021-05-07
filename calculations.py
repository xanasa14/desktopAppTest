#Code for Windows Calculator
#https://github.com/microsoft/calculator
from pywinauto import Desktop, Application

app = Application(backend='uia').start('calc.exe')

dialog = Desktop(backend='uia').Calculator
dialog.print_control_identifiers(depth=1)
#max_calc = dialog.child_window(title="Maximize Calculator", auto_id='Maximize', control_type="Button")
#max_calc.click()


# 2 * 3
operations = [ "plusButton", "minusButton","multiplyButton","divideButton"]

a = "6"
b = "3"

"""
#app.Properties.print_control_identifiers()
dialog.child_window(auto_id="CalculatorResults", control_type="Text").type_keys("5")
dialog.child_window( auto_id="num2Button", control_type="Button").click()
dialog.child_window( auto_id="divideButton", control_type="Button").click()
dialog.child_window( auto_id="num3Button", control_type="Button").click()
dialog.child_window( auto_id="equalButton", control_type="Button").click()
"""
for oper in operations:
    dialog.child_window(auto_id="CalculatorResults", control_type="Text").type_keys(a)
    dialog.child_window(auto_id=oper, control_type="Button").click()
    dialog.child_window(auto_id="CalculatorResults", control_type="Text").type_keys(b)
    dialog.child_window(auto_id="equalButton", control_type="Button").click()
    print(dialog.child_window(auto_id="CalculatorResults", control_type="Text").wrapper_object())