import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
# import settings
import warnings

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
symbols_d = {'alprazolam': "/", 'diazepam': ".", 'lorazepam': "x", 'clonazepam': "-",
             'zolpidem': "/", 'tetrazepam': "+", 'cloxazolam': ".", 'clotiazepam': ".",
             'flumazenil': "/", 'triazulenone': "x", 'quazepam': "-", 'nordazepam': "|",
             'tofisopam': "+", 'mexazolam': ".", 'ketazolam': "/",
             'cinolazepam': "x", 'oxazolam': "-", 'lormetazepam': "|", 'prazepam': "+",
             'flunitrazepam': ".", 'estazolam': "/", 'ethyl loflazepate': "",
             'etizolam': "-", 'brotizolam': "|", 'clorazepate': "+", 'triazolam': ".",
             'flurazepam': "/", 'zaleplon': "x", 'eszopiclone': "-",
             'zopiclone': "+", 'bromazepam': "/", 'oxazepam': "x", "nitrazepam": "x",
             'clobazam': "/", 'midazolam': "x", 'remimazolam': "-"}
colors_d = {'ethyl loflazepate': '#E45542', 'chlordiazepoxide': '#F7A063', 'alprazolam': '#FF5733',
            'diazepam': '#75A7AB',
            'lorazepam': '#B73C22', 'clonazepam': '#906056',
            'zolpidem': '#9DF8DF', 'tetrazepam': '#ff9d5c', 'cloxazolam': '#4b4c07', 'clotiazepam': '#e9fe92',
            'flumazenil': '#D6DA03', 'triazulenone': '#FFD4EB', 'quazepam': '#F9C469', 'nordazepam': '#68D6DF',
            'tofisopam': '#C3C553', 'mexazolam': '#BEFC8B', 'medazepam': '#44CB99', 'ketazolam': '#636161',
            'cinolazepam': '#C5A9A3', 'oxazolam': '#5FB815', 'lormetazepam': '#66953E', 'prazepam': '#FF0087',
            'flunitrazepam': '#FB11FF', 'nitrazepam': '#E49C20', 'estazolam': '#8E3564',
            'etizolam': '#0CC492', 'brotizolam': '#B498FF', 'clorazepate': '#0CC44C', 'triazolam': '#1349C4',
            'flurazepam': '#75AB9C', 'zaleplon': '#18E4F5', 'eszopiclone': '#00B9FF',
            'temazepam': '#51D4F0', 'zopiclone': '#458AA4', 'bromazepam': '#4562A4', 'oxazepam': '#A585C4',
            'clobazam': '#2C6CFF', 'midazolam': '#98B7FF', 'remimazolam': '#8000FF'}

path = 'C:\\Users\\TARIQOPLATA\\PycharmProjects\\FAERS_final\\'
# path = '/Users/ftk/Documents/Work/FAERS_final'
colors_g = {'F': '#e5a2bd', 'M': '#9aceeb'}


def reports_perc(df, ht2):
    print(df.columns)
    dfx = df.sort_values(['DRUG'], ascending=False, ignore_index=True, kind="mergesort")
    # dfx = df['DRUG'].sort_values(ascending=False, ignore_index=True, kind="mergesort")
    figBAR = px.bar(dfx, x="Reports_Percent", y="DRUG", color='Sex', barmode='group',
                    color_discrete_map=settings.colors_g,
                    title=ht2, orientation='h', hover_data=['AE'])
    figBAR.show()
    figBAR.write_html(path + 'psychiatricdisordersnec.html')


