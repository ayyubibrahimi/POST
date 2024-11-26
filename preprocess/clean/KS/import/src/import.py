# Authors: LB
# Mainrainers: LB
# Copyright:   2023, HRDAG, GPL v2 or later
# =========================================
# us-post-data/preprocess/clean/KS/import/src
import pandas as pd
from pathlib import Path
from nameparser import HumanName


def clean_names(df):
    out = df
    hn = out.officer_name.apply(HumanName)
    out['last_name']      = hn.apply(lambda x: x.last)
    out['first_name']     = hn.apply(lambda x: x.first)
    out['middle_name']    = hn.apply(lambda x: x.middle)
    out['middle_initial'] = hn.apply(lambda x: x.middle[:1])
    out['suffix']         = hn.apply(lambda x: x.suffix)
    return out

if __name__ == "__main__":
    data_input = Path("../input/")
    complete =  pd.concat(pd.read_excel(x,skiprows=4,usecols="c:k")
                       for x in data_input.glob("*.xls"))
    complete.columns  =  complete.columns.str.lower()
    complete.columns = complete.columns.str.replace(" ", "_")
    new_complete = clean_names(complete)
    new_complete.drop(["unnamed:_3","unnamed:_4"], axis=1, inplace=True)
    new_complete.head()
