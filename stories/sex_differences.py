import pandas as pd

path = 'C:\\Users\\TARIQOPLATA\\PycharmProjects\\FAERS_final\\data\\Old_gold\\'


# path = '\Users\'


def main():
    df_f = pd.read_csv(path + 'Disprop_analysis_female_with_HTs.csv')
    df_m = pd.read_csv(path + 'Disprop_analysis_male_with_HTs.csv')


if __name__ == '__main__':
    main()
