import pandas as pd
import warnings

warnings.filterwarnings("ignore")
pd.set_option('display.max_columns', 1000)  # or None
pd.set_option('display.max_rows', 1000)  # or None
pd.set_option('display.max_colwidth', 100)  # or None

path = 'C:\\Users\\TARIQOPLATA\\PycharmProjects\\FAERS_final\\data\\data\\Old_gold\\'
#path = '/Users/ftk/Documents/Work/FAERS_final/data/Old_gold/'


def main2():
    df_f = pd.read_csv(path + 'Disprop_analysis_female_with_HTs.csv')
    df_m = pd.read_csv(path + 'Disprop_analysis_male_with_HTs.csv')
    df_f = df_f.drop(df_f[df_f.Reports < 5].index)
    df_f = df_f.drop(df_f[df_f.IC025 < 0].index)
    df_f = df_f.drop(df_f[df_f.PRR < 2].index)

    df_m = df_m.drop(df_m[df_m.Reports < 5].index)
    df_m = df_m.drop(df_m[df_m.IC025 < 0].index)
    df_m = df_m.drop(df_m[df_m.PRR < 2].index)

    hts = 'cardiac and vascular investigations (excl enzyme tests)'
    df_f = df_f[df_f['HT_level2'] == hts]
    df_m = df_m[df_m['HT_level2'] == hts]
    df_f = df_f.drop('ROR', axis=1)
    df_f = df_f.drop('PRR', axis=1)
    df_f = df_f.drop('HT_level3', axis=1)
    df_f = df_f.drop('HT_level2', axis=1)
    df_f = df_f.drop('HT', axis=1)
    df_f = df_f.drop('IC', axis=1)
    df_f = df_f.drop('IDX', axis=1)
    df_m = df_m.drop('IDX', axis=1)
    df_m = df_m.drop('ROR', axis=1)
    df_m = df_m.drop('PRR', axis=1)
    df_m = df_m.drop('HT_level3', axis=1)
    df_m = df_m.drop('HT_level2', axis=1)
    df_m = df_m.drop('HT', axis=1)
    df_m = df_m.drop('IC', axis=1)
    df_f = df_f.sort_values(['IC025'], ascending=False)
    df_m = df_m.sort_values(['IC025'], ascending=False)
    print(df_f['IC025'].sum())
    print(df_m['IC025'].sum())
    df_f = df_f.head(20)
    df_m = df_m.head(20)
    #aes = df_f['AE'].tolist() + df_m['AE'].tolist()
    #aes = list(dict.fromkeys(aes))
    print(df_f)
    print(df_m)


def bzds():
    bzd = open('C:\\Users\\TARIQOPLATA\\PycharmProjects\\FAERS_BZD-Gender\\Benzos_list.txt', 'r')
    bzd = bzd.readlines()
    print(bzd)
    benzo_list = []
    for item in bzd:
        if ';' in item:
            items = item.split(';')
            benzo_list.append(items[0].lower())
        elif '\n' in item:
            items = item[:-1]
            benzo_list.append(items.lower())
        else:
            benzo_list.append(item.lower())
    benzo_list = list(dict.fromkeys(benzo_list))
    print(len(benzo_list))
    print(benzo_list)
    file = open('Benzodiazepine_list.txt', 'w')
    for item in benzo_list:
        txt = item + '\n'
        file.write(txt)
    file.close()


def main():
    df_f = pd.read_csv(path + 'Disprop_analysis_female_with_HTs.csv')
    df_m = pd.read_csv(path + 'Disprop_analysis_male_with_HTs.csv')
    print(df_f)
    df_m.to_excel('FAERS_data_male.xlsx')


if __name__ == '__main__':
    main()
