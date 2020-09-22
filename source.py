import wx


APP_EXIT = 1

class MyFrame(wx.Frame):

    def __init__(self, parent, title, size):
        super().__init__(parent=parent, title=title, size=size, style=wx.CLIP_CHILDREN)

app = wx.App()

frame = MyFrame(None, 'Custom window style', (1280, 720))
frame.Center()
frame.Show()

app.MainLoop()