def get_percs():
    df_f = pd.read_csv(path + '/data/Old_gold/Disprop_analysis_female_with_HTs.csv')
    df_m = pd.read_csv(path + '/data/Old_gold/Disprop_analysis_male_with_HTs.csv')
    # anxiety disorders and symptoms
    # sleep disorders and disturbances (incl subtypes)
    # suicide and self-injurous behaviours nec
    # psychiatric disorders nec
    # hts = ['sleep disorders and disturbances', 'sleep disturbances (incl subtypes)']
    df_m1 = df_m[df_m['HT_level2'] == 'neurological disorders nec']
    df_f1 = df_f[df_f['HT_level2'] == 'neurological disorders nec']
    df_f1['Sex'] = 'F'
    df_m1['Sex'] = 'M'
    frames = [df_f1, df_m1]
    df = pd.concat(frames)
    df = df.drop_duplicates(subset=['DRUG', 'AE', 'IC025', 'Reports'], keep='first')
    df_drug = pd.read_csv(path + '/data/New/Drugs_Gender_Size.csv')
    df_fin = pd.DataFrame(columns=['DRUG', 'AE', 'Sex', 'Reports', 'Reports_Percent', 'IC025', 'Total_Reports'])
    for index, row in df.iterrows():
        df_sub_drug = df_drug[df_drug['DRUG'] == row['DRUG']]
        df_sub_drug = df_sub_drug[df_sub_drug['Sex'] == row['Sex']]
        ae_perc = (row['Reports'] / df_sub_drug['Reports'].values[0]) * 100
        ae_perc = round(ae_perc, 3)
        if row['DRUG'] == 'cinolazepam':
            print(row['DRUG'])
            print(type(row['DRUG']))
        df_fin = df_fin.append({'DRUG': str(row['DRUG']), 'AE': row['AE'], 'Sex': row['Sex'], 'Reports': row['Reports'],
                                'Reports_Percent': ae_perc, 'IC025': row['IC025'],
                                'Total_Reports': df_sub_drug['Reports'].values[0]},
                               ignore_index=True)
    # print(df_fin)
    df_fin['DRUG'] = df_fin["DRUG"].map(str)
    reports_perc(df_fin, 'psychiatric disorders nec')


def get_drug_totals(df):
    hglts = df['HT_level2'].tolist()
    hglts = list(dict.fromkeys(hglts))
    drugs = df['DRUG'].tolist()
    drugs = list(dict.fromkeys(drugs))
    df_g = pd.DataFrame(columns=['DRUG', 'HTLGT', 'IC025_sum', 'Reports_sum', 'Sex'])
    for item in drugs:
        df_x = df[df['Sex'] == 'M']
        df_x = df_x[df_x['DRUG'] == item]
        for element in hglts:
            df_x2 = df_x[df_x['HT_level2'] == element]
            if df_x2.empty:
                ic025_sum = 0
                reports = 0
            else:
                ic025_sum = df_x2['IC025'].sum()
                reports = df_x2['Reports'].sum()
            df_g = df_g.append(
                {'DRUG': item, 'HTLGT': element, 'IC025_sum': ic025_sum, 'Reports_sum': reports, 'Sex': 'M'},
                ignore_index=True)
    for item in drugs:
        df_x = df[df['Sex'] == 'F']
        df_x = df_x[df_x['DRUG'] == item]
        for element in hglts:
            df_x2 = df_x[df_x['HT_level2'] == element]
            if df_x2.empty:
                ic025_sum = 0
                reports = 0
            else:
                ic025_sum = df_x2['IC025'].sum()
                reports = df_x2['Reports'].sum()
            df_g = df_g.append({'DRUG': item, 'HTLGT': element, 'IC025_sum': ic025_sum, 'Reports_sum': reports,
                                'Sex': 'F'},
                               ignore_index=True)


"""
    fig = px.pie(df_1, values='IC025_sum', names='DRUG', title='Female', color='DRUG', hole=.2, color_discrete_map=colors_d)
    fig.update_traces(textposition='inside', textinfo='label+text+value+percent')
    fig.update_layout(
        font=dict(
            size=18
        )
    )
    #fig.show()
    df_1 = df_g[df_g['Sex'] == 'M']
    fig = px.pie(df_1, values='IC025_sum', names='DRUG', title='Male', hole=.2, color='DRUG', color_discrete_map=colors_d)
    fig.update_traces(textposition='inside', textinfo='label+text+value+percent')
    fig.update_layout(
        font=dict(
            size=18
        )
    )
    #fig.show()"""
