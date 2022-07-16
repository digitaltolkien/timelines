#!/usr/bin/env python3

import yaml

data = yaml.safe_load(open("data/LR_B_SA.yaml"))

common = data["common"]
prev_date_string = None
for event in data["events"]:
    event.update(common)
    date = event["date"]
    if isinstance(date, str):
        date_string = date.split(".")[1]
    else:
        if "circa" in date:
            date_string = "c." + date["circa"].split(".")[1]
        elif "start" in date:
            date_string = date["start"].split(".")[1] + "–" + date["end"].split(".")[1]

    description = event["description"]
    if date_string == prev_date_string:
        print(f"""<div class="event"><div class="date"></div><div class="description">{description}</div></div>""")
    else:
        print(f"""<div class="event new-date"><div class="date">{date_string}</div><div class="description">{description}</div></div>""")
        prev_date_string = date_string

