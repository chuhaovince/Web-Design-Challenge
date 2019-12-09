import pandas as pd
path = "Resources/cities.csv"
data = pd.read_csv(path)
data_html = data.to_html("data.html", bold_rows = True)