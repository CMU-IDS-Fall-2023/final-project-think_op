import pandas as pd

if __name__ == '__main__':
    df1 = pd.read_excel('data\gtd_1970_2020.xlsx')
    df2 = pd.read_excel('data\gtd_Jan_June_2021.xlsx')
    df = pd.concat([df1,df2])

    # Save to csv
    # Can't upload to github. CSV too large
    df.to_csv('data\gtd_1970_2021.csv', index=False)