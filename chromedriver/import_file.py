import os


path = "C:\\Users\\a.pytskiy\\Downloads"

filename = max([os.path.join(path, f) for f in os.listdir(path)], key=os.path.getmtime)
new_filename = os.rename(filename, os.path.join(path, "123.pptx"))


