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
            'cinolazepam': '#C5A9A3', 'oxazolam': '#5FB815', 'lormetazepam': '#66953E', 'prazepam': '#FF0087',
            'flunitrazepam': '#FB11FF', 'nitrazepam': '#E49C20', 'estazolam': '#8E3564', 'ethyl loflazepate': '#FBB4FC',
            'etizolam': '#0CC492', 'brotizolam': '#B498FF', 'clorazepate': '#0CC44C', 'triazolam': '#1349C4',
            'chlordiazepoxide': '#4a8c12', 'flurazepam': '#75AB9C', 'zaleplon': '#18E4F5', 'eszopiclone': '#00B9FF',
            'temazepam': '#82F721', 'zopiclone': '#458AA4', 'bromazepam': '#4562A4', 'oxazepam': '#A585C4',
            'clobazam': '#2C6CFF', 'midazolam': '#98B7FF', 'remimazolam': '#8000FF'}
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
           'prazepam': 'circle-open',
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
    # path = 'C:\\Users\\TARIQOPLATA\PycharmProjects\\FAERS_final\\data\\data\\Old_gold\\'
    path = '/Users/ftk/Documents/Work/FAERS_final/data/Old_gold/'
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


def main_v1():
    # path = 'C:\\Users\\TARIQOPLATA\PycharmProjects\\FAERS_final\\data\\data\\Old_gold\\'
    path = '/Users/ftk/Documents/Work/FAERS_final/data/Old_gold/'
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

    fig = px.scatter(total_df, x="IC025_f", y="IC025_m", color="DRUG", hover_data=['AE'], symbol_map=symbols,
                     symbol="DRUG", trendline="ols", trendline_scope="overall", trendline_color_override="black")
    fig.show()

    df_m2 = total_df.groupby(['AE', 'DRUG'], as_index=False).sum()

    df_fx = df_m2[df_m2['IC025_f'] == 0.0]
    df_fx = df_fx.sort_values('IC025_m', ascending=False)
    df_fx = df_fx.drop_duplicates(subset=['DRUG', 'AE', 'IC025_m'], keep='first', ignore_index=True)
    df_fx = df_fx.head(20)
    df_f_aes = df_fx['AE'].tolist()
    df_f_drug = df_fx['DRUG'].tolist()
    df_fx = total_df.loc[total_df['AE'].isin(df_f_aes) & total_df['DRUG'].isin(df_f_drug)]
    df_fx = df_fx.drop_duplicates(subset=['DRUG', 'AE', 'IC025_m'], keep='first', ignore_index=True)
    df_fx = df_fx.sort_values('IC025_m', ascending=False)
    print(df_fx)

    df_mx = df_m2[df_m2['IC025_m'] == 0.0]
    df_mx = df_mx.sort_values('IC025_f', ascending=False)
    df_mx = df_mx.drop_duplicates(subset=['DRUG', 'AE', 'IC025_f'], keep='first', ignore_index=True)
    df_mx = df_mx.head(20)
    df_m_aes = df_mx['AE'].tolist()
    df_m_drug = df_mx['DRUG'].tolist()
    df_mx = total_df.loc[total_df['AE'].isin(df_m_aes) & total_df['DRUG'].isin(df_m_drug)]
    df_mx = df_mx.drop_duplicates(subset=['DRUG', 'AE', 'IC025_f'], keep='first', ignore_index=True)
    df_mx = df_mx.sort_values('IC025_f', ascending=False)
    print(df_mx)

    fig2 = px.bar(df_fx, x="IC025_m", y="AE", title="Top 10 male AEs", color="DRUG", color_discrete_map=colors_d,
                  orientation='h')
    fig.update_xaxes(tickangle=90)
    fig2.show()

    fig3 = px.bar(df_mx, x="AE", y="IC025_f", title="Top 10 female AEs", color="DRUG", color_discrete_map=colors_d)
    fig.update_xaxes(tickangle=90)
    fig3.show()

    # df_m1 = total_df[total_df['IC025_f'] != '0.0']
    # df_f1 = total_df[total_df['IC025_m'] != '0.0']
    # print(df_m1)
    # fig = px.pie(df_m1, values='IC025_m', names="DRUG", title="Percentage of drugs having only male AEs MALE")
    # fig.show()
    # fig = px.pie(df_f1, values='IC025_f', names="DRUG", title="Percentage of drugs having only male AEs FEMALE")
    # fig.show()

    """
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
    # path = 'C:\\Users\\TARIQOPLATA\PycharmProjects\\FAERS_final\\data\\data\\Old_gold\\'
    path = '/Users/ftk/Documents/Work/FAERS_final/data/Old_gold/'
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
