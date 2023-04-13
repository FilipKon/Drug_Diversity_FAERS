import pandas as pd
import plotly.express as px
import warnings
import numpy as np
import math
import plotly.graph_objs as go
from plotly.subplots import make_subplots
warnings.filterwarnings("ignore")
pd.set_option('display.max_columns', 1000)  # or None
pd.set_option('display.max_rows', 1000)  # or None
pd.set_option('display.max_colwidth', 100)  # or None

drugs_alpha = {'alprazolam': 962, 'bromazepam': 963, 'brotizolam': 964, 'chlordiazepoxide': 965, 'cinolazepam': 966,
               'clobazam': 967, 'clonazepam': 968, 'clorazepate': 969, 'clotiazepam': 970, 'cloxazolam': 971,
               'diazepam': 972, 'estazolam': 973, 'eszopiclone': 974, 'ethyl loflazepate': 975, 'etizolam': 976,
               'flumazenil': 977, 'flunitrazepam': 978, 'flurazepam': 979, 'ketazolam': 980, 'lorazepam': 981,
               'lormetazepam': 982, 'medazepam': 983, 'mexazolam': 984, 'midazolam': 985, 'nimetazepam': 986,
               'nitrazepam': 987,
               'nordazepam': 988, 'oxazepam': 989, 'oxazolam': 990, 'prazepam': 991, 'quazepam': 992, 'temazepam': 993,
               'tetrazepam': 994, 'tofisopam': 995, 'triazolam': 996, 'triazulenone': 997, 'zaleplon': 998,
               'zolpidem': 999, 'zopiclone': 1000}

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

colors_g = {'F': '#e5a2bd', 'M': '#9aceeb'}

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

