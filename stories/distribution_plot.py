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

"""
    ZEIGE MIR IN EINEM PLOT WELCHE DRUGS ODER AES EINE TENDENZ NUR FÜR FRAUEN ODER MÄNNER HABEN
    
"""


def main_copy():
    path = 'C:\\Users\\TARIQOPLATA\PycharmProjects\\FAERS_final\\data\\data\\Old_gold\\'
    #path = '/Users/ftk/Documents/Work/FAERS_final/data/Old_gold/'
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
        df_f = df.loc[(df['DRUG'] == row['DRUG']) & (df['AE'] == row['AE']) &
                      (df['Sex'] == 'F')]
        df_m = df.loc[(df['DRUG'] == row['DRUG']) & (df['AE'] == row['AE']) &
                      (df['Sex'] == 'M')]
        if df_f.empty:
            continue
            # ratio = 1 / df_m['IC025'].values[0]
            # count = df_m['IC025'].values[0]
        elif df_m.empty:
            continue
            # ratio = df_f['IC025'].values[0] / 1
            # count = df_f['IC025'].values[0]
        else:
            ratio = df_f['IC025'].values[0] / df_m['IC025'].values[0]
            count = df_f['IC025'].values[0] + df_m['IC025'].values[0]
        total_df = total_df.append({'DRUG': row['DRUG'], 'AE': row['AE'], 'Ratio': ratio, 'Count': count},
                                   ignore_index=True)
    total_df = total_df.sort_values('Ratio', ascending=True)
    print(total_df)
    fre = total_df.assign(
        bins=pd.cut(total_df["Ratio"], [0.000, 0.167, 0.200, 0.250, 0.333, 0.500, 0.800, 1.250, 2.000, 3.000,
                                        4.000, 5.000, 6.000, 500.000], labels=['0 to 0.167', '0.167 to 0.2',
                                                                               '0.2 to 0.25', '0.25 to 0.33',
                                                                               '0.33 to 0.5', '0.5 to 0.8',
                                                                               '0.8 to 1.25', '1.25 to 2',
                                                                               '2 to 3', '3 to 4', '4 to 5',
                                                                               '5 to 6', '6 to 500']))
    print(fre)
    fre_AE_counts = fre.groupby(["bins", "AE"], as_index=False)["Count"].count()
    fre_AE_sum = fre.groupby(["bins", "AE"], as_index=False)["Ratio"].sum()
    fre_count_counts = fre.groupby(["bins", "DRUG"], as_index=False)["Count"].count()
    fre_count_sum = fre.groupby(["bins", "DRUG"], as_index=False)["Ratio"].sum()
    fig = px.bar(fre_count_sum, x='bins', y='Ratio', color='DRUG', title="Sum of drug reports in bin",
                 color_discrete_map=colors_d, pattern_shape="DRUG", pattern_shape_map=symbols_d)
    fig.update_layout(
        xaxis_title="Ratios",
        yaxis_title="Sum of IC025 per drug in ratio range",
        title="Neurpsychiatric disorders"
    )
    fig.show()

    total_df = pd.DataFrame(columns=['DRUG', 'AE', 'Ratio', 'Count'])
    for index, row in df.iterrows():
        df_f = df.loc[(df['AE'] == row['AE']) &
                      (df['Sex'] == 'F')]
        df_m = df.loc[(df['AE'] == row['AE']) &
                      (df['Sex'] == 'M')]
        if df_f.empty:
            continue
            # ratio = 1 / df_m['IC025'].values[0]
            # count = df_m['IC025'].values[0]
        elif df_m.empty:
            continue
            # ratio = df_f['IC025'].values[0] / 1
            # count = df_f['IC025'].values[0]
        else:
            ratio = df_f['IC025'].sum() / df_m['IC025'].sum()
            count = df_f['IC025'].sum() + df_m['IC025'].sum()
        total_df = total_df.append({'DRUG': row['DRUG'], 'AE': row['AE'], 'Ratio': ratio, 'Count': count},
                                   ignore_index=True)
    total_df = total_df.sort_values('Ratio', ascending=True)
    print(total_df)
    fre = total_df.assign(
        bins=pd.cut(total_df["Ratio"], [0.000, 0.167, 0.200, 0.250, 0.333, 0.500, 0.800, 1.250, 2.000, 3.000,
                                        4.000, 5.000, 6.000, 500.000], labels=['0 to 0.167', '0.167 to 0.2',
                                                                               '0.2 to 0.25', '0.25 to 0.33',
                                                                               '0.33 to 0.5', '0.5 to 0.8',
                                                                               '0.8 to 1.25', '1.25 to 2',
                                                                               '2 to 3', '3 to 4', '4 to 5',
                                                                               '5 to 6', '6 to 500']))
    print(fre)
    fig = px.bar(fre_AE_sum, x='bins', y='Ratio', color='AE', title="Counts of AE in bin")
    fig.update_layout(
        xaxis_title="Ratios",
        yaxis_title="Sum of IC025 per AE in ratio range"
    )
    fig.show()
    """
    #fig.write_html('Sumofdrugreportsinbin_' + ht + '.html')
    fig = px.bar(fre_count_counts, x='bins', y='Count', color='DRUG', title="Counts of drug reports in bin")
    fig.update_layout(
        xaxis_title="Ratios",
        yaxis_title="Sum of reports per drug in ratio range"
    )
    fig.show()
    #fig.write_html('Countsofdrugreportsinbin_' + ht + '.html')
    fig = px.bar(fre_AE_counts, x='bins', y='Count', color='AE', title="Counts of AE in bin")
    fig.update_layout(
        xaxis_title="Ratios",
        yaxis_title="Sum of reports per drug in ratio range"
    )
    fig.show()
    #fig.write_html('CountspfAEsinbin_' + ht + '.html')
    fig = px.bar(fre_AE_sum, x='bins', y='Count', color='AE', title="Sum of AE reports in bin")
    fig.update_layout(
        xaxis_title="Ratios",
        yaxis_title="Sum of reports per drug in ratio range"
    )
    fig.show()
    #fig.write_html('Sum_of_AE_reports_in_bin_' + ht + '.html')"""


