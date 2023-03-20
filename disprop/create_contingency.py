import pandas as pd
import warnings

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
    
  def main():
    # path = 'C:\\Users\\TARIQOPLATA\\PycharmProjects\\FAERS_BZD-Gender\\data\\General_data\\'
    path_1 = 'C:\\Users\\TARIQOPLATA\\PycharmProjects\\FAERS_BZD-Gender\\data\\FINAL\\' + 'FINISHED_FULLRES.csv'
    #df = pd.read_csv(path_1)
    #change_aes(df)
    # df = df[df['DRUG'] == 'alprazolam']
    # df = df[df['Gender'] == 'M']
    # sum = df['0'].sum()
    # print(sum)
    #meddra_check(df)
    calc_conti_gender('M', path_1)
    calc_conti_gender('F', path_1)
