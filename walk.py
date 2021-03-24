import os
for roo, dirs, files in os.walk(".", topdown=False):
   for name in files:
      print(os.path.join(roo, name))
   for name in dirs:
      print(os.path.join(roo, name))