"""
    df_99 = df_g.groupby(['DRUG'], as_index=False).sum()
    df_99 = df_99.sort_values(by='IC025_sum', ascending=False)
    drugsss = df_99['DRUG'].tolist()
    drugsss = list(dict.fromkeys(drugsss))
    for item in drugsss:
        dfX = df_g[df_g['DRUG'] == item]
        x = dfX['IC025_sum'].sum()
        if x < 200:
            df_g = df_g.drop(df_g[df_g.DRUG == item].index)
    df_99 = df_g.groupby(['DRUG'], as_index=False).sum()
    df_99 = df_99.sort_values(by='IC025_sum', ascending=False)
    print(df_99)
    drugs = df_99['DRUG'].tolist()
    drugs = list(dict.fromkeys(drugs))

    df_98 = df_g.groupby(['HTLGT'], as_index=False).sum()
    df_98 = df_98.sort_values(by='IC025_sum', ascending=True)
    hglts = df_98['HTLGT'].tolist()
    hglts = list(dict.fromkeys(hglts))

    #df_g = df_g.sort_values(by=['IC025_sum'], ascending=False, ignore_index=True)

    df_1 = df_g[df_g['Sex'] == 'F']
    new_radar_fig2(drugs, df_1, hglts, 'F')
    df_1 = df_g[df_g['Sex'] == 'M']
    new_radar_fig2(drugs, df_1, hglts, 'M')"""


def main():
    df_f = pd.read_csv(path + '\\data\\data\\Old_gold\\Disprop_analysis_female_with_HTs.csv')
    df_m = pd.read_csv(path + '\\data\\data\\Old_gold\\Disprop_analysis_male_with_HTs.csv')
    hts = ['nervous system disorders', 'psychiatric disorders']
    df_f = df_f[df_f['HT'].isin(hts)]
    df_m = df_m[df_m['HT'].isin(hts)]

    drugs = df_m['DRUG'].tolist() + df_f['DRUG'].tolist()
    drugs = list(dict.fromkeys(drugs))

    df_m['Sex'] = 'M'
    df_f['Sex'] = 'F'
    frames = [df_f, df_m]
    df = pd.concat(frames)
    df = df.drop_duplicates(subset=['DRUG', 'AE', 'IC025', 'Sex', 'Reports'], keep='first', ignore_index=True)
    df = df.groupby(by=['DRUG', 'Sex'], as_index=False).sum()
    fig = go.Figure()
    df_f1 = df[df['Sex'] == 'F']
    df_m1 = df[df['Sex'] == 'M']
    df_f1 = df_f1.sort_values(['IC025'], ignore_index=True, ascending=False)
    df_m1 = df_m1.sort_values(['IC025'], ignore_index=False, ascending=False)
    df_fx = df_f1.head(10)
    df_mx = df_m1.head(10)
    drugies = df_fx['DRUG'].tolist() + df_mx['DRUG'].tolist()
    drugies = list(dict.fromkeys(drugies))
    df_f1 = df_f1[df_f1['DRUG'].isin(drugies)]
    df_m1 = df_m1[df_m1['DRUG'].isin(drugies)]
    df_f1 = df_f1.sort_values(['DRUG'], ignore_index=True, ascending=False)
    df_m1 = df_m1.sort_values(['DRUG'], ignore_index=False, ascending=False)
    print(df_f1)
    print(df_m1)
    fig.add_trace(go.Scatterpolar(
        r=df_f1['IC025'],
        theta=df_f1['DRUG'],
        name='Female'
    ))

    fig.add_trace(go.Scatterpolar(
        r=df_m1['IC025'],
        theta=df_m1['DRUG'],
        name='Male'
    ))
    fig.update_layout(
        polar=dict(
            radialaxis=dict(
                visible=True,
                # range=[0, 5]
            )),
        showlegend=True
    )
    fig.show()
    # get_drug_totals(df)


