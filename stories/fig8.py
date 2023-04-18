import pandas as pd
import plotly.express as px
import warnings
import numpy as np
import plotly.graph_objs as go

warnings.filterwarnings("ignore")
pd.set_option('display.max_columns', 1000)  # or None
pd.set_option('display.max_rows', 1000)  # or None
pd.set_option('display.max_colwidth', 100)  # or None

colors_d = {'alprazolam': '#FF5733', 'diazepam': '#75A7AB', 'lorazepam': '#B73C22', 'clonazepam': '#906056',
            'zolpidem': '#9DF8DF', 'tetrazepam': '#ff9d5c', 'cloxazolam': '#4b4c07', 'clotiazepam': '#e9fe92',
            'flumazenil': '#D6DA03', 'triazulenone': '#FFD4EB', 'quazepam': '#F9C469', 'nordazepam': '#68D6DF',
            'tofisopam': '#C3C553', 'mexazolam': '#BEFC8B', 'medazepam': '#27FFC4', 'ketazolam': '#636161',
            'cinolazepam': '#C5A9A3', 'oxazolam': '#5FB815', 'lormetazepam': '#ee99ac', 'prazepam': '#FF0087',
            'flunitrazepam': '#FB11FF', 'nitrazepam': '#E49C20', 'estazolam': '#8E3564', 'ethyl loflazepate': '#FBB4FC',
            'etizolam': '#0CC492', 'brotizolam': '#B498FF', 'clorazepate': '#0CC44C', 'triazolam': '#1349C4',
            'chlordiazepoxide': '#dfcfe9', 'flurazepam': '#75AB9C', 'zaleplon': '#18E4F5', 'eszopiclone': '#00B9FF',
            'temazepam': '#82F721', 'zopiclone': '#458AA4', 'bromazepam': '#4562A4', 'oxazepam': '#A585C4',
            'clobazam': '#2C6CFF', 'midazolam': '#98B7FF', 'remimazolam': '#8000FF'}
colors_d_full = {'alprazolam': 'rgba(255, 87, 51, 1)', 'diazepam': 'rgba(117, 167, 171, 1)',
                 'lorazepam': 'rgba(183, 60, 34, 1)', 'clonazepam': 'rgba(144, 96, 86, 1)',
                 'zolpidem': 'rgba(157, 248, 223, 1)', 'tetrazepam': 'rgba(255, 157, 92, 1)',
                 'cloxazolam': 'rgba(75, 76, 7, 1)', 'clotiazepam': 'rgba(233, 254, 146, 1)',
                 'flumazenil': 'rgba(214, 218, 3, 1)', 'triazulenone': 'rgba(255, 212, 235, 1)',
                 'quazepam': 'rgba(249, 196, 105, 1)', 'nordazepam': 'rgba(104, 214, 223, 1)',
                 'tofisopam': 'rgba(195, 197, 83, 1)', 'mexazolam': 'rgba(190, 252, 139, 1)',
                 'medazepam': 'rgba(39, 255, 196, 1)', 'ketazolam': 'rgba(99, 97, 97, 1)',
                 'cinolazepam': 'rgba(197, 169, 163, 1)', 'oxazolam': 'rgba(95, 184, 21, 1)',
                 'lormetazepam': 'rgba(238, 153, 172, 1)', 'prazepam': 'rgba(255, 0, 135, 1)',
                 'flunitrazepam': 'rgba(251, 17, 255, 1)', 'nitrazepam': 'rgba(228, 156, 32, 1)',
                 'estazolam': 'rgba(142, 53, 100, 1)', 'ethyl loflazepate': 'rgba(251, 180, 252, 1)',
                 'etizolam': 'rgba(12, 196, 146, 1)', 'brotizolam': 'rgba(180, 152, 255, 1)',
                 'clorazepate': 'rgba(12, 196, 76, 1)', 'triazolam': 'rgba(19, 73, 196, 1)',
                 'chlordiazepoxide': 'rgba(223, 207, 233, 1)', 'flurazepam': 'rgba(117, 171, 156, 1)',
                 'zaleplon': 'rgba(24, 228, 245, 1)', 'eszopiclone': 'rgba(0, 185, 255, 1)',
                 'temazepam': 'rgba(130, 247, 33, 1)', 'zopiclone': 'rgba(69, 138, 164, 1)',
                 'bromazepam': 'rgba(69, 98, 164, 1)', 'oxazepam': 'rgba(165, 133, 196, 1)',
                 'clobazam': 'rgba(44, 108, 255, 1)', 'midazolam': 'rgba(152, 183, 255, 1)',
                 'remimazolam': 'rgba(128, 0, 255, 1)'}
