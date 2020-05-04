#! /usr/bin/env python

import numpy as np
import pandas as pd


def main():
    data = {
        "language": [
            "Python",
            "C",
            "Java",
            "GO",
            np.nan,
            "SQL",
            "PHP",
            "Python"],
        "score": [
            1,
            2,
            np.nan,
            4,
            5,
            6,
            7,
            10]}
    df = pd.DataFrame(data)
    print(df)
    df.to_csv('example_data.csv')


if __name__ == '__main__':
    main()
