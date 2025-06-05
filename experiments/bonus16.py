import FreeSimpleGUI as sg

label1 = sg.Text("yntri yngers vory pti zip arvi:")
input1 = sg.Input()
choose_button1 = sg.FileBrowse("kttcra im axper")

label2 = sg.Text("ur tanenq dnenq es zipy aper:")
input2 = sg.Input()
choose_button2 = sg.FolderBrowse("jogir arden")

compress_button = sg.Button("ashxati merymar aperik")
window = sg.Window("Zipa karum ani esi", layout=[
    [label1, input1, choose_button1],
    [label2, input2, choose_button2], [compress_button]
])
window.read()
window.close()