def new_radar_fig2(drugies, df, hts, gender):
    fig = go.Figure()
    i = 0
    # print(drugies)
    for item in hts:
        df_mX = df[df['HTLGT'] == item]
        drug_list = df['DRUG'].tolist()
        drug_list = list(dict.fromkeys(drug_list))
        ic025s = []
        i = 0
        j = 0
        while i < len(drugies):
            if drugies[i] not in drug_list:
                ic025s.append(0)
                j = len(drug_list) + 5
            else:
                j = 0
            while j < len(drug_list):
                if drug_list[j] == drugies[i]:
                    df_sum = df_mX[df_mX['DRUG'] == drugies[i]]
                    ic025s.append(df_sum['IC025_sum'].sum())
                j += 1
            i += 1
        fig.add_trace(go.Barpolar(
            # r = df_X['IC025'].tolist(),
            # theta = df_X['HT_2'].tolist(),
            r=ic025s,
            theta=drugies,
            name=item,
            # legendrank=drugs_alpha.get(item),
            # marker=dict(pattern=dict(shape=symbols_d.get(item), fillmode='overlay', bgcolor=colors_d.get(item)))
        ))
        fig.update_traces(text=df_mX['IC025_sum'].tolist())
    fig.update_layout(
        polar=dict(
            radialaxis=dict(
                visible=True
            )),
        showlegend=True,
        font=dict(
            size=20,
        ),
        title_text='IC025 sum for all neuropsychiatric disorders subHT in ' + gender,
    )
    fig.update_layout(barmode='stack', xaxis={'categoryorder': 'total descending'})
    fig.update_polars(radialaxis=dict(visible=True, range=[0, 450]))
    fig.update_polars(angularaxis=dict(direction="clockwise", rotation=60),
                      radialaxis=dict(categoryorder='total descending'))
    fig.show()


def fig4_overview():
    df_f = pd.read_csv(path + '\\data\\data\\Old_gold\\Disprop_analysis_female_with_HTs.csv')
    df_m = pd.read_csv(path + '\\data\\data\\Old_gold\\Disprop_analysis_male_with_HTs.csv')
    df_m['Sex'] = 'M'
    df_f['Sex'] = 'F'
    # df_m = df_m[df_m['DRUG'] == 'nordazepam']
    # df_f = df_f[df_f['DRUG'] == 'nordazepam']
    hts = ['psychiatric disorders', 'nervous system disorders']
    df_m = df_m[df_m['HT'].isin(hts)]
    df_f = df_f[df_f['HT'].isin(hts)]
    frames = [df_f, df_m]
    df = pd.concat(frames)
    # df = df.groupby(['AE', 'Sex', 'DRUG'], as_index=False).sum()
    df = df.drop_duplicates(subset=['DRUG', 'AE', 'IC025'], keep='first')
    df = df.sort_values(['IC025'], ascending=False)
    df2 = df.head(23)
    df_aes = df2['AE'].tolist()
    df2 = df[df['AE'].isin(df_aes)]
    df2 = df2.drop_duplicates(subset=['DRUG', 'AE', 'IC025'], keep='first')
    df2 = df2.sort_values(['IC025'], ascending=False)
    fig1 = px.bar(df2, x="AE", y="IC025", color='Sex', barmode='group', color_discrete_map=colors_g)
    # fig1.update_xaxes(categoryorder='max descending')
    fig1.update_yaxes(categoryorder='total descending')
    fig1.update_layout(
        xaxis_title="Adverse Events (AEs)",
        yaxis_title="IC025",
        legend_title="Sex",
        title='Nordazepam',
        font=dict(
            size=18,
        )
    )
    fig1.show()


