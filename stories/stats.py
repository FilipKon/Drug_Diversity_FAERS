import pandas as pd


pd.set_option('display.max_columns', 1000)  # or None
pd.set_option('display.max_rows', 1000)  # or None
pd.set_option('display.max_colwidth', 100)  # or None

path = 'C:\\Users\\TARIQOPLATA\\PycharmProjects\\FAERS_final\\data\\data\\Old_gold\\'

def get_benzos(df):
    translator = open('C:\\Users\\TARIQOPLATA\\PycharmProjects\\FAERS_BZD-Gender\\Benzos_list.txt', 'r')
    translator = translator.readlines()
    benzos = []
    for item in translator:
        items = item.split(';')
        for drugs in items:
            if '\n' in drugs:
                drugs = drugs[:-1]
            benzos.append(drugs.lower())
    df = df[df['DRUG'].isin(benzos)]
    return df


def overview():
    # df_before_filt = pd.read_csv(
    #    'C:\\Users\\TARIQOPLATA\\PycharmProjects\\FAERS_final\\data\\data\\New\\FINISHED_FULLRES.csv')
    df = pd.read_csv('C:\\Users\\TARIQOPLATA\\PycharmProjects\\FAERS_BZD-Gender\\data\\Khaleel2022\\DEMOGRAPHICS.txt',
                     sep='$')
    ids = df['primaryid'].tolist()
    ids = list(dict.fromkeys(ids))
    print(len(ids))
    print('FEMALE')
    df_f = df[df['Gender'] == 'F']
    ids_f = df_f['primaryid'].tolist()
    ids_f = list(dict.fromkeys(ids_f))
    print(len(ids_f))
    print('MALE')
    df_m = df[df['Gender'] == 'M']
    ids_m = df_m['primaryid'].tolist()
    ids_m = list(dict.fromkeys(ids_m))
    print(len(ids_m))
    filter_benzos(ids_f, ids_m)


def filter_benzos(ids_f, ids_m):
    df = pd.read_csv('C:\\Users\\TARIQOPLATA\\PycharmProjects\\FAERS_BZD-Gender\\data\\Khaleel2022\\DRUG_ADVERSE_REACTIONS_Pairs.txt', sep='$')
    df = get_benzos(df)
    df_m = df[df['primaryid'].isin(ids_m)]
    ids = df_m['primaryid'].tolist()
    print('ALL MALE IDS')
    print(len(ids))
    print('UNIQUE MALE IDS')
    ids = list(dict.fromkeys(ids))
    print(len(ids))

    df_f = df[df['primaryid'].isin(ids_f)]
    ids = df_f['primaryid'].tolist()
    print('ALL FEMALE IDS')
    print(len(ids))
    print('UNIQUE FEMALE IDS')
    ids = list(dict.fromkeys(ids))
    print(len(ids))


def pipeline():
    df_f = pd.read_csv(path + 'Disprop_analysis_female_with_HTs_before_filtering_v2.csv')
    df_m = pd.read_csv(path + 'Disprop_analysis_male_with_HTs_before_filtering_v2.csv')
    df_f = df_f.drop_duplicates(subset=['DRUG', 'AE', 'Reports', 'IC025'])
    df_m = df_m.drop_duplicates(subset=['DRUG', 'AE', 'Reports', 'IC025'])
    drugs = df_f['DRUG'].tolist()
    drugs = list(dict.fromkeys(drugs))
    print('FEMALE BEFORE FILTERING')
    print(len(drugs))
    print(drugs)
    aes = df_f['Reports'].sum()
    print(['Reports sum ', aes])

    drugs = df_m['DRUG'].tolist()
    drugs = list(dict.fromkeys(drugs))
    print('MALE BEFORE FILTERING')
    print(len(drugs))
    print(drugs)
    aes = df_m['Reports'].sum()
    print(['AES ', aes])

    df_f = pd.read_csv(path + 'Disprop_analysis_female_with_HTs.csv')
    df_m = pd.read_csv(path + 'Disprop_analysis_male_with_HTs.csv')
    df_f = df_f.drop_duplicates(subset=['DRUG', 'AE', 'Reports', 'IC025'])
    df_m = df_m.drop_duplicates(subset=['DRUG', 'AE', 'Reports', 'IC025'])
    df_f = df_f.drop(df_f[df_f.Reports <= 5].index)
    df_f = df_f.drop(df_f[df_f.IC025 <= 0].index)
    df_f = df_f.drop(df_f[df_f.PRR < 2].index)

    df_m = df_m.drop(df_m[df_m.Reports <= 5].index)
    df_m = df_m.drop(df_m[df_m.IC025 <= 0].index)
    df_m = df_m.drop(df_m[df_m.PRR < 2].index)

    drugs = df_f['DRUG'].tolist()
    drugs = list(dict.fromkeys(drugs))
    print('FEMALE AFTER FILTERING')
    print(len(drugs))
    print(drugs)
    aes = df_f['AE'].tolist()
    aes = list(dict.fromkeys(aes))
    print(['AES ', len(aes)])
    aes = df_f['Reports'].sum()
    print(['Reports sum ', aes])

    drugs = df_m['DRUG'].tolist()
    drugs = list(dict.fromkeys(drugs))
    print('MALE AFTER FILTERING')
    print(len(drugs))
    print(drugs)
    aes = df_m['AE'].tolist()
    aes = list(dict.fromkeys(aes))
    print(['AES ', len(aes)])
    aes = df_m['Reports'].sum()
    print(['Reports sum ', aes])


def main():
    pipeline()


if __name__ == '__main__':
    main()
