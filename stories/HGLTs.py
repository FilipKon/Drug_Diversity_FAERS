import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
# import settings
import warnings
from plotly.subplots import make_subplots
import SOC
warnings.filterwarnings("ignore")
pd.set_option('display.max_columns', 100)  # or None
pd.set_option('display.max_rows', None)  # or None
pd.set_option('display.max_colwidth', 100)  # or None

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
drugs_alpha = {'alprazolam': 962, 'bromazepam': 963, 'brotizolam': 964, 'chlordiazepoxide': 965, 'cinolazepam': 966,
               'clobazam': 967, 'clonazepam': 968, 'clorazepate': 969, 'clotiazepam': 970, 'cloxazolam': 971,
               'diazepam': 972, 'estazolam': 973, 'eszopiclone': 974, 'ethyl loflazepate': 975, 'etizolam': 976,
               'flumazenil': 977, 'flunitrazepam': 978, 'flurazepam': 979, 'ketazolam': 980, 'lorazepam': 981,
               'lormetazepam': 982, 'medazepam': 983, 'mexazolam': 984, 'midazolam': 985, 'nimetazepam': 986,
               'nitrazepam': 987,
               'nordazepam': 988, 'oxazepam': 989, 'oxazolam': 990, 'prazepam': 991, 'quazepam': 992, 'temazepam': 993,
               'tetrazepam': 994, 'tofisopam': 995, 'triazolam': 996, 'triazulenone': 997, 'zaleplon': 998,
               'zolpidem': 999, 'zopiclone': 1000}


def bar_chart(df, ht, sex, fig, i):
    df = df[df['Sex'] == sex]
    df = df[df['HT_level2'] == ht]
    df = df.sort_values(by='IC025', ascending=False)

    fig.add_trace(
        go.Bar(
            x=df['HT_level2'],
            y=[df['Reports'].sum()],
            name=sex,
            marker_color=colors_g.get(sex),
            offsetgroup=i,
            legendgroup=i,
            opacity=0.5,
            showlegend=False
            # legendgrouptitle_text="Smoker",
        ),
        secondary_y=True
    )
    return fig


def scatter_chart(df, ht, sex, fig, i, j):
    df = df[df['Sex'] == sex]
    df = df[df['HT_level2'] == ht]
    df = df.sort_values(by='DRUG', ascending=True)
    drugs = df['DRUG'].tolist()
    drugs = list(dict.fromkeys(drugs))
    for item in drugs:
        df2 = df[df['DRUG'] == item]
        if j == 0:
            fig.add_trace(
                go.Scatter(
                    x=df2['HT_level2'],
                    y=[df2['IC025'].sum()],
                    mode="markers",
                    name=item,
                    # marker_symbols=symbols.get(item),
                    marker=dict(symbol=symbols.get(item), color=colors_d.get(item), size=15),
                    # marker=dict(color=colors_d.get(item)),
                    # marker=settings.symbols.get(item),
                    offsetgroup=i,
                    legendgroup=i,
                    showlegend=True
                ),
                secondary_y=False
            )
            fig.update_traces(legendrank=drugs_alpha.get(item))
        else:
            fig.add_trace(
                go.Scatter(
                    x=df2['HT_level2'],
                    y=[df2['IC025'].sum()],
                    mode="markers",
                    name=item,
                    # marker_symbols=symbols.get(item),
                    marker=dict(symbol=symbols.get(item), color=colors_d.get(item), size=15),
                    # marker=dict(color=colors_d.get(item)),
                    # marker=settings.symbols.get(item),
                    offsetgroup=i,
                    legendgroup=i,
                    showlegend=False
                ),
                secondary_y=False
            )
            fig.update_traces(legendrank=drugs_alpha.get(item))
    return fig


def bar_chart_v2(df, ht, sex, fig, i):
    df = df[df['Sex'] == sex]
    df = df[df['HT_level2'] == ht]
    df = df.sort_values(by='Reports_Percent', ascending=False)

    fig.add_trace(
        go.Bar(
            x=df['HT_level2'],
            y=[df['Reports_Percent'].sum()],
            name=sex,
            marker_color=colors_g.get(sex),
            offsetgroup=i,
            legendgroup=i,
            opacity=0.5,
            showlegend=False
            # legendgrouptitle_text="Smoker",
        ),
        secondary_y=True
    )
    return fig


