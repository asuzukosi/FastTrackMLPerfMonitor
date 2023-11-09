"""Takes the data and generates html with nice Plotly graphs
Usage:
    generate_html.py data.csv index.html
"""

import datetime
import sys
from io import StringIO
from pathlib import Path

import pandas as pd
import plotly.express as px

# number of days to look back
n_days = 180

def fetch_csv(csvPath: str) -> pd.DataFrame:
    return pd.read_csv(csvPath)

def plot_cumulative_state(df: pd.DataFrame, outfile: str):
    fig = px.line(
        df,
        x="timestamp",
        y="value",
        title="FastTrackML performance chart",
        color='application',
        facet_col="test_name",
        facet_col_wrap=4,
        markers=True,
        hover_data=["application", "test_name", "value"],
        
    )

    fig.update_traces(marker={'size': 4})
    fig.update_layout(title_x=0.5)
    fig.update_yaxes(ticksuffix="%", title='', rangemode="tozero")
    fig.update_xaxes(title='')
    fig.for_each_annotation(lambda a: a.update(text=a.text.split("=")[-1]))

    fig.write_html(outfile, include_plotlyjs='cdn')

if __name__ == "__main__":
    data = fetch_csv(sys.argv[1])
    data["timestamp"] = pd.to_datetime(data["timestamp"])

    now = datetime.datetime.now()
    cutoff_date = now - datetime.timedelta(days=n_days)
    data = data.loc[data["timestamp"] > cutoff_date]
    # data = data.loc[data["test_name"] in ["test_collect_metrics_data_0", "test_collect_metrics_data_1"]]

    plot_cumulative_state(data, sys.argv[2])