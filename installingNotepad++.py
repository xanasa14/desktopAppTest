#Run as admin
import pywinauto
print(pywinauto.__version__)

from pywinauto import Application, Desktop

app = Application(backend="uia").start(cmd_line=r"C:\Users\User\Downloads\npp.7.9.5.Installer.exe")
app.window(title_re="Installer")
#app.Installer.print_control_identifiers()
selectLang = app.Installer.child_window(title="Installer Language", control_type="Window")
#app.Installer.print_control_identifiers()
okay = app.Installer.child_window(title="OK", auto_id="1", control_type="Button")
Next = okay.click_input()

#print(app.Installer)
#app.Next.print_control_identifiers()


#NEXT
dialogs = app.top_window
#app.Dialogs.print_control_identifiers()

nextPage = app.Dialogs.child_window(title="Next >", auto_id="1", control_type="Button")
nextPage.click_input()

#AGREE
agreement = app.top_window
app.Dialogs.Agreement.child_window.print_control_identifiers()

#agree = app.Agreement.child_window(title="Next >", auto_id="1", control_type="Button")
#nextPage.click_input()