def scatter_chart_v2(df, ht, sex, fig, i, j):
    df = df[df['Sex'] == sex]
    df = df[df['HT_level2'] == ht]
    df = df.sort_values(by='DRUG', ascending=True)
    drugs = df['DRUG'].tolist()
    drugs = list(dict.fromkeys(drugs))
    for item in drugs:
        df2 = df[df['DRUG'] == item]
        if j == 0:
            fig.add_trace(
                go.Scatter(
                    x=df2['HT_level2'],
                    y=[df2['Reports_Percent'].sum()],
                    mode="markers",
                    name=item,
                    # marker_symbols=symbols.get(item),
                    marker=dict(symbol=symbols.get(item), color=colors_d.get(item), size=15),
                    # marker=dict(color=colors_d.get(item)),
                    # marker=settings.symbols.get(item),
                    offsetgroup=i,
                    legendgroup=i,
                    showlegend=True
                ),
                secondary_y=False
            )
            fig.update_traces(legendrank=drugs_alpha.get(item))
        else:
            fig.add_trace(
                go.Scatter(
                    x=df2['HT_level2'],
                    y=[df2['Reports_Percent'].sum()],
                    mode="markers",
                    name=item,
                    # marker_symbols=symbols.get(item),
                    marker=dict(symbol=symbols.get(item), color=colors_d.get(item), size=15),
                    # marker=dict(color=colors_d.get(item)),
                    # marker=settings.symbols.get(item),
                    offsetgroup=i,
                    legendgroup=i,
                    showlegend=False
                ),
                secondary_y=False
            )
            fig.update_traces(legendrank=drugs_alpha.get(item))
    return fig


def create_hglts_v1():
    path = 'C:\\Users\\TARIQOPLATA\PycharmProjects\\FAERS_final\\data\\data\\Old_gold\\'
    #path = '/Users/ftk/Documents/Work/FAERS_final/data/Old_gold/'
    # path = '/Users/ftk/Documents/Work/FAERS_final/data/Old_gold/'
    df_f = pd.read_csv(path + 'Disprop_analysis_female_with_HTs.csv')
    df_m = pd.read_csv(path + 'Disprop_analysis_male_with_HTs.csv')
    hts = ['anxiety disorders and symptoms']
    #'suicidal and self-injurious behaviours nec',
    #       'sleep disorders and disturbances', 'psychiatric disorders nec'
    # 'sleep disturbances (incl subtypes)' SLEEPS PUT TOGETHER
    df_f = df_f[df_f['HT_level2'].isin(hts)]
    df_m = df_m[df_m['HT_level2'].isin(hts)]
    df_f['Sex'] = 'F'
    df_m['Sex'] = 'M'
    frames = [df_f, df_m]
    df = pd.concat(frames)
    df = df.drop_duplicates(subset=['DRUG', 'AE', 'IC025', 'Sex', 'Reports'], keep='first', ignore_index=True)

    fig = make_subplots(specs=[[{"secondary_y": True}]])
    fig.update_layout(scattermode="group", xaxis=dict(title='higher level group terms (HLGT)'),
                      yaxis=dict(
                          title="IC025 (drugs)",
                      ),
                      yaxis2=dict(
                          title="Reports (sex)"),
                      font=dict(
                          size=18
                      ))
    j = 0
    for item in hts:
        fig = bar_chart(df, item, 'M', fig, 1)
        scatter_chart(df, item, 'M', fig, 1, j)
        j += 1
        fig = bar_chart(df, item, 'F', fig, 2)
        scatter_chart(df, item, 'F', fig, 2, j)

    fig.show()


def get_perc(df):
    df = df.drop_duplicates(subset=['DRUG', 'AE', 'IC025', 'Reports'], keep='first')
    df_drug = pd.read_csv('C:\\Users\\TARIQOPLATA\\PycharmProjects\\FAERS_final\\data\\data\\New\\Drugs_Gender_Size.csv')
    #df_drug = pd.read_csv('/Users/ftk/Documents/Work/FAERS_final/data/New/Drugs_Gender_Size.csv')
    df_fin = pd.DataFrame(columns=['DRUG', 'AE', 'Sex', 'Reports', 'Reports_Percent', 'IC025', 'Total_Reports', 'HT', 'HT_level2'])
    for index, row in df.iterrows():
        df_sub_drug = df_drug[df_drug['DRUG'] == row['DRUG']]
        df_sub_drug = df_sub_drug[df_sub_drug['Sex'] == row['Sex']]
        ae_perc = (row['Reports'] / df_sub_drug['Reports'].values[0]) * 100
        ae_perc = round(ae_perc, 3)
        df_fin = df_fin.append({'DRUG': str(row['DRUG']), 'AE': row['AE'], 'Sex': row['Sex'], 'Reports': row['Reports'],
                                'Reports_Percent': ae_perc, 'IC025': row['IC025'],
                                'Total_Reports': df_sub_drug['Reports'].values[0], 'HT': row['HT'],
                                'HT_level2': row['HT_level2']},
                               ignore_index=True)
    return df_fin


