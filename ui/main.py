__author__ = 'zardosht'

import wx
import MainWindow


def main():
    app = wx.App()
    main_window = MainWindow.MainWindow(None)
    main_window.Show()

    app.MainLoop()


if __name__ == '__main__':
    main()