import pandas as pd
import plotly.express as px
import warnings
import numpy as np
import plotly.graph_objs as go

warnings.filterwarnings("ignore")
pd.set_option('display.max_columns', 1000)  # or None
pd.set_option('display.max_rows', 1000)  # or None
pd.set_option('display.max_colwidth', 100)  # or None
colors_g = {'F': '#e5a2bd', 'M': '#9aceeb'}


def main():
    path = 'C:\\Users\\TARIQOPLATA\PycharmProjects\\FAERS_final\\data\\data\\Old_gold\\'
    # path = '/Users/ftk/Documents/Work/FAERS_final/data/Old_gold/'
    df_f_all = pd.read_csv(path + 'Disprop_analysis_female_with_HTs_before_filtering_v2.csv')
    df_m_all = pd.read_csv(path + 'Disprop_analysis_male_with_HTs_before_filtering_v2.csv')

    df_f = pd.read_csv(path + 'Disprop_analysis_female_with_HTs.csv')
    df_m = pd.read_csv(path + 'Disprop_analysis_male_with_HTs.csv')
    hts = ['nervous system disorders', 'psychiatric disorders']
    df_f = df_f[df_f['HT'].isin(hts)]
    df_m = df_m[df_m['HT'].isin(hts)]
    df_f_all = df_f_all[df_f_all['HT'].isin(hts)]
    df_m_all = df_m_all[df_m_all['HT'].isin(hts)]
    drug = ['nordazepam']
    df_f = df_f[df_f['DRUG'].isin(drug)]
    df_m = df_m[df_m['DRUG'].isin(drug)]
    df_f_all = df_f_all[df_f_all['DRUG'].isin(drug)]
    df_m_all = df_m_all[df_m_all['DRUG'].isin(drug)]
    df_f_all['Sex'] = 'F'
    df_m_all['Sex'] = 'M'
    frames = [df_f_all, df_m_all]
    df_full = pd.concat(frames)

    # Get only males and only female aes
    f_aes = df_f['AE'].tolist()
    m_aes = df_m['AE'].tolist()
    print(f_aes)
    print(m_aes)
    only_f = get_diffs(f_aes, m_aes)
    only_f = list(dict.fromkeys(only_f))
    only_m = get_diffs(m_aes, f_aes)
    only_m = list(dict.fromkeys(only_m))

    # FIRST ONLY MALE
    df_full2 = df_full[df_full['AE'].isin(only_m)]
    df_full2 = df_full2.sort_values(by=['IC025'], ascending=False)
    df_full2 = df_full2.head(20)
    top20_aes = df_full2['AE'].tolist()
    df_full2 = df_full[df_full['AE'].isin(top20_aes)]
    df_full2 = df_full2.sort_values(by=['IC025'], ascending=False)
    fig = px.scatter(df_full2, y="IC025", x="AE", color="Sex", symbol="DRUG", color_discrete_map=colors_g,
                     title="AEs for nordazepam for male only Top 20")
    fig.update_layout(font=dict(size=18))
    fig.update_traces(marker_size=15)
    fig.update_xaxes(categoryorder='total descending')
    fig.show()

    # FIRST ONLY FEMALE
    df_full2 = df_full[df_full['AE'].isin(only_f)]
    df_full2 = df_full2.sort_values(by=['IC025'], ascending=False)
    df_full2 = df_full2.head(20)
    top20_aes = df_full2['AE'].tolist()
    df_full2 = df_full[df_full['AE'].isin(top20_aes)]
    df_full2 = df_full2.sort_values(by=['IC025'], ascending=False)
    fig = px.scatter(df_full2, y="IC025", x="AE", color="Sex", symbol="DRUG", color_discrete_map=colors_g,
                     title="AEs for nordazepam for female only Top 20")
    fig.update_layout(font=dict(size=18))
    fig.update_traces(marker_size=15)
    fig.update_xaxes(categoryorder='total descending')
    fig.show()


def get_diffs(df_1, df_2):
    df = []
    for item in df_1:
        if item not in df_2:
            df.append(item)
        else:
            continue
    return df


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


if __name__ == '__main__':
    main()