colors_d_opa = {'alprazolam': 'rgba(255, 87, 51, 0.15)', 'diazepam': 'rgba(117, 167, 171, 0.15)',
                'lorazepam': 'rgba(183, 60, 34, 0.15)', 'clonazepam': 'rgba(144, 96, 86, 0.15)',
                'zolpidem': 'rgba(157, 248, 223, 0.15)', 'tetrazepam': 'rgba(255, 157, 92, 0.15)',
                'cloxazolam': 'rgba(75, 76, 7, 0.15)', 'clotiazepam': 'rgba(233, 254, 146, 0.15)',
                'flumazenil': 'rgba(214, 218, 3, 0.15)', 'triazulenone': 'rgba(255, 212, 235, 0.15)',
                'quazepam': 'rgba(249, 196, 105, 0.15)', 'nordazepam': 'rgba(104, 214, 223, 0.15)',
                'tofisopam': 'rgba(195, 197, 83, 0.15)', 'mexazolam': 'rgba(190, 252, 139, 0.15)',
                'medazepam': 'rgba(39, 255, 196, 0.15)', 'ketazolam': 'rgba(99, 97, 97, 0.15)',
                'cinolazepam': 'rgba(197, 169, 163, 0.15)', 'oxazolam': 'rgba(95, 184, 21, 0.15)',
                'lormetazepam': 'rgba(238, 153, 172, 0.15)', 'prazepam': 'rgba(255, 0, 135, 0.15)',
                'flunitrazepam': 'rgba(251, 17, 255, 0.15)', 'nitrazepam': 'rgba(228, 156, 32, 0.15)',
                'estazolam': 'rgba(142, 53, 100, 0.15)', 'ethyl loflazepate': 'rgba(251, 180, 252, 0.15)',
                'etizolam': 'rgba(12, 196, 146, 0.15)', 'brotizolam': 'rgba(180, 152, 255, 0.15)',
                'clorazepate': 'rgba(12, 196, 76, 0.15)', 'triazolam': 'rgba(19, 73, 196, 0.15)',
                'chlordiazepoxide': 'rgba(223, 207, 233, 0.15)', 'flurazepam': 'rgba(117, 171, 156, 0.15)',
                'zaleplon': 'rgba(24, 228, 245, 0.15)', 'eszopiclone': 'rgba(0, 185, 255, 0.15)',
                'temazepam': 'rgba(130, 247, 33, 0.15)', 'zopiclone': 'rgba(69, 138, 164, 0.15)',
                'bromazepam': 'rgba(69, 98, 164, 0.15)', 'oxazepam': 'rgba(165, 133, 196, 0.15)',
                'clobazam': 'rgba(44, 108, 255, 0.15)', 'midazolam': 'rgba(152, 183, 255, 0.15)',
                'remimazolam': 'rgba(128, 0, 255, 0.15)'}
symbols_d = {'alprazolam': "/", 'diazepam': ".", 'lorazepam': "x", 'clonazepam': "-",
             'zolpidem': "/", 'tetrazepam': "+", 'cloxazolam': ".",
             'flumazenil': "/", 'triazulenone': "x", 'quazepam': "-", 'nordazepam': "|",
             'tofisopam': "+", 'mexazolam': ".", 'ketazolam': "/",
             'cinolazepam': "x", 'oxazolam': "-", 'lormetazepam': "|", 'prazepam': "+",
             'flunitrazepam': ".", 'estazolam': "/", 'ethyl loflazepate': "",
             'etizolam': "-", 'brotizolam': "|", 'clorazepate': "+", 'triazolam': ".",
             'flurazepam': "/", 'zaleplon': "x", 'eszopiclone': "-",
             'zopiclone': "+", 'bromazepam': "/", 'oxazepam': "x", "nitrazepam": "x",
             'clobazam': "/", 'midazolam': "x", 'remimazolam': "-"}
symbols = {'alprazolam': 'circle', 'diazepam': 'hexagon', 'lorazepam': 'star', 'clonazepam': 'square',
           'zolpidem': 'diamond', 'tetrazepam': 'cross', 'cloxazolam': 'x', 'clotiazepam': 'star-triangle-up-open',
           'flumazenil': 'pentagon', 'triazulenone': 'hourglass', 'quazepam': 'octagon', 'nordazepam': 'arrow',
           'tofisopam': 'arrow-down', 'mexazolam': 'circle-cross', 'medazepam': 'diamond-wide', 'ketazolam': 'bowtie',
           'cinolazepam': 'star-square', 'oxazolam': 'hexagram', 'lormetazepam': 'diamond-open',
           'prazepam': 'circle-open', 'midazolam': 'triangle-left-open',
           'flunitrazepam': 'x-open', 'nitrazepam': 'circle-x', 'estazolam': 'triangle-ne',
           'ethyl loflazepate': 'pentagon-open',
           'etizolam': 'star-open', 'brotizolam': 'triangle-left', 'clorazepate': 'square-open',
           'triazolam': 'arrow-open',
           'chlordiazepoxide': 'square-open', 'flurazepam': 'triangle-right', 'zaleplon': 'diamond-tall',
           'eszopiclone': 'star-square-open',
           'temazepam': 'bowtie-open', 'zopiclone': 'asterisk-open', 'bromazepam': 'triangle-right-open',
           'oxazepam': 'hexagon2-open', 'clobazam': 'triangle-se', 'triangle-sw': 'hash', 'remimazolam': 'diamond-open'}


