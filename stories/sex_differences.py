import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

pd.set_option('display.max_columns', 100)  # or 1000
pd.set_option('display.max_rows', 100)  # or 1000
pd.set_option('display.max_colwidth', 100)  # or 199
colors_g = {'F': '#e5a2bd', 'M': '#9aceeb'}
path = 'C:\\Users\\TARIQOPLATA\\PycharmProjects\\FAERS_final\\data\\data\\Old_gold\\'
# path = '\Users\'


def main():
    df_f = pd.read_csv(path + 'Disprop_analysis_female_with_HTs_before_filtering_v2.csv')
    df_m = pd.read_csv(path + 'Disprop_analysis_male_with_HTs_before_filtering_v2.csv')
    df_f = pd.read_csv(path + 'Disprop_analysis_female_with_HTs.csv')
    df_m = pd.read_csv(path + 'Disprop_analysis_male_with_HTs.csv')
    hts = ['psychiatric disorders', 'nervous system disorders']
    sex_totals = {'F': 2775448, 'M': 1488960}
    df_f = df_f[df_f['HT'].isin(hts)]
    df_m = df_m[df_m['HT'].isin(hts)]
    #aes = ['sopor', 'logorrhoea', 'muscle rigidity', 'presenile dementia',
    # 'extrapyrimidal disorder', 'akathisia', 'serotonin syndrome', 'disorientation']
    #df_f = df_f[df_f['AE'].isin(aes)]
    #df_m = df_m[df_m['AE'].isin(aes)]
    df_m['Sex'] = 'M'
    df_f['Sex'] = 'F'
    df_f = df_f.drop('IDX', axis=1)
    df_m = df_m.drop('IDX', axis=1)
    df_m1 = df_m.groupby(['DRUG', 'HT'], as_index=False).sum()
    df_f1 = df_f.groupby(['DRUG', 'HT'], as_index=False).sum()
    fig = go.Figure(data=go.Heatmap(
        x=df_f1['DRUG'],
        y=df_f1['HT'],
        z=df_f1['IC025'], texttemplate="%{text}", text=df_f1['IC025']))
    fig.update_layout(title='Female')
    fig.show()
    #frames = [df_f, df_m]
    #df = pd.concat(frames)

    #df = df.drop(df[df.DRUG == 'zolazepam'].index)
    #df = df.drop(df[df.DRUG == 'nimetazepam'].index)
    #df = df.drop(df[df.DRUG == 'pinazepam'].index)
    #df = df.drop(df[df.DRUG == 'remimazolam'].index)
    #df = df.drop(df[df.DRUG == 'bentazepam'].index)
   #df = df.drop(df[df.DRUG == 'cinolazepam'].index)
    #df = df.drop(df[df.DRUG == 'medazepam'].index)
    #df = df.drop(df[df.DRUG == 'ketazolam'].index)
    #df = df.drop(df[df.DRUG == 'halazepam'].index)

    #df = df.groupby(['AE', 'Sex'], as_index=False).sum()
    df = df.sort_values(by=['IC025'], ascending=False)
    #df_m = df_m.sort_values(by=['IC025'], ascending=False)
    #df_f = df_f.sort_values(by=['IC025'], ascending=False)
    print(df)
    fig = px.bar(df, x='AE', y='IC025', color='Sex', barmode="group")
    fig.show()
    """
    df_1 = df[df['Sex']=='M']
    fig = px.pie(df_1, values='IC025', names='DRUG', title='Male', hole=.2, color='DRUG')
    fig.show()
    df_1 = df[df['Sex']=='F']
    fig = px.pie(df_1, values='IC025', names='DRUG', title='Female', hole=.2, color='DRUG')
    fig.show()
    df = df.drop(df[df.IC025 < 0].index)
    df = df.drop(df[df.PRR < 2].index)
    df = df.drop(df[df.Reports < 5].index)
    df_1 = df[df['Sex']=='M']
    fig = px.pie(df_1, values='IC025', names='AE', title='Male', hole=.2, color='AE')
    fig.show()
    df_1 = df[df['Sex']=='F']
    fig = px.pie(df_1, values='IC025', names='AE', title='Female', hole=.2, color='AE')
    fig.show()

    df_1 = df[df['Sex']=='M']
    fig = px.pie(df_1, values='IC025', names='HT_level2', title='Male', hole=.2, color='HT_level2')
    fig.show()
    df_1 = df[df['Sex']=='F']
    fig = px.pie(df_1, values='IC025', names='HT_level2', title='Female', hole=.2, color='HT_level2')
    fig.show()"""


if __name__ == '__main__':
    main()