def figure_1():
    df_f = pd.read_csv(
        'C:\\Users\\TARIQOPLATA\\PycharmProjects\\FAERS_BZD-Gender\\Disprop_G\\Disprop_analysis_female_with_HTs.csv')
    df_m = pd.read_csv(
        'C:\\Users\\TARIQOPLATA\\PycharmProjects\\FAERS_BZD-Gender\\Disprop_G\\Disprop_analysis_male_with_HTs.csv')
    ht = ['psychiatric disorders']
    df_m1 = df_m[df_m['HT'].isin(ht)]
    df_f1 = df_f[df_f['HT'].isin(ht)]
    df_m1 = df_m1.drop_duplicates(subset=['DRUG', 'AE', 'IC025', 'Reports', 'HT'], keep='first', ignore_index=True)
    df_f1 = df_f1.drop_duplicates(subset=['DRUG', 'AE', 'IC025', 'Reports', 'HT'], keep='first', ignore_index=True)
    ht = ht[0]
    # ht = 'injury;poisoning and procedural complications'
    ht_level2 = df_m1['HT_level2'].tolist() + df_f1['HT_level2'].tolist()
    ht_level2 = list(dict.fromkeys(ht_level2))
    drugs = df_m1['DRUG'].tolist() + df_f1['DRUG'].tolist()
    drugs = list(dict.fromkeys(drugs))
    drugs = sorted(drugs)
    df_males = pd.DataFrame(columns=['DRUG', 'HT_2', 'IC025_sum', 'Reports_sum', 'Gender'])
    df_g = pd.DataFrame(columns=['HT_2', 'IC025_sum', 'Reports_sum', 'Gender'])
    for item in ht_level2:
        df_m2 = df_m1[df_m1['HT_level2'] == item]
        for drug in drugs:
            df_m3 = df_m2[df_m2['DRUG'] == drug]
            ic025_sum = df_m3['IC025'].sum()
            reports = df_m3['Reports'].sum()
            df_males = df_males.append(
                {'DRUG': drug, 'HT_2': item, 'IC025_sum': ic025_sum, 'Reports_sum': reports, 'Gender': 'M'},
                ignore_index=True)
    for item in ht_level2:
        df_x = df_males[df_males['HT_2'] == item]
        ic025_sum = df_x['IC025_sum'].sum()
        reports = df_x['Reports_sum'].sum()
        df_g = df_g.append({'HT_2': item, 'IC025_sum': ic025_sum, 'Reports_sum': reports, 'Gender': 'M'},
                           ignore_index=True)
    for item in ht_level2:
        df_f2 = df_f1[df_f1['HT_level2'] == item]
        for drug in drugs:
            df_f3 = df_f2[df_f2['DRUG'] == drug]
            ic025_sum = df_f3['IC025'].sum()
            reports = df_f3['Reports'].sum()
            df_males = df_males.append(
                {'DRUG': drug, 'HT_2': item, 'IC025_sum': ic025_sum, 'Reports_sum': reports, 'Gender': 'F'},
                ignore_index=True)
    for item in ht_level2:
        df_x = df_males[df_males['Gender'] == 'F']
        df_x = df_x[df_x['HT_2'] == item]
        ic025_sum = df_x['IC025_sum'].sum()
        reports = df_x['Reports_sum'].sum()
        df_g = df_g.append({'HT_2': item, 'IC025_sum': ic025_sum, 'Reports_sum': reports, 'Gender': 'F'},
                           ignore_index=True)
    df_males = df_males.drop_duplicates(['DRUG', 'HT_2', 'IC025_sum', 'Gender'], ignore_index=True)
    df_bM = df_males.groupby(['HT_2', 'Gender'], as_index=False).sum()
    df = df_bM.sort_values(by=['Reports_sum'], ascending=True, ignore_index=True)
    for item in ht_level2:
        dfX = df_males[df_males['HT_2'] == item]
        x = dfX['IC025_sum'].sum()
        # 150 FOR PSYCH; NERV; INJURY
        if x < 150:
            df_males = df_males.drop(df_males[df_males.HT_2 == item].index)
    df_99 = df_males.groupby(['HT_2'], as_index=False).sum()
    df_99 = df_99.sort_values(by='IC025_sum', ascending=False)
    ht_l2_new = df_99['HT_2'].tolist()

    df_98 = df_males.groupby(['DRUG'], as_index=False).sum()
    df_98 = df_98.sort_values(by='IC025_sum', ascending=True)
    drugies = df_98['DRUG'].tolist()
    print(df_98)

    df_1 = df_males[df_males['Gender'] == 'F']
    create_radar(drugies, df_1, ht_l2_new, 'F', ht)
    df_1 = df_males[df_males['Gender'] == 'M']
    create_radar(drugies, df_1, ht_l2_new, 'M', ht)


