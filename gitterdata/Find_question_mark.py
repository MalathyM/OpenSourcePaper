import sys
import pandas as pd
import numpy as np
import csv
import argparse
parser = argparse.ArgumentParser(description="This script updates the new column with value as 1 if the sentence contains ? symbol")
print(parser)
try:
    data = pd.read_excel(sys.argv[1])
except Exception:
    data = pd.read_csv(sys.argv[1])
finally:
	sub='\?'
	data['question'] = data[sys.argv[3]].str.contains(sub) 
	data['question'] = data['question'].map({True: 1, False: 0})
	data.to_csv(sys.argv[2],encoding='utf-8', index=False)
