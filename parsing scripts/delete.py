import glob
import os
import csv

for filename in glob.glob('lacticAcid/exhale/*/*'):
   name = os.path.basename(os.path.normpath(filename))
   if name.startswith("dark") or name.startswith("light") or name.startswith("purge") or name.startswith("exhale") or name.startswith("result_Acetone_2") or name.startswith("_flow") or name.startswith("results") or name.startswith("start") or name.startswith("hm") or name.startswith("Q") or name.startswith("result_2") or name.startswith("result_DIV"):
      os.remove(filename)