def main():
    path = 'C:\\Users\\TARIQOPLATA\PycharmProjects\\FAERS_final\\data\\data\\Old_gold\\'
    # path = '/Users/ftk/Documents/Work/FAERS_final/data/Old_gold/'
    df_f = pd.read_csv(path + 'Disprop_analysis_female_with_HTs.csv')
    df_m = pd.read_csv(path + 'Disprop_analysis_male_with_HTs.csv')
    hts = ['nervous system disorders', 'psychiatric disorders']
    df_f = df_f[df_f['HT'].isin(hts)]
    df_m = df_m[df_m['HT'].isin(hts)]
    # df_f = df_f.groupby(by=['AE']).sum()
    # df_m = df_m.groupby(by=['AE']).sum()
    df_f['Sex'] = 'F'
    df_m['Sex'] = 'M'
    frames = [df_f, df_m]
    df = pd.concat(frames)
    df = df.drop_duplicates(subset=['DRUG', 'AE', 'Sex', 'IC025'], keep='first', ignore_index=True)
    total_df = pd.DataFrame(columns=['DRUG', 'AE', 'Ratio', 'Count'])
    for index, row in df.iterrows():
        df_f = df.loc[(df['DRUG'] == row['DRUG']) & (df['AE'] == row['AE']) & (df['Sex'] == 'F')]
        df_m = df.loc[(df['DRUG'] == row['DRUG']) & (df['AE'] == row['AE']) & (df['Sex'] == 'M')]
        if df_f.empty:
            # continue
            ratio = 1 / df_m['IC025'].values[0]
            count = df_m['IC025'].values[0]
            df_new = pd.DataFrame([{'DRUG': row['DRUG'], 'AE': row['AE'], 'Ratio': float(ratio), 'Count': float(count),
                                    'IC025_m': float(df_m['IC025'].values[0]),
                                    'IC025_f': 0}])
        elif df_m.empty:
            # continue
            ratio = df_f['IC025'].values[0] / 1
            count = df_f['IC025'].values[0]
            df_new = pd.DataFrame([{'DRUG': row['DRUG'], 'AE': row['AE'], 'Ratio': float(ratio), 'Count': float(count),
                                    'IC025_m': 0,
                                    'IC025_f': float(df_f['IC025'].values[0])}])
        else:
            ratio = df_f['IC025'].values[0] / df_m['IC025'].values[0]
            count = df_f['IC025'].values[0] + df_m['IC025'].values[0]
            df_new = pd.DataFrame([{'DRUG': row['DRUG'], 'AE': row['AE'], 'Ratio': float(ratio), 'Count': float(count),
                                    'IC025_m': float(df_m['IC025'].values[0]),
                                    'IC025_f': float(df_f['IC025'].values[0])}])
        total_df = pd.concat([total_df, df_new], axis=0, ignore_index=True)
    total_df = total_df.drop_duplicates(subset=['DRUG', 'AE', 'IC025_m', 'IC025_f'], keep='first', ignore_index=True)
    male_part = total_df.loc[total_df['Ratio'] < 0.5]
    #male_part = total_df[(total_df['Ratio'] < 0.5) | (total_df['IC025_m'] == 0)]
    #male_part = male_part.drop(male_part[male_part.IC025_m == 0].index)
    df_axis1 = total_df.loc[total_df['IC025_f'] == 0]
    print(total_df[total_df['DRUG'] == "diazepam"])
    male_part = pd.concat([df_axis1, male_part], axis=0)
    male_part = male_part.drop_duplicates(subset=['DRUG', 'AE', 'IC025_m', 'IC025_f'], keep='first',
                                          ignore_index=True)
    df_big = male_part.groupby(['DRUG'], as_index=False).sum()
    df_big = df_big.sort_values(['IC025_m'], ascending=False)
    df_big = df_big.head(10)
    fig4 = px.bar(df_big, x="DRUG", y="IC025_m", title="Top 10 male DRUGS", color="DRUG",
                  color_discrete_map=colors_d)  # width=2100, height=700
    fig4.update_xaxes(categoryorder='max descending')
    fig4.show()


if __name__ == '__main__':
    main()
