import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import settings
import warnings
from plotly.subplots import make_subplots

warnings.filterwarnings("ignore")
pd.set_option('display.max_columns', 1000)  # or None
pd.set_option('display.max_rows', 1000)  # or None
pd.set_option('display.max_colwidth', 100)  # or None


def bar_chart(df, ht, sex, fig, i):
    df = df[df['Sex'] == sex]
    df = df[df['HT_level2'] == ht]
    df = df.sort_values(by='IC025', ascending=False)

    fig.add_trace(
        go.Bar(
            x=df['HT_level2'],
            y=[df['Reports'].sum()],
            name=sex,
            marker_color=settings.colors_g.get(sex),
            offsetgroup=i,
            legendgroup=i,
            opacity=0.5,
            #legendgrouptitle_text="Smoker",
        ),
        secondary_y=True
    )
    return fig
    """
    fig = px.bar(df, x="AE", y="IC025", color='Sex', barmode='group', height=400, #pattern_shape="DRUG",
                 color_discrete_map=settings.colors_g)
    #pattern_shape_map={'zopiclone': '+', 'eszopiclone': '-'}
    # ["+", "-"]
    fig.update_layout(
        font=dict(
            size=18,
        )
    )
    fig.show()"""


def scatter_chart(df, ht, sex, fig, i):
    df = df[df['Sex'] == sex]
    df = df[df['HT_level2'] == ht]
    df = df.sort_values(by='IC025', ascending=False)
    drugs = df['DRUG'].tolist()
    drugs = list(dict.fromkeys(drugs))
    for item in drugs:
        df2 = df[df['DRUG'] == item]
        fig.add_trace(
            go.Scatter(
                x=df2['HT_level2'],
                y=[df2['IC025'].sum()],
                mode="markers",
                name=item,
                marker=dict(color=settings.colors_d[item]),
                #marker=settings.symbols.get(item),
                offsetgroup=i,
                legendgroup=i,
            ),
            secondary_y=False
        )
    return fig


def main():
    df_f = pd.read_csv('/Users/ftk/Documents/Work/FAERS_final/data/Old_gold/Disprop_analysis_female_with_HTs.csv')
    df_m = pd.read_csv('/Users/ftk/Documents/Work/FAERS_final/data/Old_gold/Disprop_analysis_male_with_HTs.csv')
    hts = ['anxiety disorders and symptoms', 'suicidal and self-injurious behaviours nec',
           'sleep disorders and disturbances', 'psychiatric disorders nec']
    #'sleep disturbances (incl subtypes)' SLEEPS PUT TOGETHER
    df_f = df_f[df_f['HT_level2'].isin(hts)]
    df_m = df_m[df_m['HT_level2'].isin(hts)]
    df_f['Sex'] = 'F'
    df_m['Sex'] = 'M'
    frames = [df_f, df_m]
    df = pd.concat(frames)
    df = df.drop_duplicates(subset=['DRUG', 'AE', 'IC025', 'Sex', 'Reports'], keep='first', ignore_index=True)

    # Create a bar and scatter plot in one separated by hts and sex, using DRUG for scatter and Reports for bar

    fig = go.Figure(
        layout=dict(
            xaxis=dict(categoryorder="category descending"),
            #yaxis=dict(range=[0, 7]),
            scattermode="group",
            legend=dict(groupclick="toggleitem"),
        ),
    )
    fig = make_subplots(specs=[[{"secondary_y": True}]])
    fig.update_layout(scattermode="group")
    for item in hts:
        fig = bar_chart(df, item, 'M', fig, 1)
        scatter_chart(df, item, 'M', fig, 1)
        fig = bar_chart(df, item, 'F', fig, 2)
        scatter_chart(df, item, 'F', fig, 2)
    fig.show()


    #fig.show()


if __name__ == '__main__':
    main()
