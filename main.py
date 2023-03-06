import pandas as pd

#path = 'C:\\Users\\TARIQOPLATA\\PycharmProjects\\FAERS_final\\data\\data\\Old_gold\\'
path = '/Users/ftk/Documents/Work/FAERS_final/data/Old_gold/'


def main():
    df_f = pd.read_csv(path + 'Disprop_analysis_female_with_HTs.csv')
    df_m = pd.read_csv(path + 'Disprop_analysis_male_with_HTs.csv')
    hts = 'neurological disorders nec'
    df_f = df_f[df_f['HT_level2'] == hts]
    df_m = df_m[df_m['HT_level2'] == hts]
    aes = ['logorrhoea', 'arousal', 'reslessness']
    df_f = df_f[df_f['AE'] == aes]
    df_m = df_m[df_m['AE'] == aes]


if __name__ == '__main__':
    main()
