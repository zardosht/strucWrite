__author__ = 'zardosht'


root = '/path/to/root'
ids = {root : tree.AddRoot(root)}
for (dirpath, dirnames, filenames) in os.walk(root):
    for dirname in dirnames:
        fullpath = os.path.join(dirpath, dirname)
        ids[fullpath] = tree.AppendItem(ids[dirpath], dirname)
    for filename in sorted(filenames):
        tree.AppendItem(ids[dirpath], filename)
