import pandas as pd



df = pd.read_csv('MachineLearningCVE/output_file.csv')
df = df.drop(df[df.Label == 'BENIGN'].index)
df.to_csv('MachineLearningCVE/output_file.csv', index=False)