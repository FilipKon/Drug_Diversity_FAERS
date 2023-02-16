import pandas as pd
import plotly.express as px
import warnings
import settings
warnings.filterwarnings("ignore")

path = 'C:\\Users\\TARIQOPLATA\\PycharmProjects\\FAERS_final\\'
#path = '\Users\'


def bar_chart(df, sex):
    df = df[df['Sex'] == 'M']
    fig = px.bar(df, x="AE", y="Reports_percentages", color='DRUG', barmode='group', height=400)
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
    df2 = df.groupby(by=['AE'], as_index=False).sum()
    df2 = df2.sort_values(by=['IC025'], ascending=False)
    df2 = df2.head(20)
    print(df2)
    aes = df2['AE'].tolist()
    df = df[df['AE'].isin(aes)]
    fig = px.scatter(df, y="IC025", x="AE", color="Sex", symbol="DRUG", color_discrete_map=settings.colors_g)
    fig.update_traces(marker_size=15)
    #fig.update_layout(scattermode="group")
    fig.show()


def main():
    df_f = pd.read_csv(path + 'data\\Old_gold\\Disprop_analysis_female_with_HTs.csv')
    df_m = pd.read_csv(path + 'data\\Old_gold\\Disprop_analysis_male_with_HTs.csv')
    df_f_old = pd.read_csv(path + 'data\\Old_gold\\Disprop_analysis_female_with_HTs_before_filtering_v2.csv')
    df_m_old = pd.read_csv(path + 'data\\Old_gold\\Disprop_analysis_male_with_HTs_before_filtering_v2.csv')
    drug_totals = pd.read_csv(path + 'data\\New\\Drugs_Gender_Size.csv')
    hts = ['psychiatric disorders', 'nervous system disorders']
    #'investigations', 'injury;poisoning and procedural complications'
    drug = ['zopiclone', 'eszopiclone']
    df_m1 = df_m[df_m['DRUG'].isin(drug)]
    df_f1 = df_f[df_f['DRUG'].isin(drug)]
    df_m1 = df_m1[df_m1['HT'].isin(hts)]
    df_f1 = df_f1[df_f1['HT'].isin(hts)]
    df_f1['Sex'] = 'F'
    df_m1['Sex'] = 'M'
    frames = [df_f1, df_m1]
    df = pd.concat(frames)
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
    scatter(df)


if __name__ == '__main__':
    main()
