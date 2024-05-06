import pandas as pd
from datetime import datetime
from uuid import uuid4

def mmx_dict_to_dataframe(mmx_dict):
    total_channels = []
    for recommendation, channels in mmx_dict.items():
        if recommendation == "Other options":
            data = {}
            data["channel"] = "others"
            data["comment"] = channels
            data["recommendation"] = "others"
            total_channels.append(data)
            continue

        for channel in channels:
            data = {}
            data["channel"] = channel[0]
            data["recommendation"] = recommendation
            data["comment"] = channel[1]
            total_channels.append(data)
    mmx_df = pd.DataFrame.from_dict(total_channels)
    mmx_df["time"] = datetime.now()
    mmx_df["id"] = str(uuid4())
    return mmx_df
