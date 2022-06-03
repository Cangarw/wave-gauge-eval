import os

import matplotlib.pyplot as mp
import pandas as pd

files = [x for x in os.listdir('./') if 'LOGGER' in x and 'CSV' in x]
for file in files:
    print(f"{file}")
    df = pd.read_csv(file)
    X = pd.Series([x / 8 for x in range(len(df['PressureBar']))])
    fig = mp.figure(figsize=(10, 5))
    ax = fig.add_subplot(1, 1, 1, title=f"Data from the logfile: {file}")
    ax.set_ylim(1000, df['PressureBar'].max() + 1)
    line, = ax.plot(X, df['PressureBar'], color='blue', lw=2)
    fig.savefig(f"{file[:-4]}.svg")
    fig.savefig(f"{file[:-4]}.png")
    mp.show()