def create_radar(drugies, df, ht_level2, gender, ht):
    # FILTER
    # df = df.drop(df[df.score < 50].index)
    # df = df.drop(df[df.IC025 == 0].index)
    # df = df.sort_values(by=['HT_2', 'IC025_sum'], ascending=True)
    # print(df)
    fig = go.Figure()
    i = 0
    for item in drugies:
        df_mX = df[df['DRUG'] == item]
        ht_list = df['HT_2'].tolist()
        ht_list = list(dict.fromkeys(ht_list))
        ic025s = []
        i = 0
        j = 0
        while i < len(ht_level2):
            if ht_level2[i] not in ht_list:
                ic025s.append(0)
                j = len(ht_list) + 5
            else:
                j = 0
            while j < len(ht_list):
                if ht_list[j] == ht_level2[i]:
                    df_sum = df_mX[df_mX['HT_2'] == ht_level2[i]]
                    ic025s.append(df_sum['IC025_sum'].sum())
                j += 1
            i += 1
        print(item)
        print(colors_d.get(item))
        fig.add_trace(go.Barpolar(
            # r = df_X['IC025'].tolist(),
            # theta = df_X['HT_2'].tolist(),
            r=ic025s,
            theta=ht_level2,
            name=item,
            legendrank=drugs_alpha.get(item),
            marker=dict(pattern=dict(shape=symbols_d.get(item), fillmode='overlay', bgcolor=colors_d.get(item)),
                        color=colors_d.get(item))
        ))
        fig.update_traces(text=df_mX['IC025_sum'].tolist())
    fig.update_layout(
        polar=dict(
            radialaxis=dict(
                visible=True
            )),
        showlegend=True,
        font=dict(
            size=18
        ),
        title_text='IC025 sum for all ' + ht + ' subHT in ' + gender,
    )
    fig.update_layout(barmode='stack', xaxis={'categoryorder': 'total descending'})
    fig.update_polars(radialaxis=dict(visible=True, range=[0, 400]))
    fig.update_polars(angularaxis=dict(direction="clockwise", rotation=80),
                      radialaxis=dict(categoryorder='total ascending'))
    # ( "trace" | "category ascending" | "category descending" | "array" | "total ascending" | "total descending" | "min ascending" | "min descending" | "max ascending" | "max descending" | "sum ascending" | "sum descending" | "mean ascending" | "mean descending" | "median ascending" | "median descending" )
    # fig.write_html('Figure_1_female_'+ht+'.html')
    fig.show()


