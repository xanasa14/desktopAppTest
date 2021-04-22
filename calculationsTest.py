from pywinauto import application
from pywinauto import Desktop, Application

app = Application(backend='uia').start('calc.exe')
app.Notepad.print_control_identifiers()
#app.Notepad.MenuSelect("Edit->Replace")
#app.Replace.print_control_identifiers()