def create_perc_figures(df, hts, fig):
    # Create 2 layered bar chart with hts and sex separately
    j = 0
    for item in hts:
        fig = bar_chart_v2(df, item, 'M', fig, 1)
        fig = bar_chart_v2(df, item, 'F', fig, 2)
        fig = scatter_chart(df, item, 'F', fig, 2, j)
        fig = scatter_chart(df, item, 'M', fig, 1, j)
        j += 1
    return fig


def main_v1():
    #path = '/Users/ftk/Documents/Work/FAERS_final/data/Old_gold/'
    path = 'C:\\Users\\TARIQOPLATA\PycharmProjects\\FAERS_final\\data\\data\\Old_gold\\'
    # path = '/Users/ftk/Documents/Work/FAERS_final/data/Old_gold/'
    df_f = pd.read_csv(path + 'Disprop_analysis_female_with_HTs.csv')
    df_m = pd.read_csv(path + 'Disprop_analysis_male_with_HTs.csv')
    hts = ['psychiatric disorders nec', 'suicidal and self-injurious behaviours nec', 'anxiety disorders and symptoms',
           'sleep disorders and disturbances', 'sleep disturbances (incl subtypes)']
        #, 'suicidal and self-injurious behaviours nec',
        #   'sleep disorders and disturbances', 'psychiatric disorders nec']
    # 'sleep disturbances (incl subtypes)' SLEEPS PUT TOGETHER
    df_f = df_f[df_f['HT_level2'].isin(hts)]
    df_m = df_m[df_m['HT_level2'].isin(hts)]

    df_f['Sex'] = 'F'
    df_m['Sex'] = 'M'
    frames = [df_f, df_m]
    df = pd.concat(frames)
    print(df)

    df['HT_level2'] = df['HT_level2'].replace(['sleep disturbances (incl subtypes)'], 'sleep disorders and disturbances (incl subtypes)')
    df['HT_level2'] = df['HT_level2'].replace(['sleep disorders and disturbances'], 'sleep disorders and disturbances (incl subtypes)')

    df = df.drop_duplicates(subset=['DRUG', 'AE', 'IC025', 'Sex', 'Reports'], keep='first', ignore_index=True)
    hts = ['psychiatric disorders nec', 'suicidal and self-injurious behaviours nec', 'anxiety disorders and symptoms',
           'sleep disorders and disturbances (incl subtypes)']
    df = get_perc(df)
    print(df)
    fig = go.Figure(
        layout=dict(
            xaxis=dict(categoryorder="category descending"),
            # yaxis=dict(range=[0, 7]),
            scattermode="group",
            legend=dict(groupclick="toggleitem"),
        ),
    )
    fig = make_subplots(specs=[[{"secondary_y": True}]])
    fig.update_layout(scattermode="group", xaxis=dict(title='higher level group terms (HLGT)'),
                      yaxis=dict(
                          title="IC025 (drugs)",
                      ),
                      yaxis2=dict(
                          title="Reports_Percent (sex)"),
                      font=dict(
                          size=18
                      ))
    fig = create_perc_figures(df, hts, fig)
    fig.show()
    j = 0
    #for item in hts:
    #    fig = bar_chart_v2(df, item, 'M', fig, 1)
        #fig = scatter_chart_v2(df, item, 'M', fig, 1, j)
    #    fig = scatter_chart(df, item, 'M', fig, 1, j)
    #    j += 1
    #    fig = bar_chart_v2(df, item, 'F', fig, 2)
        #fig = scatter_chart_v2(df, item, 'F', fig, 2, j)
    #    fig = scatter_chart(df, item, 'F', fig, 2, j)
    #fig.show()

    # fig.show()


