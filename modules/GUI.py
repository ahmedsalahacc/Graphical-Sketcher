from tkinter import *
from tkinter import ttk
from sketcher import Sketcher

class SketcherInterface:
    def __init__(self):
        self.sketcher = Sketcher()
        self.master = Tk()
        self.master.resizable(False,False)
        self._setMaster()
        self.pane = ttk.Frame(width=500,height = 500,relief = SUNKEN)
        self.pane.pack(fill = BOTH,expand = 1,side = 'top')
        self._setLabel(self.pane,0,20,text = 'BOTH fields must be of the same length',row=0,col=0)
        self._setLabel(self.pane, 40, 20, text='Independent Var', row=1, col=0)
        self.vars = [StringVar]*2
        self.field1 = self._setField(self.pane,40,10,row = 2,col = 0)
        self._setLabel(self.pane, 40, 20, text='Dependent Var', row=3, col=0)
        self.field2 = self._setField(self.pane, 40, 10, row=4, col=0)
        self._setButton(self.pane,0,40,'Sketch',command = self._sketch,row = 5,col=0)
        self.message = StringVar()
        self._setValField(self.pane,0,0,self.message,row=6,col=0)

    def initiate(self):
        self.master.mainloop()

    def _setMaster(self):
        self.master.geometry('400x440+650+250')
        self.master.title('Sketcher')

    def _setButton(self, root, xpad, ypad, text, command, row=0, col=0):
        button = ttk.Button(root,text = text,command = command)
        button.grid(padx =xpad,pady=ypad,row=row,column =col)

    def _setLabel(self, root, xpad, ypad, text, row=0, col=0):
        label = ttk.Label(root, text=text)
        label.grid(padx=xpad, pady=ypad, row=row, column=col)

    def _setValField(self, root, xpad, ypad,textVar,row=0, col=0):
        label = ttk.Label(root)
        label.config(textvariable=textVar)
        label.grid(padx=xpad, pady=ypad, row=row, column=col)

    def _setField(self, root, xpad, ypad, row=0, col=0):
        field = ttk.Entry(root,width = 50)
        field.grid(padx=xpad, pady=ypad, row=row, column=col)
        return field

    def _sketch(self):
        self.vars[0] = self.field1.get()
        self.vars[1] = self.field2.get()
        if len(self.vars[0].split(',')) != len(self.vars[1].split(',')):
            self.message.set("ERROR fields are not of the same length")
        else:
            self.message.set("Checked")
            self.sketcher.setPairs(self.vars[0],self.vars[1])
            self.sketcher.plot('X','y','X vs y')

    
