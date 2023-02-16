import pandas as pd
import plotly.express as px
import warnings
import settings
warnings.filterwarnings("ignore")
pd.set_option('display.max_columns', 1000)  # or None
pd.set_option('display.max_rows', 1000)  # or None
pd.set_option('display.max_colwidth', 100)  # or None

#path = 'C:\\Users\\TARIQOPLATA\\PycharmProjects\\FAERS_final\\'
path = '/Users/ftk/Documents/Work/FAERS_final/'


def bar_chart(df):
    #df = df[df['Sex'] == 'M']
    fig = px.bar(df, x="AE", y="IC025", color='DRUG', barmode='stack', height=400)
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


def scatter(df):
    df = df.drop_duplicates(subset=['DRUG', 'AE', 'IC025', 'Reports', 'Sex'])
    df_e = df[df['DRUG'] == 'eszopiclone']
    df_e = df_e.drop_duplicates(subset=['DRUG', 'AE'])
    df_e = df_e.sort_values(by=['IC025'], ascending=False)
    df_e = df_e.head(10)
    print(df_e)
    df_z = df[df['DRUG'] == 'zopiclone']
    df_z = df_z.drop_duplicates(subset=['DRUG', 'AE'])
    df_z = df_z.sort_values(by=['IC025'], ascending=False)
    df_z = df_z.head(10)
    print(df_z)
    #df2 = df.groupby(by=['AE'], as_index=False).sum()
    #df2 = df2.sort_values(by=['IC025'], ascending=False)
    #df2 = df2.head(20)
    #aes = df2['AE'].tolist()
    aes = df_e['AE'].tolist() + df_z['AE'].tolist()
    df = df[df['AE'].isin(aes)]
    fig = px.scatter(df, y="IC025", x="AE", color="Sex", symbol="DRUG", color_discrete_map=settings.colors_g)
    fig.update_traces(marker_size=15)
    #fig.update_layout(scattermode="group")
    fig.show()


def create_scatter():
    path2 = 'data\\Old_gold\\'
    path2 = 'data/Old_gold/'
    df_f = pd.read_csv(path + path2 + 'Disprop_analysis_female_with_HTs.csv')
    df_m = pd.read_csv(path + path2 + 'Disprop_analysis_male_with_HTs.csv')

    hts = ['psychiatric disorders', 'nervous system disorders']
    drug = ['zopiclone', 'eszopiclone']
    df_m1 = df_m[df_m['DRUG'].isin(drug)]
    df_f1 = df_f[df_f['DRUG'].isin(drug)]
    df_m1 = df_m1[df_m1['HT'].isin(hts)]
    df_f1 = df_f1[df_f1['HT'].isin(hts)]
    df_f1['Sex'] = 'F'
    df_m1['Sex'] = 'M'
    frames = [df_f1, df_m1]
    df = pd.concat(frames)
    scatter(df)


def create_bar():
    path2 = 'data\\Old_gold\\'
    path2 = 'data/Old_gold/'
    df_f_old = pd.read_csv(path + path2 + 'Disprop_analysis_female_with_HTs_before_filtering_v2.csv')
    df_m_old = pd.read_csv(path + path2 + 'Disprop_analysis_male_with_HTs_before_filtering_v2.csv')
    hts = ['psychiatric disorders', 'nervous system disorders']
    drug = ['zopiclone', 'eszopiclone']
    df_m_old = df_m_old[df_m_old['DRUG'].isin(drug)]
    df_f_old = df_f_old[df_f_old['DRUG'].isin(drug)]
    df_m_old = df_m_old[df_m_old['HT'].isin(hts)]
    df_f_old = df_f_old[df_f_old['HT'].isin(hts)]
    df_f_old['Sex'] = 'F'
    df_m_old['Sex'] = 'M'
    frames = [df_f_old, df_m_old]
    df = pd.concat(frames)
    df1 = df.sort_values(by=['IC025'], ascending=True)
    df1 = df1.head(20)
    df2 = df.sort_values(by=['IC025'], ascending=False)
    df2 = df2.head(20)
    aes = df1['AE'].tolist() + df2['AE'].tolist()
    df = df[df['AE'].isin(aes)]
    df = df.drop_duplicates(subset=['DRUG', 'AE', 'Sex', 'Reports'])
    bar_chart(df)


def main():
    create_bar()
    #drug_totals = pd.read_csv(path + 'data/New/Drugs_Gender_Size.csv')



    #df_m1_old = df_m_old[df_m_old['DRUG'].isin(drug)]
    #df_f1_old = df_f_old[df_f_old['DRUG'].isin(drug)]
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
    #pie_chart(df_m1, 'M', 'eszopiclone')
    #pie_chart(df_f1, 'F', 'eszopiclone')


if __name__ == '__main__':
    main()
