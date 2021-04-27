from pywinauto import application
from pywinauto import Desktop, Application

app = Application(backend='uia').start('calc.exe', timeout=3)
#dialog = Desktop(backend='uia').Calculator
#dialog.print_control_identifiers(depth=5)
dlg = app.Notepad
dlg = app.top_window()
dialogs = app.windows()
app.window(title_re=".*Part of Title.*")
app.dlg.control
app['dlg']['control']

app.YourDialog.print_control_identifiers(depth=5)