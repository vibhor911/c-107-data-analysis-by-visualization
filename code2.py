import pandas as pd
import csv
import plotly.graph_objects as go

df = pd.read_csv("data.csv")

student_id = df.loc[df['student_id'] == "TRL_987"]
print(student_id.groupby("level")["attempt"] .mean())

fig = go.Figure(go.Scatter(
    x = student_id.groupby("level")["attempt"] .mean(),
    y = ['level 1','level 2','level 3','level 4'],
    orientation = 'h'
))

fig.show()