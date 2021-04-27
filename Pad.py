from pywinauto.application import Application

app = Application(backend="uia").start("notepad.exe").connect(title='Untitled - Notepad')
#it gets capitalized and removed all extra characters non alpha

textEditor = app.UntitledNotepad.child_window(title="Text Editor", auto_id="15", control_type="Edit").wrapper_object()
textEditor.type_keys("Holiii my name is xavi", with_spaces= True)

fileMenu = app.UntitledNotepad.child_window(title='File', control_type="MenuItem").wrapper_object()
fileMenu.click_input()
app.UntitledNotepad.print_control_identifiers()
Sav = app.UntitledNotepad.child_window(title="Save	Ctrl+S", auto_id="3", control_type="MenuItem").wrapper_object()
Sav.click_input()
