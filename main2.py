#Run as admin
import pywinauto
print(pywinauto.__version__)

from pywinauto import Application, Desktop

app = Application(backend="uia").start(cmd_line=r"C:\Users\User\Downloads\npp.7.9.5.Installer.exe")
app.window(title_re="Installer")
selectLang = app.Installer.print_control_identifiers()
okButton = selectLang

'''
dlg = app.Notepad
dlg = app.top_window()
dialogs = app.windows()
app.window(title_re=".*Part of Title.*")
app.dlg.control
app['dlg']['control']

app.YourDialog.print_control_identifiers()
app.YourDialog.draw_outline()
print("ASHFAFAHFKAHFKHASFLKHALHF ")
print(
app.YourDialog.draw_outline()
)
#app.child_window( auto_id="1007", control_type="Text").item_count()

#app.Properties.print_control_identifiers()

#app2 = app.child_window( auto_id="1002", control_type="Button")
#app3 = app2.child_window(title="okButton", auto_id="1", control_type="Button")

'''