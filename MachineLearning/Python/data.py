#load churn.txt into a numpy dataframe
import numpy as np
import pandas as pd
from pathlib import Path

pathFile = Path(__file__).parent / "sources/Customer-Churn.csv"
data = pd.read_csv(pathFile)
pd.set_option('display.max_columns', 500)
              
print(data.head(10))