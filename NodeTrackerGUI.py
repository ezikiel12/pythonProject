from TestCommands import *
import wx
import time

class MyApp(wx.App):
    def __init__(self):
        super().__init__(clearSigInt= True)

        #init frame
        self.InitFrame()

    def InitFrame(self):
        # add frame contents
        frame = MyFrame(parent=None, title="BDI Node Production Tracker", size = (800, 600))
        frame.Show()

class MyFrame(wx.Frame):
    def __init__(self, parent, title, size):
        super().__init__(parent=parent, title=title, size=size)

        self.OnInit()

    def OnInit(self):
        # add panel here
        panel = MyPanel(parent=self)

class MyPanel(wx.Panel):
    def __init__(self, parent):
        super().__init__(parent=parent)

        serial = wx.StaticText(self, label = "Serial Number", pos = (25, 25))
        ip = wx.StaticText(self, label="IP Address", pos=(200, 25))
        macaddr = wx.StaticText(self, label="Mac Address", pos=(500, 25))
        fw = wx.StaticText(self, label="FW Version", pos=(25, 100))
        tech = wx.StaticText(self, label="Tech", pos=(200, 100))

        # add buttons
        button = wx.Button(parent=self, label = "Submit", pos = (250, 250))
        button.Bind(event=wx.EVT_BUTTON, handler=self.onSubmit)

        # add text box
        self._textbox = wx.TextCtrl(parent=self, value = "Serial #", pos = (20, 40))

    def onSubmit(self, event):
            #add an action
        print("Thanks for submitting information")
        serNum = self._textbox.GetValue()
        print (serNum)


        submitThanks = wx.StaticText(self, label="Node Information Submitted", pos=(220, 280))



if __name__ == "__main__":
    app = MyApp()
    app.MainLoop()