symbols_d = {'nervous system neoplasms benign': "/", 'adjustment disorders (incl subtypes)': ".", 'demyelinating disorders': "x",
             'headaches': "-",
            'nervous system neoplasms malignant and unspecified nec': "/", 'central nervous system infections and inflammations': "+",
             'neurological disorders of the eye': ".",
            'spinal cord and nerve root disorders': "/", 'triazulenone': "x", 'quazepam': "-", 'nordazepam': "|",
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

path = 'C:\\Users\\TARIQOPLATA\\PycharmProjects\\FAERS_final\\'
#path = '/Users/ftk/Documents/Work/FAERS_final/'

drug_1 = 'zopiclone'
drug_2 = 'eszopiclone'
drug1 = 'zopiclone'
drug2 = 'eszopiclone'

def bar_chart(df):
    # df = df[df['Sex'] == 'M']
    fig = px.bar(df, x="AE", y="IC025", color='Sex', barmode='group', height=400, pattern_shape="DRUG",
                 color_discrete_map=colors_g, pattern_shape_map={'zolpidem': '+', 'clotiazepam': '-'})
    # ["+", "-"]
    fig.update_layout(
        font=dict(
            size=18,
        )
    )
    fig.show()


def pie_chart(df, sex, drug):
    df = df[df['DRUG'] == drug]
    df = df.sort_values(by=['IC025'], ascending=False)
    df = df.head(20)
    print(df)
    tit = drug + ' ' + sex
    fig = px.pie(df, values='IC025', names='AE', title=tit)
    fig.update_traces(textposition='inside', textinfo='percent+label', textfont_size=24)
    fig.show()


def scatter(df, drug1, drug2):
    fig_fin = make_subplots(rows=1, cols=2, subplot_titles=(drug1, drug2))
    #BROTIZOLAM, ETIZOLAM
    df = df.drop_duplicates(subset=['DRUG', 'AE', 'IC025', 'Reports', 'Sex'])
    df = df.drop('IDX', axis=1)
    df = df.drop('HT_level2', axis=1)
    df = df.drop('HT', axis=1)
    #df = df.drop('HT_level3', axis=1)
    df = df.drop('IC', axis=1)
    df = df.drop('ROR', axis=1)
    df_e = df[df['DRUG'] == drug1]
    df_e = df_e.drop_duplicates(subset=['DRUG', 'AE'])
    df_e = df_e.sort_values(by=['IC025'], ascending=False)
    df_e = df_e.head(10)
    aes_1 = df_e['AE'].tolist()
    df_1 = df[df['AE'].isin(aes_1)]
    print(df_e)

    fig = px.scatter(df_1, y="IC025", x="AE", color="Sex", symbol="DRUG", color_discrete_map=colors_g,
                     title=drug1)

    fig.update_traces(marker_size=15)
    fig.update_layout(yaxis_range=[0, 6])
    fig.update_xaxes(categoryorder='total descending')
    #fig.show()

    df_z = df[df['DRUG'] == drug2]
    df_z = df_z.drop_duplicates(subset=['DRUG', 'AE'])
    df_z = df_z.sort_values(by=['IC025'], ascending=False)
    df_z = df_z.head(10)
    aes_1 = df_z['AE'].tolist()
    df_2 = df[df['AE'].isin(aes_1)]
    print(df_z)

    fig2 = px.scatter(df_1, y="IC025", x="AE", color="Sex", symbol="DRUG", color_discrete_map=colors_g,
                      title=drug2)
    fig2.update_traces(marker_size=15)
    fig2.update_layout(yaxis_range=[0, 6])
    fig2.update_xaxes(categoryorder='total descending')
    #fig2.show()

    # Data component
    #data = [fig, fig2]
    #fig_fin = go.Figure(data=data, layout=layout)

    fig_fin.add_trace(
        go.Scatter(
            y=df_1["IC025"],
            x=df_1["AE"],
            mode='markers',
            name=drug1,
            showlegend=True,
            marker=dict(color=list(map(Setcolor, df_1["Sex"])), symbol=list(map(Setshape, df_1["DRUG"])), size=15),
        ), row=1, col=1
        )
    fig_fin.update_layout(showlegend=True)
    fig_fin.update_xaxes(categoryorder='max descending', row=1, col=1)
    fig_fin.add_trace(
        go.Scatter(
            y=df_2["IC025"],
            x=df_2["AE"],
            mode='markers',
            name=drug2,
            showlegend=True,
            marker=dict(color=list(map(Setcolor, df_2["Sex"])), symbol=list(map(Setshape, df_2["DRUG"])), size=15),
            ), row=1, col=2
        )
    fig_fin.update_xaxes(categoryorder='max descending',  row=1, col=2)
    fig_fin.update_yaxes(range=[-6, 6], row=1, col=2)
    fig_fin.update_yaxes(range=[-6, 6], row=1, col=1, title_text="IC025")
    fig_fin.update_xaxes(title_text="Adverse Events", row=1, col=1)
    fig_fin.update_xaxes(title_text="Adverse Events", row=1, col=2)
    fig.update_layout(title_text="Customizing Subplot Axes", height=700)
    #fig_fin.update_layout(
   #     autosize=False,
     #   width=4100,
     #   height=1000)
    fig_fin.show()
    # df2 = df.groupby(by=['AE'], as_index=False).sum()
    # df2 = df2.sort_values(by=['IC025'], ascending=False)
    # df2 = df2.head(20)
    # aes = df2['AE'].tolist()
    """
    aes = df_e['AE'].tolist() + df_z['AE'].tolist()
    df = df[df['AE'].isin(aes)]
    fig = px.scatter(df, y="IC025", x="AE", color="Sex", symbol="DRUG", color_discrete_map=colors_g)
    fig.update_traces(marker_size=15)
    fig.update_xaxes(categoryorder='max descending')
    # fig.update_layout(scattermode="group")
    fig.show()"""


def Setshape(x):
    if x == drug1:
        return "diamond"
    elif x == drug2:
        return "circle"
    return "arrow"


def Setcolor(x):
    if x == "F":
        return '#e5a2bd'
    elif x == "M":
        return '#9aceeb'


def create_scatter(drug1, drug2):
    path2 = 'data\\data\\Old_gold\\'
    #path2 = 'data/Old_gold/'
    df_f = pd.read_csv(path + path2 + 'Disprop_analysis_female_with_HTs.csv')
    df_m = pd.read_csv(path + path2 + 'Disprop_analysis_male_with_HTs.csv')
    #df_f = pd.read_csv(path + path2 + 'Disprop_analysis_female_with_HTs_before_filtering_v2.csv')
    #df_m = pd.read_csv(path + path2 + 'Disprop_analysis_male_with_HTs_before_filtering_v2.csv')

    hts = ['psychiatric disorders', 'nervous system disorders']
    drug = [drug1, drug2]
    df_m1 = df_m[df_m['DRUG'].isin(drug)]
    df_f1 = df_f[df_f['DRUG'].isin(drug)]
    df_m1 = df_m1[df_m1['HT'].isin(hts)]
    df_f1 = df_f1[df_f1['HT'].isin(hts)]
    df_f1['Sex'] = 'F'
    df_m1['Sex'] = 'M'
    frames = [df_f1, df_m1]
    df = pd.concat(frames)
    df = df.drop(df[df.AE == 'agitation neonatal'].index)
    df = df.drop(df[df.AE == 'foetal alcohol syndrome'].index)
    #df = df.drop(df[df.score < 50].index)
    print(df)
    scatter(df, drug1, drug2)


def create_bar():
    path2 = 'data\\data\\Old_gold\\'
    #path2 = 'data/Old_gold/'
    df_f_old = pd.read_csv(path + path2 + 'Disprop_analysis_female_with_HTs_before_filtering_v2.csv')
    df_m_old = pd.read_csv(path + path2 + 'Disprop_analysis_male_with_HTs_before_filtering_v2.csv')
    hts = ['psychiatric disorders', 'nervous system disorders']
    drug = ['midazolam', 'flurazepam']
    df_m_old = df_m_old[df_m_old['DRUG'].isin(drug)]
    df_f_old = df_f_old[df_f_old['DRUG'].isin(drug)]
    df_m_old = df_m_old[df_m_old['HT'].isin(hts)]
    df_f_old = df_f_old[df_f_old['HT'].isin(hts)]
    df_f_old['Sex'] = 'F'
    df_m_old['Sex'] = 'M'
    frames = [df_f_old, df_m_old]
    df = pd.concat(frames)
    df = df.sort_values(by=['IC025'], ascending=True)
    # df1 = df1.head(20)
    # df2 = df.sort_values(by=['IC025'], ascending=False)
    # df2 = df2.head(20)
    # aes = df1['AE'].tolist() + df2['AE'].tolist()
    # df = df[df['AE'].isin(aes)]
    df = df.drop_duplicates(subset=['DRUG', 'AE', 'Sex', 'Reports'])
    find_max(df)
    # bar_chart(df)


def find_max(df):
    aes = df['AE'].tolist()
    maxis = {}
    for item in aes:
        df_sub = df[df['AE'] == item]
        df_zop = df_sub[df_sub['DRUG'] == 'brotizolam']
        df_eszop = df_sub[df_sub['DRUG'] == 'etizolam']
        maxZop = df_zop['IC025'].max()
        maxEsz = df_eszop['IC025'].max()
        diff = abs(maxZop-maxEsz)
        print([diff, maxEsz, maxZop, item])
        if math.isnan(diff):
            continue
        if item not in maxis:
            maxis[item] = diff
        else:
            continue
    maxis = dict(sorted(maxis.items(), key=lambda item: item[1]))
    aes = []
    i = 1
    it = list(maxis.items())
    while i <= 10:
        x = it[-i]
        aes.append(x[0])
        i += 1
    print(maxis)
    print(aes)
    df = df[df['AE'].isin(aes)]
    bar_chart(df)


def main():
    create_scatter(drug_1, drug_2)
    """
    drug_totals = drug_totals[drug_totals['DRUG'].isin(drug)]

    df_f1['Gender'] = 'F'
    df_m1['Gender'] = 'M'

    frames = [df_f1, df_m1]
    df = pd.concat(frames)
    df_final = pd.DataFrame(columns=['DRUG', 'AE', 'Sex', 'Reports', 'Reports_percentages'])
    for index, row in df.iterrows():
        drug_totals_sub = drug_totals[drug_totals['Sex'] == row['Gender']]
        drug_totals_sub = drug_totals_sub[drug_totals_sub['DRUG'] == row['DRUG']]
        rep_per = (row['Reports'] / drug_totals_sub.iloc[0]['Reports']) * 100
        df_final = df_final.append({'DRUG': row['DRUG'], 'AE': row['AE'], 'Sex': row['Gender'],
                                    'Reports': row['Reports'], 'Reports_percentages': rep_per}, ignore_index=True)
    df_final = df_final.drop_duplicates(subset=['DRUG', 'AE', 'Sex', 'Reports', 'Reports_percentages'], keep='first', ignore_index=True)
    df_final.to_csv('Zopi_eszopi.csv')"""
    # pie_chart(df_m1, 'M', 'eszopiclone')
    # pie_chart(df_f1, 'F', 'eszopiclone')


if __name__ == '__main__':
    main()
