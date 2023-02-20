import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import settings
import warnings

warnings.filterwarnings("ignore")
pd.set_option('display.max_columns', 1000)  # or None
pd.set_option('display.max_rows', 1000)  # or None
pd.set_option('display.max_colwidth', 100)  # or None

# path = 'C:\\Users\\TARIQOPLATA\\PycharmProjects\\FAERS_final\\data\\Old_gold\\'
path = '/Users/ftk/Documents/Work/FAERS_final'


def reports_perc(df, ht2):
    print(df.columns)
    dfx = df.sort_values(['DRUG'], ascending=False, ignore_index=True, kind="mergesort")
    #dfx = df['DRUG'].sort_values(ascending=False, ignore_index=True, kind="mergesort")
    figBAR = px.bar(dfx, x="Reports_Percent", y="DRUG", color='Sex', barmode='group', color_discrete_map=settings.colors_g,
                    title=ht2, orientation='h', hover_data=['AE'])
    figBAR.show()
    figBAR.write_html(path + 'psychiatricdisordersnec.html')


def main():
    df_f = pd.read_csv(path + '/data/Old_gold/Disprop_analysis_female_with_HTs.csv')
    df_m = pd.read_csv(path + '/data/Old_gold/Disprop_analysis_male_with_HTs.csv')
    # anxiety disorders and symptoms
    # sleep disorders and disturbances (incl subtypes)
    # suicide and self-injurous behaviours nec
    # psychiatric disorders nec
    hts = ['sleep disorders and disturbances', 'sleep disturbances (incl subtypes)']
    df_m1 = df_m[df_m['HT_level2'] == 'psychiatric disorders nec']
    df_f1 = df_f[df_f['HT_level2'] == 'psychiatric disorders nec']
    df_f1['Sex'] = 'F'
    df_m1['Sex'] = 'M'
    frames = [df_f1, df_m1]
    df = pd.concat(frames)
    df = df.drop_duplicates(subset=['DRUG', 'AE', 'IC025', 'Reports'], keep='first')
    df_drug = pd.read_csv(path + '/data/New/Drugs_Gender_Size.csv')
    df_fin = pd.DataFrame(columns=['DRUG', 'AE', 'Sex', 'Reports', 'Reports_Percent', 'IC025', 'Total_Reports'])
    for index, row in df.iterrows():
        df_sub_drug = df_drug[df_drug['DRUG'] == row['DRUG']]
        df_sub_drug = df_sub_drug[df_sub_drug['Sex'] == row['Sex']]
        ae_perc = (row['Reports'] / df_sub_drug['Reports'].values[0]) * 100
        ae_perc = round(ae_perc, 3)
        if row['DRUG'] == 'cinolazepam':
            print(row['DRUG'])
            print(type(row['DRUG']))
        df_fin = df_fin.append({'DRUG': str(row['DRUG']), 'AE': row['AE'], 'Sex': row['Sex'], 'Reports': row['Reports'],
                                'Reports_Percent': ae_perc, 'IC025': row['IC025'],
                                'Total_Reports': df_sub_drug['Reports'].values[0]},
                               ignore_index=True)
    #print(df_fin)
    df_fin['DRUG'] = df_fin["DRUG"].map(str)

    reports_perc(df_fin, 'psychiatric disorders nec')


if __name__ == '__main__':
    main()
