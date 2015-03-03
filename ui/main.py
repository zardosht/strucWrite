__author__ = 'zardosht'

import wx


app = wx.App()
frame = wx.Frame(None, -1, 'strucWrite', style=wx.DEFAULT_FRAME_STYLE & (~wx.RESIZE_BORDER))
frame.Show()

app.MainLoop()