def Setcolor_opa(x):
    return colors_d_opa.get(x)


def Setcolor_full(x):
    return colors_d_full.get(x)


def Setshape(x):
    print([x, symbols.get(x)])
    return symbols.get(x)


def fin_scatter(df_part, df_part2):
    fig = go.Figure()
    drugs = df_part["DRUG"].tolist() + df_part2["DRUG"].tolist()
    drugs = list(dict.fromkeys(drugs))

    for item in drugs:
        df_part_d = df_part[df_part["DRUG"] == item]
        df_part2_d = df_part2[df_part2["DRUG"] == item]

        fig.add_trace(go.Scatter(x=df_part_d['IC025_f'], y=df_part_d['IC025_m'], showlegend=True, mode='markers',
                                 name=item,
                                 hovertemplate=df_part_d["AE"],
                                 #hoverinfo="text",
                                 marker=dict(color=list(map(Setcolor_full, df_part_d['DRUG'])),
                                             symbol=list(map(Setshape, df_part_d['DRUG'])))))
        fig.add_trace(go.Scatter(x=df_part2_d['IC025_f'], y=df_part2_d['IC025_m'], showlegend=True, mode='markers',
                                 name=item,
                                 hovertemplate=df_part2_d["AE"],
                                 #hoverinfo="text",
                                 marker=dict(color=list(map(Setcolor_opa, df_part2_d['DRUG'])),
                                             symbol=list(map(Setshape, df_part2_d['DRUG'])))))

    fig.update_layout(showlegend=True)
    fig.update_yaxes(range=[-0.1, 7])
    fig.update_xaxes(range=[-0.1, 7])
    fig.update_traces(marker={'size': 8})
    fig.update_layout(font=dict(size=18), height=1200, width=1200)
    fig.show()
    #fig.write_html("Figure_8A_v2.html")


