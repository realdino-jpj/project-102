import os
import sys
from os import listdir

path = input("enter folder path: ")
extension = input("enter extension: ")

if os.path.exists(path):
   for item in path:
       if item.endswith(extension):
          os.remove(item)
else:
    print("path does not exist")