def main():
    #path = '/Users/ftk/Documents/Work/FAERS_final/data/Old_gold/'
    path = 'C:\\Users\\TARIQOPLATA\PycharmProjects\\FAERS_final\\data\\data\\Old_gold\\'
    # path = '/Users/ftk/Documents/Work/FAERS_final/data/Old_gold/'
    df_f = pd.read_csv(path + 'Disprop_analysis_female_with_HTs.csv')
    df_m = pd.read_csv(path + 'Disprop_analysis_male_with_HTs.csv')
    hts = ['psychiatric disorders nec', 'suicidal and self-injurious behaviours nec', 'anxiety disorders and symptoms',
           'sleep disorders and disturbances', 'sleep disturbances (incl subtypes)']

    df_f = df_f[df_f['HT_level2'].isin(hts)]
    df_m = df_m[df_m['HT_level2'].isin(hts)]

    df_f['Sex'] = 'F'
    df_m['Sex'] = 'M'
    frames = [df_f, df_m]
    df = pd.concat(frames)
    print(df)

    df['HT_level2'] = df['HT_level2'].replace(['sleep disturbances (incl subtypes)'], 'sleep disorders and disturbances (incl subtypes)')
    df['HT_level2'] = df['HT_level2'].replace(['sleep disorders and disturbances'], 'sleep disorders and disturbances (incl subtypes)')

    df = df.drop_duplicates(subset=['DRUG', 'AE', 'IC025', 'Sex', 'Reports'], keep='first', ignore_index=True)
    hts = ['psychiatric disorders nec', 'suicidal and self-injurious behaviours nec', 'anxiety disorders and symptoms',
           'sleep disorders and disturbances (incl subtypes)']
    df = get_perc(df)

    #fig = px.bar(df, x='Reports_Percent', y='DRUG', color='Sex',  barmode='group', pattern_shape="HT_level2",
    #             pattern_shape_sequence=[".", "x", "+", "/"], color_discrete_map=colors_g, orientation='h')
    fig = go.Figure(
        layout=dict(
            xaxis=dict(categoryorder="category descending"),
            # yaxis=dict(range=[0, 7]),
            #scattermode="group",
            legend=dict(groupclick="toggleitem"),
        ),
    )
    drugs = df['DRUG'].tolist()
    drugs = list(dict.fromkeys(drugs))
    drugs = sorted(drugs)
    sexes = ['F', 'M', 'F', 'M', 'F', 'M', 'F', 'M', 'M', 'F', 'M', 'F', 'M', 'F', 'M', 'F', 'M', 'F', 'M', 'F', 'M', 'F', 'M', 'F', 'M'
             , 'F', 'M', 'F', 'M', 'F', 'M', 'F', 'M', 'F', 'M', 'F', 'M', 'F', 'M', 'F', 'M', 'F', 'M', 'F', 'M', 'F', 'M',
             'F', 'M', 'F', 'M', 'F', 'M', 'F', 'M', 'F', 'M', 'F', 'M', 'F', 'M', 'F', 'M', 'F', 'M', 'F']
    df = df.groupby(by=['DRUG', 'HT_level2', 'Sex'], as_index=False).sum()
    print(df)
    colors = [colors_g[category] for category in sexes]
    for ht in hts:
        df2 = df[df['HT_level2'] == ht]
        print(df2)
        fig.add_trace(
            go.Bar(
                y=[df2['DRUG'], df2['Sex']],
                x=df2['Reports_Percent'],
                name=ht,
                orientation='h'
                #marker_color=colors,
                #marker=dict(pattern=df2["HT_level2"]),
            )
        )
        #fig.update_traces()
        #fig.update_traces(marker_pattern_shape=df2["HT_level2"].map({'psychiatric disorders nec': ".",
        #                                                                'suicidal and self-injurious behaviours nec': "+",
        #                                                                'anxiety disorders and symptoms': "+",
        #                                                                'sleep disorders and disturbances (incl subtypes)': "/"}),
        #                marker_opacity=0.8)
    #fig.update_xaxes(tickangle=45)
    fig.update_layout(barmode="stack")
    fig.show()


def neuro_nec():
    #path = '/Users/ftk/Documents/Work/FAERS_final/data/Old_gold/'
    path = 'C:\\Users\\TARIQOPLATA\PycharmProjects\\FAERS_final\\data\\data\\Old_gold\\'
    # path = '/Users/ftk/Documents/Work/FAERS_final/data/Old_gold/'
    df_f = pd.read_csv(path + 'Disprop_analysis_female_with_HTs.csv')
    df_m = pd.read_csv(path + 'Disprop_analysis_male_with_HTs.csv')
    df_f = df_f[df_f['HT_level2'] == "neurological disorders nec"]
    df_m = df_m[df_m['HT_level2'] == "neurological disorders nec"]
    df_m = df_m.sort_values(['IC025'], ascending=True)
    df_f = df_f.sort_values(['IC025'], ascending=True)

    #df_ae = df_f.groupby(by=['AE'], as_index=False).sum()
    #df_ae = df_ae.sort_values(['IC025'], ascending=False)
    #print(df_ae)

    #df_drug = df_f.groupby(by=['DRUG'], as_index=False).sum()
    #df_drug = df_drug.sort_values(['IC025'], ascending=False)
    #print(df_drug)

    df_f['Sex'] = 'F'
    df_m['Sex'] = 'M'
    frames = [df_f, df_m]
    df = pd.concat(frames)
    df = get_perc(df)
    df = df.sort_values(["DRUG"], ascending=False)
    print(df)
    fig1 = px.bar(df, x="Reports_Percent", y="DRUG", color='Sex', barmode='group', color_discrete_map=colors_g,
                  title="neurological disorders nec", orientation='h')
    fig1.update_xaxes(categoryorder='total ascending')
    fig1.update_yaxes(categoryorder='total ascending')
    fig1.show()


if __name__ == '__main__':
    neuro_nec()
