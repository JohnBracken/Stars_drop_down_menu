import pandas as pd
stars = pd.read_json("./stars.json")
stars_sorted = stars.sort_values(by=["PROPER NAME"])
stars_sorted.to_json("./stars_json_sorted.json", orient="records", indent=4)
