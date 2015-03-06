__author__ = 'zardosht'


# MainWindow.py

import wx


class MainWindow(wx.Frame):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.init_ui()

    def init_ui(self):
        menu_bar = wx.MenuBar()
        file_menu = wx.Menu()
        quit_menu_item = file_menu.Append(wx.ID_EXIT, 'Quit', 'Quit application')
        self.Bind(wx.EVT_MENU, self.on_quit, quit_menu_item)
        menu_bar.Append(file_menu, '&Fiile')
        self.SetMenuBar(menu_bar)




        self.SetSize((720, 480))
        self.SetTitle('strucWrite')
        self.Centre()

    def on_quit(self, e):
        self.Close()