import pandas as pd
import numpy as np
import warnings
warnings.filterwarnings("ignore", category=FutureWarning)


def main():
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


if __name__ == '__main__':
    main()
