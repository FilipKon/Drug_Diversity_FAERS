import pandas as pd
pd.set_option('display.max_columns', 100)  # or 1000
pd.set_option('display.max_rows', 100)  # or 1000
pd.set_option('display.max_colwidth', 100)  # or 199

path = 'C:\\Users\\TARIQOPLATA\\PycharmProjects\\FAERS_final\\data\\data\\Old_gold\\'
# path = '\Users\'


def main():
    df_f = pd.read_csv(path + 'Disprop_analysis_female_with_HTs.csv')
    df_m = pd.read_csv(path + 'Disprop_analysis_male_with_HTs.csv')
    hts = ['psychiatric disorders', 'nervous system disorders']
    df_f = df_f[df_f['HT'].isin(hts)]
    df_m = df_m[df_m['HT'].isin(hts)]
    df_m['Sex'] = 'M'
    df_f['Sex'] = 'F'
    df_f = df_f.drop('IDX', axis=1)
    df_m = df_m.drop('IDX', axis=1)
    #frames = [df_f, df_m]
    #df = pd.concat(frames)
    #df = df.sort_values(by=['IC025'], ascending=False)
    df_m = df_m.sort_values(by=['IC025'], ascending=False)
    df_f = df_f.sort_values(by=['IC025'], ascending=False)
    print(df_f)


if __name__ == '__main__':
    main()
