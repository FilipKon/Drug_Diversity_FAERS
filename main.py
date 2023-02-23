import pandas as pd

path = 'C:\\Users\\TARIQOPLATA\\PycharmProjects\\FAERS_final\\data\\data\\Old_gold\\'


# path = '\Users\'


def main():
    df_f = pd.read_csv(path + 'Disprop_analysis_female_with_HTs.csv')
    df_m = pd.read_csv(path + 'Disprop_analysis_male_with_HTs.csv')
    hts = 'neurological disorders nec'
    df_f = df_f[df_f['HT_level2'] == hts]
    df_m = df_m[df_m['HT_level2'] == hts]
    aes = df_m['AE'].tolist() + df_f['AE'].tolist()
    aes = list(dict.fromkeys(aes))
    print(aes)


if __name__ == '__main__':
    main()
