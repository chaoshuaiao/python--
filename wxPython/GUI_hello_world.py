
import wx

# class Myapp(wx.App):
#     def OnInit(self):
#         frame = wx.Frame(None, -1, "Hello World")
#         frame.Show()
#         return True
    

# print(lst)
class frame(wx.Frame):
    def __init__(self,parent, title):
        wx.Frame.__init__(self,parent, title = "Hello World")
        panel = wx.Panel(self)
        sizer = wx.BoxSizer(wx.VERTICAL)
        self.text1 = wx.TextCtrl(panel, value= "Hello World", size=(200, 180),style=wx.TE_MULTILINE)
        sizer.Add(self.text1, 0, wx.ALIGN_TOP | wx.EXPAND)
        button = wx.Button(panel,label="Click Me")
        sizer.Add(button)
        panel.SetSizerAndFit(sizer)
        panel.Layout()
        self.Bind(wx.EVT_BUTTON, self.OnClick, button)
        self.Show()
    def OnClick(self, text):
        self.text1.AppendText(" hello, world\n")
if __name__ == '__main__':
        app = wx.App()
        frame = frame(None, "Hello World!\n")
        app.MainLoop()
                   