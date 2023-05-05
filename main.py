import pandas as pd
import numpy as np
import warnings
import plotly.graph_objects as go
warnings.filterwarnings("ignore", category=FutureWarning)
pd.set_option('display.max_columns', 1000)  # or None
pd.set_option('display.max_rows', 1000)  # or None
pd.set_option('display.max_colwidth', 100)  # or None


def main2():
    df_m_bf = pd.read_csv(
        'C:\\Users\\TARIQOPLATA\\PycharmProjects\\FAERS_final\\data\\data\\Old_gold\\Disprop_analysis_male_with_HTs_before_filtering_v2.csv')
    df_f_bf = pd.read_csv(
        'C:\\Users\\TARIQOPLATA\\PycharmProjects\\FAERS_final\\data\\data\\Old_gold\\Disprop_analysis_female_with_HTs_before_filtering_v2.csv')

    df_f_bf = df_f_bf.drop_duplicates(subset=['DRUG', 'AE', 'Reports', 'IC'], keep='first', ignore_index=True)
    df_m_bf = df_m_bf.drop_duplicates(subset=['DRUG', 'AE', 'Reports', 'IC'], keep='first', ignore_index=True)

    df_m = pd.read_csv(
        'C:\\Users\\TARIQOPLATA\\PycharmProjects\\FAERS_final\\data\\data\\Old_gold\\Disprop_analysis_male_with_HTs.csv')
    df_f = pd.read_csv(
        'C:\\Users\\TARIQOPLATA\\PycharmProjects\\FAERS_final\\data\\data\\Old_gold\\Disprop_analysis_female_with_HTs.csv')

    df_f = df_f.drop_duplicates(subset=['DRUG', 'AE', 'Reports', 'IC'], keep='first', ignore_index=True)
    df_m = df_m.drop_duplicates(subset=['DRUG', 'AE', 'Reports', 'IC'], keep='first', ignore_index=True)

    df_f = df_f.drop(df_f[df_f.Reports <= 5].index)
    df_f = df_f.drop(df_f[df_f.PRR < 2].index)
    df_f = df_f.drop(df_f[df_f.IC025 <= 0].index)

    df_m = df_m.drop(df_m[df_m.Reports <= 5].index)
    df_m = df_m.drop(df_m[df_m.PRR < 2].index)
    df_m = df_m.drop(df_m[df_m.IC025 <= 0].index)

    drugs_bf = df_f['DRUG'].tolist() + df_m['DRUG'].tolist()
    drugs_bf = list(dict.fromkeys(drugs_bf))

    print('MALES')
    total = 0
    for item in drugs_bf:
        df_m_bf2 = df_m[df_m['DRUG'] == item]
        sum = df_m_bf2['Reports'].sum()
        total += sum
        print([item, sum])
    print(['MALE TOTAL ', total])
    total = 0
    print('FEMALES')
    for item in drugs_bf:
        df_f_bf2 = df_f[df_f['DRUG'] == item]
        sum = df_f_bf2['Reports'].sum()
        total += sum
        print([item, sum])
    print(['FEMALE TOTAL ', total])


def main():
    path = 'C:\\Users\\TARIQOPLATA\\PycharmProjects\\FAERS_final'
    df_f = pd.read_csv(path + '\\data\\data\\Old_gold\\Disprop_analysis_female_with_HTs.csv')
    df_m = pd.read_csv(path + '\\data\\data\\Old_gold\\Disprop_analysis_male_with_HTs.csv')
    hts = ['investigations']
    df_f = df_f[df_f['HT'].isin(hts)]
    df_m = df_m[df_m['HT'].isin(hts)]
    df_f = df_f.drop_duplicates(subset=['DRUG', 'AE', 'IC025', 'Reports'], keep='first', ignore_index=True)
    df_m = df_m.drop_duplicates(subset=['DRUG', 'AE', 'IC025', 'Reports'], keep='first', ignore_index=True)
    df_f = df_f.groupby(by=['DRUG'], as_index=False).sum()
    print(['FEMALE ', df_f['IC025'].sum()])
    df_m = df_m.groupby(by=['DRUG'], as_index=False).sum()
    print(['MALE ', df_m['IC025'].sum()])
    df_f = df_f.sort_values(by='IC025', ascending=False)
    df_m = df_m.sort_values(by='IC025', ascending=False)
    #df_f = df_f.head(10)
    #df_m = df_m.head(10)
    print(df_f)
    print('MALE')
    print(df_m)


if __name__ == '__main__':
    main()
