import pandas as pd
import warnings
import numpy as np
"""
    CREATE  A  ,  B  = A+B (AB)
            C  ,  D  = C+D (CD)
            A+C, B+D = A+B+C+D (N)
            (AC),(BD)

    A = DRUG/AE REPORTS
    B = AE TOTAL REPORTS - DRUG/AE REPORTS
    C = DRUG TOTAL REPORTS - DRUG/AE REPORTS
    D = TOTAL OF ALL OTHER DRUG REPORTS WITH ALL OTHER AES
"""

path = "C:\\Users\\TARIQOPLATA\\PycharmProjects\\FAERSA\\data\\FAERS_published\\"


def get_drug_total_reports(drug):
    df = pd.read_csv(path + 'Drugs_Gender_Size.csv')
    df = df.loc[df['DRUG'] == drug, 'Reports'].sum()
    return df


def get_ae_total_reports(ae):
    df = pd.read_csv(path + 'FINISHED_FULLRES.csv')
    df = df.drop('DRUG', axis=1)
    summ = df.loc[df['AE'] == ae, 'Reports'].sum()
    return summ


def get_all_other_drug_ae_reports(drug, ae):
    df = pd.read_csv(path + 'FINISHED_FULLRES.csv')
    df = df.loc[(df['DRUG'] != drug) & (df['AE'] != ae), 'Reports'].sum()
    return df


def calc_conti_gender(gender, path_1):
    benzos = get_benzos()
    benzos = list(dict.fromkeys(benzos))
    df_conti = pd.DataFrame(columns=['DRUG', 'AE', 'A', 'B', 'C', 'D', 'N'])
    df = pd.read_csv(path_1)
    df.drop(df[df.Sex != gender].index, inplace=True)

    df_ae = pd.read_csv(path + 'FINISHED_FULLRES.csv')
    df_ae = df_ae.drop('DRUG', axis=1)
    df_ae.drop(df_ae[df_ae.Sex != gender].index, inplace=True)

    df_d = pd.read_csv(path + 'Drugs_Gender_Size.csv')
    df_d.drop(df_d[df_d.Sex != gender].index, inplace=True)

    df_all = pd.read_csv(path + 'FINISHED_FULLRES.csv')
    df_all.drop(df_all[df_all.Sex != gender].index, inplace=True)
    i = 0
    max = len(benzos)
    for item in benzos:
        df_fil = df.loc[df['DRUG'] == item]
        all_aes = df_fil['AE'].tolist()
        j = 0
        max2 = len(all_aes)
        for ae in all_aes:
            a = df.loc[(df['DRUG'] == item) & (df['AE'] == ae), 'Reports'].sum()
            ae_totals = df_ae.loc[df_ae['AE'] == ae, 'Reports'].sum()
            b = ae_totals - a
            drug_totals = df_d.loc[df_d['DRUG'] == item, 'Reports'].sum()
            c = drug_totals - a
            all_others = df_all.loc[(df_all['DRUG'] != item) & (df_all['AE'] != ae), 'Reports'].sum()
            d = all_others
            print([item, ae, a, b, c, d, i, max, j, max2])
            j += 1
            n = a + b + c + d
            df_conti = df_conti.append({'DRUG': item, 'AE': ae, 'A': a, 'B': b, 'C': c, 'D': d, 'N': n},
                                       ignore_index=True)
        i += 1
    name = 'contingency_table_NEWESTOKE_' + gender + '.csv'
    df_conti.to_csv(name)
    print([name, ' DONE .....'])


def get_ae():
    df = pd.read_csv(path + '/ADVERSE_REACTIONS.txt', sep='$')
    df = df.drop('PERIOD', axis=1)
    return df


def get_demo():
    df = pd.read_csv(path + '/DEMOGRAPHICS.txt', sep='$')
    df = df.drop('fda_dt', axis=1)
    df = df.drop('I_F_COD', axis=1)
    df = df.drop('event_dt', axis=1)
    df = df.drop('Period', axis=1)
    df = df.drop('caseid', axis=1)
    df = df.drop('caseversion', axis=1)
    df['Gender'] = df['Gender'].replace('', 'UNK', regex=True)
    df['Gender'].fillna('', inplace=True)
    df['Gender'] = df['Gender'].replace(np.nan, 'UNK', regex=True)
    df['Gender'] = df['Gender'].replace('', 'UNK', regex=True)
    df['Gender'] = df['Gender'].replace(' ', 'UNK', regex=True)
    return df


def get_drugs():
    df = pd.read_csv('C:\\Users\\TARIQOPLATA\\PycharmProjects\\FAERS_BZD-Gender\\data\\Khaleel2022\\DRUGS_STANDARDIZED.txt', sep='$')
    df = df.drop('PERIOD', axis=1)
    df = df.drop('DRUG_ID', axis=1)
    df = df.drop('RXAUI', axis=1)
    # df = df.drop('DRUG_SEQ', axis=1)
    return df


def get_source():
    df = pd.read_csv(path + '/REPORT_SOURCES.txt', sep='$')
    df = df.drop('PERIOD', axis=1)
    return df


def get_indi():
    df = pd.read_csv(path + '/DRUG_INDICATIONS.txt', sep='$')
    df = df.drop('PERIOD', axis=1)
    return df


def merge_data():
    df_ae = get_ae()
    df_demo = get_demo()
    df_indi = get_indi()
    df_source = get_source()
    df_drugs = get_drugs()
    df = pd.merge(df_demo, df_ae, on=['primaryid'])
    df = pd.merge(df_drugs, df, on=['primaryid'])
    df = pd.merge(df_source, df, on=['primaryid'])
    df = pd.merge(df_indi, df, on=['primaryid', 'DRUG_SEQ'])
    df = df.drop('DRUG_SEQ', axis=1)
    df = df.drop_duplicates(subset=['DRUG', 'Gender', 'primaryid', 'ADVERSE_EVENT', 'DRUG_INDICATION', 'RPSR_COD'], keep='first',
                            ignore_index=True)
    df.to_csv('Merged_data_Indis.csv')
    print(df)
    return df


def count_data(df):
    df2 = df.groupby(['DRUG_INDICATION', 'Gender']).size()
    df2.to_csv('Drug_Indication_Gender_Size.csv')
    df5 = df.groupby(['DRUG', 'Gender', 'ADVERSE_EVENT', 'DRUG_INDICATION']).size()
    df5.to_csv('Gender_Fullresults_DRUGGENDERAEINDI.csv')
    # df3 = df.groupby(['DRUG_INDICATION']).size()
    # df3.to_csv('Gender_Fullresults_INDICATION.csv')
    # print(df3)


def main():
    print('LETS GO')
    df = merge_data()
    print('MERGE FINISHED')
    count_data(df)
    print('COUNT FINISHED')
    #calc_conti_gender('M', path_1)
    #calc_conti_gender('F', path_1)


if __name__ == '__main__':
    main()