def figure_2():
    df_f = pd.read_csv(
        'C:\\Users\\TARIQOPLATA\\PycharmProjects\\FAERS_BZD-Gender\\Disprop_G\\Disprop_analysis_female_with_HTs.csv')
    df_m = pd.read_csv(
        'C:\\Users\\TARIQOPLATA\\PycharmProjects\\FAERS_BZD-Gender\\Disprop_G\\Disprop_analysis_male_with_HTs.csv')
    ht2 = 'neurological disorders nec'
    df_m1 = df_m[df_m['HT_level2'] == ht2]
    df_f1 = df_f[df_f['HT_level2'] == ht2]
    drugs = df_m1['DRUG'].tolist() + df_f1['DRUG'].tolist()
    drugs = list(dict.fromkeys(drugs))
    drugs = sorted(drugs)
    aes_ = df_m1['AE'].tolist() + df_f1['AE'].tolist()
    aes_ = list(dict.fromkeys(aes_))
    aes_ = sorted(aes_)
    df_m1['Gender'] = 'M'
    df_f1['Gender'] = 'F'
    frames = [df_f1, df_m1]
    df = pd.concat(frames)
    df_g = pd.DataFrame(columns=['AE', 'IC025_sum', 'Reports_sum', 'Gender'])
    for item in aes_:
        df_x = df[df['Gender'] == 'M']
        df_x = df_x[df_x['AE'] == item]
        if df_x.empty:
            ic025_sum = 0
            reports = 0
        else:
            ic025_sum = df_x['IC025'].sum()
            reports = df_x['Reports'].sum()
        df_g = df_g.append({'AE': item, 'IC025_sum': ic025_sum, 'Reports_sum': reports, 'Gender': 'M'},
                           ignore_index=True)
    for item in aes_:
        df_x = df[df['Gender'] == 'F']
        df_x = df_x[df_x['AE'] == item]
        if df_x.empty:
            ic025_sum = 0
            reports = 0
        else:
            ic025_sum = df_x['IC025'].sum()
            reports = df_x['Reports'].sum()
        df_g = df_g.append({'AE': item, 'IC025_sum': ic025_sum, 'Reports_sum': reports, 'Gender': 'F'},
                           ignore_index=True)
    df_aes = df['AE'].tolist()
    df_aes = list(dict.fromkeys(df_aes))
    dfx = df.sort_values(by=['Reports'], ascending=True, ignore_index=True)
    print(dfx)
    figBAR = px.bar(dfx, x="Reports", y="DRUG", color='Gender', barmode='group', color_discrete_map=colors_g,
                    title=ht2, orientation='h')
    # category_orders={'DRUG': dfx["DRUG"]}
    figBAR.update_layout(
        xaxis_title="total reports",
        yaxis_title="drugs",
        legend_title="Sex",
        font=dict(
            size=18,
        )
    )
    df_99 = df.groupby(['AE'], as_index=False).sum()
    df_99 = df_99.sort_values(by='IC025', ascending=False)
    aes_ = df_99['AE'].tolist()
    aes_ = list(dict.fromkeys(aes_))
    for item in aes_:
        dfX = df[df['AE'] == item]
        x = dfX['IC025'].sum()
        if x < 30:
            df = df.drop(df[df.AE == item].index)
    df_99 = df.groupby(['AE'], as_index=False).sum()
    df_99 = df_99.sort_values(by='IC025', ascending=False)
    aes_ = df_99['AE'].tolist()
    aes_ = list(dict.fromkeys(aes_))

    df_98 = df.groupby(['DRUG'], as_index=False).sum()
    df_98 = df_98.sort_values(by='IC025', ascending=True)

    drugies = df_98['DRUG'].tolist()
    drugies = list(dict.fromkeys(drugies))
    print(aes_)
    df_1 = df[df['Gender'] == 'F']
    new_radar_fig2(drugies, df_1, aes_, 'F', ht2)
    df_1 = df[df['Gender'] == 'M']
    new_radar_fig2(drugies, df_1, aes_, 'M', ht2)
    # bar_plot(df, 'Both', ht2)


def new_radar_fig2(drugies, df, aes, gender, group):
    fig = go.Figure()
    i = 0
    # print(drugies)
    for item in drugies:
        df_mX = df[df['DRUG'] == item]
        ht_list = df['AE'].tolist()
        ht_list = list(dict.fromkeys(ht_list))
        ic025s = []
        i = 0
        j = 0
        while i < len(aes):
            if aes[i] not in ht_list:
                ic025s.append(0)
                j = len(ht_list) + 5
            else:
                j = 0
            while j < len(ht_list):
                if ht_list[j] == aes[i]:
                    df_sum = df_mX[df_mX['AE'] == aes[i]]
                    ic025s.append(df_sum['IC025'].sum())
                j += 1
            i += 1
        fig.add_trace(go.Barpolar(
            # r = df_X['IC025'].tolist(),
            # theta = df_X['HT_2'].tolist(),
            r=ic025s,
            theta=aes,
            name=item,
            legendrank=drugs_alpha.get(item),
            marker=dict(pattern=dict(shape=symbols_d.get(item), fillmode='overlay', bgcolor=colors_d.get(item)),
                        color=colors_d.get(item))
        ))
        fig.update_traces(text=df_mX['IC025'].tolist())
    fig.update_layout(
        polar=dict(
            radialaxis=dict(
                visible=True
            )),
        showlegend=True,
        #marker=dict(size=30),
        font=dict(
            size=20,
        ),
        title_text='IC025 sum for all ' + group + ' subHT in ' + gender,
    )
    #fig.update_layout(legend=dict(font=dict(size=20), marker=dict(size=30)))
    #fig.update_traces(marker_colorbar_tickfont_size=2)
    fig.update_layout(barmode='stack', xaxis={'categoryorder': 'total descending'},
                      #legend={'itemsizing': 'constant'}
                      )
    # fig.update_layout(barmode='stack', xaxis={'categoryorder': 'total descending'})
    fig.update_polars(radialaxis=dict(visible=True, range=[0, 55]))
    fig.update_polars(angularaxis=dict(direction="clockwise", rotation=80),
                      radialaxis=dict(categoryorder='total ascending'))
    fig.show()


