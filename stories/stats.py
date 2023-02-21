import pandas as pd


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


def main():
    overview()


if __name__ == '__main__':
    main()
