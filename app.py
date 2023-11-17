from tkinter import *
root = Tk()

l1 = LabelFrame(root,text="Label")
l1.pack()
l2 = LabelFrame(root,text="Message")
l2.pack()

label = Label(l1,text="This is Label and this is my first label")
label.pack()

message = Message(l2,text="this is an message box")
message.pack()

root.mainloop()