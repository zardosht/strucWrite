__author__ = 'zardosht'


import wx
import os.path, dircache


def FMNUBuildFolder(self, event):

    dlg = wx.wxDirDialog(self)

    try:
        if dlg.ShowModal() == wx.wxID_OK:
            dir = dlg.GetPath()
            self.root = ""
            self.list.DeleteAllItems()
            self.tree.DeleteAllItems()
            self.musiclist = []
            self.musiclistdict = {}
            self.nummp3s = 0
            self.numparsed = 0
            self.StartBuildFromDir(dir)
            self.BuildMusicDict()
            self.ParseMusicList()
            self.tree.Expand(self.root)
    finally:
        dlg.Destroy()


def StartBuildFromDir(self, dir):
    rootname = os.path.split(dir)
    self.root = self.tree.AddRoot(rootname[1])
    self.rootdir = dir
    self.BuildChildrenFromDir(self.root, dir)


def BuildChildrenFromDir(self, parent, dir):
    dirlisting = os.listdir(dir)
    for listing in dirlisting:
        pathinquestion = os.path.join(dir, listing)
        if os.path.isfile(pathinquestion):
            extension = os.path.splitext(pathinquestion)
            extension = extension[1]
            if extension == ".mp3":
                child = self.tree.AppendItem(parent, listing)
                childdata = self.tree.GetItemData(child)
                childdata.path = pathinquestion
                id3info = ID3(pathinquestion)
                mp3info = [id3info.get('TITLE', ""),
                           id3info.get('ARTIST', ""),
                           id3info.get('GENRE', ""),
                           id3info.get('YEAR', ""),
                           id3info.get('ALBUM', ""),
                           id3info.get('TRACKNUMBER', ""),
                           pathinquestion]
                self.musiclist.append(mp3info)
                self.nummp3s += 1
        elif os.path.isdir(pathinquestion):
            newparent = self.tree.AppendItem(parent, listing)
            newdir = os.path.join(dir, listing)
            self.BuildChildrenFromDir(newparent, newdir)


def ParseMusicList(self):
    items = self.musiclistdict.items()
    for i, x in enumerate(items):
        key, data = x
        self.list.InsertStringItem(i, data[0])
        self.list.SetStringItem(i, 0, data[0])
        self.list.SetStringItem(i, 1, data[1])
        self.list.SetStringItem(i, 2, data[2])
        self.list.SetStringItem(i, 3, data[3])
        self.list.SetStringItem(i, 4, data[4])
        self.list.SetStringItem(i, 5, data[5])
        self.list.SetStringItem(i, 6, data[6])
        self.list.SetItemData(i, key)

def BuildMusicDict(self):
    key = 0
    for mp3listing in self.musiclist:
        key += 1
        newmp3listing = tuple(mp3listing)
        self.musiclistdict[key] = newmp3listing
    self.itemDataMap = self.musiclistdict
    wx.wxColumnSorterMixin.__init__(self, 7)
