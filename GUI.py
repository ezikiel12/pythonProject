import wx

app = wx.App(clearSigInt=True)
frame = wx.Frame(parent=None, id=wx.ID_ANY, title="Node Production Tracker", pos = (100, 100))
panel = wx.Panel(parent=frame, id=wx.ID_ANY)
welcomeText = wx.StaticText(parent=panel, label="Node Tracker", pos = (20, 20))

frame.Show()
app.MainLoop()
