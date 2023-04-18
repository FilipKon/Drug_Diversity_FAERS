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


def get_benzos(df):
    translator = open('C:\\Users\\TARIQOPLATA\\PycharmProjects\\FAERS_BZD-Gender\\Benzos_list.txt', 'r')
    translator = translator.readlines()
    benzos = []
    for item in translator:
        items = item.split(';')
        for drugs in items:
            if '\n' in drugs:
                drugs = drugs[:-1]
            #if drugs.lower() in df:
            benzos.append(drugs.lower())
    return benzos


def calc_conti_gender(gender, path_1, df):
    benzos = get_benzos(df)
    benzos = list(dict.fromkeys(benzos))
    df_conti = pd.DataFrame(columns=['DRUG', 'AE', 'A', 'B', 'C', 'D', 'N'])
    df = pd.read_csv(path_1 + 'Gender_Fullresults_HP.csv')
    df.drop(df[df.Gender != gender].index, inplace=True)

    df_ae = pd.read_csv(path_1 + 'Gender_Fullresults_HP.csv')
    df_ae = df_ae.drop('DRUG', axis=1)
    df_ae.drop(df_ae[df_ae.Gender != gender].index, inplace=True)

    df_d = pd.read_csv(path_1 + 'Drugs_Gender_Size_HP.csv')
    df_d.drop(df_d[df_d.Gender != gender].index, inplace=True)

    df_all = pd.read_csv(path_1 + 'Gender_Fullresults_HP.csv')
    df_all.drop(df_all[df_all.Gender != gender].index, inplace=True)
    i = 0
    max = len(benzos)
    for item in benzos:
        df_fil = df.loc[df['DRUG'] == item]
        all_aes = df_fil['ADVERSE_EVENT'].tolist()
        j = 0
        max2 = len(all_aes)
        for ae in all_aes:
            a = df.loc[(df['DRUG'] == item) & (df['ADVERSE_EVENT'] == ae), '0'].sum()
            ae_totals = df_ae.loc[df_ae['ADVERSE_EVENT'] == ae, '0'].sum()
            b = ae_totals - a
            drug_totals = df_d.loc[df_d['DRUG'] == item, '0'].sum()
            c = drug_totals - a
            all_others = df_all.loc[(df_all['DRUG'] != item) & (df_all['ADVERSE_EVENT'] != ae), '0'].sum()
            d = all_others
            print([item, ae, a, b, c, d, i, max, j, max2])
            j += 1
            n = a + b + c + d
            df_new = pd.DataFrame([{'DRUG': item, 'AE': ae, 'A': a, 'B': b, 'C': c, 'D': d, 'N': n}])
            df_conti = pd.concat([df_conti, df_new], axis=0, ignore_index=True)
            #df_conti = pd.concat([pd.DataFrame(row, index=[key])], axis=1, ignore_index=True) 
            print(df_conti)
            #df_conti = pd.concat({'DRUG': item, 'AE': ae, 'A': a, 'B': b, 'C': c, 'D': d, 'N': n}, axis=0,
            #                           ignore_index=True)
        i += 1
    name = 'contingency_table_HP_' + gender + '.csv'
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
    #df_indi = get_indi()
    df_source = get_source()
    df_drugs = get_drugs()
    df = pd.merge(df_demo, df_ae, on=['primaryid'])
    df = pd.merge(df_drugs, df, on=['primaryid'])
    df = pd.merge(df_source, df, on=['primaryid'])
    #df = pd.merge(df_indi, df, on=['primaryid', 'DRUG_SEQ'])
    #df = df.drop('DRUG_SEQ', axis=1)
    df = df.drop_duplicates(subset=['DRUG', 'Gender', 'primaryid', 'ADVERSE_EVENT', 'RPSR_COD'], keep='first',
                            ignore_index=True)
    df.to_csv('Merged_data_II.csv')
    print(df)
    return df


def count_data(df):
    #df2 = df.groupby(['DRUG_INDICATION', 'Gender']).size()
    #df2.to_csv('Drug_Indication_Gender_Size.csv')
    df5 = df.groupby(['DRUG', 'Gender', 'ADVERSE_EVENT']).size()
    df5.to_csv('Gender_Fullresults_HP.csv')
    df1 = df.groupby(['DRUG', 'Gender']).size()
    df1.to_csv('Drugs_Gender_Size_HP.csv')
    #df3 = df.groupby(['DRUG_INDICATION']).size()
    #df3.to_csv('Gender_Fullresults_INDICATION.csv')
    # print(df3)


def main():
    #df = merge_data()
    #count_data(df)
    df = pd.read_csv('C:\\Users\\TARIQOPLATA\\PycharmProjects\\FAERS_final\\create_dataset\\Merged_data_II.csv')
    index_names = df[df['RPSR_COD'] != 'HP'].index
    df = df.drop(index_names)
    df.to_csv('Fullresults_HP.csv')
    count_data(df)
    calc_conti_gender('M', 'C:\\Users\\TARIQOPLATA\\PycharmProjects\\FAERS_final\\create_dataset\\', df)
    calc_conti_gender('F', 'C:\\Users\\TARIQOPLATA\\PycharmProjects\\FAERS_final\\create_dataset\\', df)


if __name__ == '__main__':
    main()