def create_radar_fig2(drugies, df, ht_level2, gender, group):
    # FILTER
    # df = df.drop(df[df.score < 50].index)
    # df = df.drop(df[df.IC025 == 0].index)
    df = df.sort_values(by=['AE', 'IC025'], ascending=True)
    fig = go.Figure()
    i = 0
    for item in drugies:
        df_mX = df[df['DRUG'] == item]
        if df_mX.empty:
            continue
        # Scatterpolar
        if i == 1 or i == 3 or i == 5:
            fig.add_trace(go.Barpolar(
                r=df_mX['IC025'].tolist(),
                theta=ht_level2,
                name=item,
                # marker_symbol=symbols[i],
                # marker_symbol=symbols.get(item),
                # mode='markers+lines',
                # connectgaps=True,
                # cmin=0, cmax=1, autocolorscale=False,
                marker=dict(  # cmin=0, cmax=1, #autocolorscale=True, #color=colors_d.get(item),
                    # line_color=colors_d.get(item), pattern_fillmode="replace",
                    pattern=dict(shape=symbols_d.get(item), fillmode='overlay', bgcolor=colors_d.get(item),
                                 )),  # size=2, solidity=0.5
            ))
        # else:
        #    fig.add_trace(go.Barpolar(
        #        r=df_mX['IC025'].tolist(),
        #        theta=ht_level2,
        #        name=item,
        # marker_symbol=symbols[i],
        # marker_symbol=symbols.get(item),
        # mode='markers+lines',
        # connectgaps=True,
        # cmin=0, cmax=1, autocolorscale=False,
        #        marker=dict(cmin=0, cmax=1, autocolorscale=True, color=colors_d.get(item),
        #                    line_color=colors_d.get(item))
        #    ))
        fig.update_traces(text=df_mX['IC025'].tolist())
        i += 1
        if i > 5:
            i = 0
        """
        fig.add_trace(go.Barpolar(
            r=df_mX['IC025'].tolist(),
            theta=ht_level2,
            name=item,
            #fig.update_traces(marker_pattern=dict(...), selector=dict(type='barpolar'))
            #fig.update_traces(marker_pattern_fillmode='overlay', marker_pattern_shape=<VALUE>
            #( "" | "/" | "\" | "x" | "-" | "|" | "+" | "." )
            # selector=dict(type='barpolar'))
            marker=dict(cmin=0, cmax=1, autocolorscale=False, color=colors_d.get(item)),
        ))
        fig.update_traces(marker_pattern_fillmode='overlay', marker_pattern_shape=patterns[i], selector=dict(type='barpolar'))
        i += 1
        if i > 5:
            i = 0"""
    fig.update_layout(
        polar=dict(
            radialaxis=dict(
                visible=True
            )),
        showlegend=True,
        title_text='IC025 sum for all AEs in ' + group + ' subHT in ' + gender
    )
    fig.update_layout(barmode='stack', xaxis={'categoryorder': 'total descending'})
    # fig.update_polars(radialaxis=dict(visible=True, range=[-20, 70]))
    fig.update_polars(angularaxis=dict(direction="clockwise", rotation=80),
                      radialaxis=dict(categoryorder='total ascending'))
    # ( "trace" | "category ascending" | "category descending" | "array" | "total ascending" | "total descending" | "min ascending" | "min descending" | "max ascending" | "max descending" | "sum ascending" | "sum descending" | "mean ascending" | "mean descending" | "median ascending" | "median descending" )
    fig.write_html('Fig_' + group + '_' + gender + '.html')
    fig.show()


if __name__ == '__main__':
    figure_2()
