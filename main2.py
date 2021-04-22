#Run as admin
import pywinauto
print(pywinauto.__version__)

from pywinauto.application import Application
app = Application(backend="uia").start(cmd_line=r"C:\Users\User\Downloads\npp.7.9.5.Installer.exe", timeout=3)

main_win = app.window(title='output.txt')
clix = app