def main_v1():
    path = 'C:\\Users\\TARIQOPLATA\PycharmProjects\\FAERS_final\\data\\data\\Old_gold\\'
    #path = '/Users/ftk/Documents/Work/FAERS_final/data/Old_gold/'
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
        elif df_m.empty:
            # continue
            ratio = df_f['IC025'].values[0] / 1
            count = df_f['IC025'].values[0]
        else:
            ratio = df_f['IC025'].sum() / df_m['IC025'].sum()
            count = df_f['IC025'].sum() + df_m['IC025'].sum()
        total_df = total_df.append({'DRUG': row['DRUG'], 'AE': row['AE'], 'Ratio': ratio, 'Count': count,
                                    'IC025_m': df_m['IC025'].sum(), 'IC025_f': df_f['IC025'].sum()},
                                   ignore_index=True)
    total_df = total_df.sort_values('DRUG', ascending=True)
    # total_df.to_csv('Distributions.csv')
    df_part = total_df[(total_df['Ratio'] < 0.5) | (total_df['Ratio'] > 2)]
    df_axis1 = total_df[total_df['IC025_m'] == 0.0]
    df_axis2 = total_df[total_df['IC025_f'] == 0.0]
    df_part = pd.concat([df_axis1, df_axis2, df_part], axis=0)
    df_part = df_part.drop_duplicates(subset=['DRUG', 'AE', 'Ratio', 'IC025_m', 'IC025_f'], keep='first',
                                      ignore_index=True)
    print(df_part)
    df_part2 = total_df[(total_df['Ratio'] >= 0.5) | (total_df['Ratio'] <= 2)]
    # df_g = df_g.drop(df_g[df_g.DRUG == item].index)
    df_part2 = df_part2.drop(df_part2[df_part2.IC025_f == 0.00].index)
    df_part2 = df_part2.drop(df_part2[df_part2.IC025_m == 0.00].index)
    df_part2 = df_part2.drop_duplicates(subset=['DRUG', 'AE', 'Ratio', 'IC025_m', 'IC025_f'], keep='first',
                                        ignore_index=True)
    #fin_scatter(df_part, df_part2)

    # SHOW THE TOP 20 AEs for each sex only axis == 0
    # MALE
    df_axis1 = total_df[total_df['IC025_f'] == 0.0]
    male_part = df_axis1.drop_duplicates(subset=['DRUG', 'AE', 'Ratio', 'IC025_m', 'IC025_f'], keep='first',
                                          ignore_index=True)
    male_part2 = male_part.groupby(['AE'], as_index=False).sum()
    male_part2 = male_part2.sort_values(['IC025_m'], ascending=False)
    male_part2 = male_part2.head(20)
    males_aes = male_part2['AE'].tolist()
    male_part3 = male_part[male_part['AE'].isin(males_aes)]
    fig5 = px.bar(male_part3, x="AE", y="IC025_m", title="Top 10 male AEs", color="DRUG",
                  color_discrete_map=colors_d)
    fig5.update_layout(barmode='stack', xaxis={'categoryorder': 'total descending'},
                       yaxis={'categoryorder': 'total descending'})
    fig5.show()

    # FEMALE
    df_axis1 = total_df[total_df['IC025_m'] == 0.0]
    male_part = df_axis1.drop_duplicates(subset=['DRUG', 'AE', 'Ratio', 'IC025_m', 'IC025_f'], keep='first',
                                          ignore_index=True)
    male_part2 = male_part.groupby(['AE'], as_index=False).sum()
    male_part2 = male_part2.sort_values(['IC025_f'], ascending=False)
    male_part2 = male_part2.head(20)
    males_aes = male_part2['AE'].tolist()
    male_part3 = male_part[male_part['AE'].isin(males_aes)]
    fig5 = px.bar(male_part3, x="AE", y="IC025_f", title="Top 10 female AEs", color="DRUG",
                  color_discrete_map=colors_d)
    fig5.update_layout(barmode='stack', xaxis={'categoryorder': 'total descending'},
                       yaxis={'categoryorder': 'total descending'})
    fig5.show()


    male_part = total_df[(total_df['Ratio'] < 0.5) | (total_df['IC025_m'] == 0.0)]
    male_part = male_part.drop(male_part[male_part.IC025_m == 0.00].index)
    df_axis1 = total_df[total_df['IC025_f'] == 0.0]
    male_part = pd.concat([df_axis1, male_part], axis=0)
    male_part = male_part.drop_duplicates(subset=['DRUG', 'AE', 'Ratio', 'IC025_m', 'IC025_f'], keep='first',
                                          ignore_index=True)
    male_part2 = male_part.groupby(['AE'], as_index=False).sum()
    male_part2 = male_part2.sort_values(['IC025_m'], ascending=False)
    male_part2 = male_part2.head(20)
    males_aes = male_part2['AE'].tolist()
    male_part3 = male_part[male_part['AE'].isin(males_aes)]
    print(male_part2)
    fig5 = px.bar(male_part3, x="AE", y="IC025_m", title="Top 10 male AEs", color="DRUG",
                  color_discrete_map=colors_d)
    fig5.update_layout(barmode='stack', xaxis={'categoryorder': 'total descending'},
                       yaxis={'categoryorder': 'total descending'})
    #fig5.update_xaxes(tickangle=90)
    #fig5.show()

    female_part = total_df[(total_df['Ratio'] > 2) | (total_df['IC025_f'] == 0.0)]
    female_part = female_part.drop(female_part[female_part.IC025_f == 0.00].index)
    df_axis1 = total_df[total_df['IC025_m'] == 0.0]
    female_part = pd.concat([df_axis1, female_part], axis=0)
    female_part = female_part.drop_duplicates(subset=['DRUG', 'AE', 'Ratio', 'IC025_m', 'IC025_f'], keep='first',
                                              ignore_index=True)
    female_part2 = female_part.groupby(['AE'], as_index=False).sum()
    female_part2 = female_part2.sort_values(['IC025_m'], ascending=False)
    female_part2 = female_part2.head(20)
    females_aes = female_part2['AE'].tolist()
    female_part3 = female_part[female_part['AE'].isin(females_aes)]
    print(female_part2)
    fig6 = px.bar(female_part3, x="AE", y="IC025_f", title="Top 10 female AEs", color="DRUG",
                  color_discrete_map=colors_d)
    fig6.update_layout(barmode='stack', xaxis={'categoryorder': 'total descending'},
                       yaxis={'categoryorder': 'total descending'})
    #fig6.show()

    aes = ['restlessness', 'mania', 'hypomania', 'logorrhoea', 'psychotic behaviour']
    male_part3 = male_part3[male_part3['AE'].isin(aes)]
    figX = px.pie(male_part3, values="IC025_m", names='DRUG', title="MALES", color_discrete_map=colors_d_full,
                  color="DRUG")
    figX.update_traces(textposition='inside', textinfo='percent+label', textfont_size=20, hole=.3,
                       title='MALE')
    #figX.show()

    aes = ['psychomotor hyperactivity', 'impulsive behaviour']
    female_part3 = female_part3[female_part3['AE'].isin(aes)]
    figX = px.pie(female_part3, values="IC025_f", names='DRUG', title="FEMALES", color_discrete_map=colors_d_full,
                  color="DRUG")
    figX.update_traces(textposition='inside', textinfo='percent+label', textfont_size=20, hole=.3,
                       title='FEMALE')
    #figX.show()



    #fig = px.scatter(male_part, x="IC025_f", y="IC025_m", color="DRUG", hover_data=['AE', 'Ratio', 'Count'],
    #                 symbol_map=symbols, symbol="DRUG", opacity=1.0, height=1200, width=1200, title='Male')
    #fig.show()
    # fig = px.scatter(df_part, x="IC025_f", y="IC025_m", color="DRUG", hover_data=['AE', 'Ratio', 'Count'],
    #                 symbol_map=symbols, symbol="DRUG", opacity=1.0, height=1200, width=1200)
    # fig.update_layout(showlegend=False)
    # fig.update_yaxes(range=[-0.1, 7])
    # fig.update_xaxes(range=[-0.1, 7])
    # fig.update_traces(marker={'size': 8})
    # fig.update_layout(font=dict(size=18))
    # fig.show()
    """
        df_m2 = total_df.groupby(['AE', 'DRUG'], as_index=False).sum()
        df_fx = df_m2[df_m2['IC025_f'] == 0.0]
        df_fx = df_fx.sort_values('IC025_m', ascending=False)
        df_fx = df_fx.drop_duplicates(subset=['DRUG', 'AE', 'IC025_m'], keep='first', ignore_index=True)
        df_fx = df_fx.head(40)
        print("PART 1")
        print(df_fx)
        df_f_aes = df_fx['AE'].tolist()
        df_f_drug = df_fx['DRUG'].tolist()
        df_fx = total_df.loc[total_df['AE'].isin(df_f_aes) & total_df['DRUG'].isin(df_f_drug)]
        df_fx = df_fx.drop_duplicates(subset=['DRUG', 'AE', 'IC025_m'], keep='first', ignore_index=True)
        df_fx = df_fx.sort_values('IC025_m', ascending=False)
        df_fx = df_fx.head(25)
        print("PART 2")
        print(df_fx)
        fig2 = px.bar(df_fx, x="IC025_m", y="AE", title="Top 10 male AEs", color="DRUG", color_discrete_map=colors_d,
                      orientation='h')
        fig2.update_layout(barmode='stack', xaxis={'categoryorder': 'total ascending'},
                           yaxis={'categoryorder': 'total ascending'})
        fig2.show()

        df_mx = df_m2[df_m2['IC025_m'] == 0.0]
        df_mx = df_mx.sort_values('IC025_f', ascending=False)
        df_mx = df_mx.drop_duplicates(subset=['DRUG', 'AE', 'IC025_f'], keep='first', ignore_index=True)
        df_mx = df_mx.head(40)
        df_m_aes = df_mx['AE'].tolist()
        df_m_drug = df_mx['DRUG'].tolist()
        df_mx = total_df.loc[total_df['AE'].isin(df_m_aes) & total_df['DRUG'].isin(df_m_drug)]
        df_mx = df_mx.drop_duplicates(subset=['DRUG', 'AE', 'IC025_f'], keep='first', ignore_index=True)
        df_mx = df_mx.sort_values('IC025_f', ascending=False)
        df_mx = df_mx.head(23)
        fig3 = px.bar(df_mx, x="AE", y="IC025_f", title="Top 10 female AEs", color="DRUG", color_discrete_map=colors_d)
        fig3.update_layout(barmode='stack', xaxis={'categoryorder': 'total descending'},
                           yaxis={'categoryorder': 'total descending'})
        fig3.show()

        df_big = total_df[total_df['Ratio'] < 0.5]
        df_small = total_df[total_df['Ratio'] > 2]

        df_big = df_big.groupby(['AE'], as_index=False).sum()
        df_big = df_big.sort_values(['IC025_m'], ascending=False)
        # print(df_big)
        df_big = df_big.head(20)
        fig4 = px.bar(df_big, x="AE", y="IC025_m", title="Top 10 male DRUGS from < 0.5", color="AE",
                      color_discrete_map=colors_d, width=2100, height=700)
        fig4.update_xaxes(categoryorder='max descending')
        fig4.update_xaxes(tickangle=90)
        fig4.show()

        df_small = df_small.groupby(['AE'], as_index=False).sum()
        df_small = df_small.sort_values(['IC025_f'], ascending=False)
        df_small = df_small.head(20)
        print(df_small)
        fig5 = px.bar(df_small, x="AE", y="IC025_f", title="Top 10 female DRUGS", color="AE",
                      color_discrete_map=colors_d, width=2100, height=700)
        fig5.update_xaxes(categoryorder='max descending')
        fig5.update_xaxes(tickangle=90)
        fig5.show()
        # df_m1 = total_df[total_df['IC025_f'] != '0.0']
        # df_f1 = total_df[total_df['IC025_m'] != '0.0']
        # print(df_m1)
        # fig = px.pie(df_m1, values='IC025_m', names="DRUG", title="Percentage of drugs having only male AEs MALE")
        # fig.show()
        # fig = px.pie(df_f1, values='IC025_f', names="DRUG", title="Percentage of drugs having only male AEs FEMALE")
        # fig.show()
        fre = total_df.assign(
            bins=pd.cut(total_df["Ratio"], [0.000, 0.167, 0.200, 0.250, 0.333, 0.500, 0.800, 1.250, 2.000, 3.000,
                                            4.000, 5.000, 6.000, 500.000], labels=['0 to 0.167', '0.167 to 0.2',
                                                                                   '0.2 to 0.25', '0.25 to 0.33',
                                                                                   '0.33 to 0.5', '0.5 to 0.8',
                                                                                   '0.8 to 1.25', '1.25 to 2',
                                                                                   '2 to 3', '3 to 4', '4 to 5',
                                                                                   '5 to 6', '6 to 500']))
        print(fre)
        # fre_count_sum = fre.groupby(["bins", "DRUG"], as_index=False)["Ratio"].sum()
        fre_count_sum = fre.groupby(["bins", "DRUG"], as_index=False).sum()
        fig = px.bar(fre_count_sum, x='bins', y='Ratio', color='DRUG', title="Sum of drug reports in bin",
                     color_discrete_map=colors_d, pattern_shape="DRUG", pattern_shape_map=symbols_d)
        fig.update_layout(
            xaxis_title="Ratios",
            yaxis_title="Sum of IC025 per drug in ratio range",
            title="Neurpsychiatric disorders"
        )
        fig.show()

        fre_AE_sum = fre.groupby(["bins", "AE"], as_index=False).sum()
        fig = px.bar(fre_AE_sum, x='bins', y='Ratio', color='AE', title="Counts of AE in bin")
        fig.update_layout(
            xaxis_title="Ratios",
            yaxis_title="Sum of IC025 per AE in ratio range"
        )
        fig.show()

        fre_AE_sum = fre.groupby(["bins", "AE", "DRUG"], as_index=False).sum()
        fig = px.bar(fre_AE_sum, x='bins', y='Ratio', color='DRUG', title="Counts of AE in bin")
        fig.update_layout(
            xaxis_title="Ratios",
            yaxis_title="Sum of IC025 per DRUG, AE in ratio range"
        )
        fig.show()"""
    """
        #fig.write_html('Sumofdrugreportsinbin_' + ht + '.html')
        fig = px.bar(fre_count_counts, x='bins', y='Count', color='DRUG', title="Counts of drug reports in bin")
        fig.update_layout(
            xaxis_title="Ratios",
            yaxis_title="Sum of reports per drug in ratio range"
        )
        fig.show()
        #fig.write_html('Countsofdrugreportsinbin_' + ht + '.html')
        fig = px.bar(fre_AE_counts, x='bins', y='Count', color='AE', title="Counts of AE in bin")
        fig.update_layout(
            xaxis_title="Ratios",
            yaxis_title="Sum of reports per drug in ratio range"
        )
        fig.show()
        #fig.write_html('CountspfAEsinbin_' + ht + '.html')
        fig = px.bar(fre_AE_sum, x='bins', y='Count', color='AE', title="Sum of AE reports in bin")
        fig.update_layout(
            xaxis_title="Ratios",
            yaxis_title="Sum of reports per drug in ratio range"
        )
        fig.show()
        #fig.write_html('Sum_of_AE_reports_in_bin_' + ht + '.html')"""


def main():
    path = 'C:\\Users\\TARIQOPLATA\PycharmProjects\\FAERS_final\\data\\data\\Old_gold\\'
    # path = '/Users/ftk/Documents/Work/FAERS_final/data/Old_gold/'
    df_f = pd.read_csv(path + 'Disprop_analysis_female_with_HTs.csv')
    df_m = pd.read_csv(path + 'Disprop_analysis_male_with_HTs.csv')
    hts = ['nervous system disorders', 'psychiatric disorders']
    df_f = df_f[df_f['HT'].isin(hts)]
    df_m = df_m[df_m['HT'].isin(hts)]
    df_f['Sex'] = 'F'
    df_m['Sex'] = 'M'
    frames = [df_f, df_m]
    df = pd.concat(frames)
    fre = df.assign(
        bins=pd.cut(df["IC025"], [0.000, 0.167, 0.200, 0.250, 0.333, 0.500, 0.800, 1.250, 2.000, 3.000,
                                  4.000, 5.000, 6.000, 500.000], labels=['0 to 0.167', '0.167 to 0.2',
                                                                         '0.2 to 0.25', '0.25 to 0.33',
                                                                         '0.33 to 0.5', '0.5 to 0.8',
                                                                         '0.8 to 1.25', '1.25 to 2',
                                                                         '2 to 3', '3 to 4', '4 to 5',
                                                                         '5 to 6', '6 to 500']))
    fre = fre.groupby(["bins", "DRUG"], as_index=False).sum()
    # fig = px.violin(df, y="IC025", color="Sex", violinmode='overlay')
    fig = px.histogram(df_m, x="IC025", color="Sex")
    fig.update_layout(barmode='overlay')
    fig.show()


if __name__ == '__main__':
    main_v1()
