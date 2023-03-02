import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import HGLTs
path = 'C:\\Users\\TARIQOPLATA\\PycharmProjects\\FAERS_final\\data\\data\\Old_gold\\'
# path = '\Users\'

"""
terms = ['activation syndrome', 'agitation', 'nervousness', 'terminal agitation', 'limited symptom panic attack',
         'panic attack', 'panic reaction', 'hyperarousal', 'psychomotor hyperactivity', 'restlessness',
         'automatism', 'head banging', 'stereotypy', 'disorganised speech', 'logorrhoea', 'repetitive speech',
         'speech disorder', 'verbigeration', 'dysarthria', 'confusional state', 'disorientation', 'delirium',
         'post-injection delirium sedation syndrome', 'impulse-control disorder', 'impulsive behaviour',
         'poriomania', 'dreamy state', 'aggression', 'antisocial behaviour', 'asocial behaviour', 'aversion',
         'belligerence', 'defiant behaviour', 'disinhibition', 'disturbance in social behaviour', 'paranoia',
         'homicidal ideation', 'hostility', 'impatience', 'judgement impaired', 'personality change',
         'self-destructive behaviour', 'stubbornness', 'suspiciousness', 'violence-related symptom', 'insomnia',
         'middle insomnia', 'hypnagogic hallucination', 'hypnopompic hallucination', 'abnormal dreams',
         'abnormal sleep-related event', 'confusional arousal', 'parasomnia', 'sleep sex', 'sleep talking',
         'sleep terror', 'somnambulism', 'completed suicide', 'intentional self-injury', 'self-injurious ideation',
         'suicidal behaviour', 'suicidal ideation', 'suicide attempt', 'suicide threat', 'suspected suicide',
         'suspected suicide attempt', 'aberrant motor behaviour', 'abnormal behaviour', 'behaviour disorder',
         'regressive behaviour', 'scatolia', 'sexually inappropriate behaviour', 'bizarre personal appearance',
         'hyperventilation', 'hypervigilance', 'psychiatric decompensation', 'psychiatric symptom', 'trance',
         'change in sustained attention', 'cognitive disorder', 'distractibility', 'disturbance in attention',
         'psychomotor disadaptation syndrome', 'neuropsychiatric symptoms', 'neuropsychiatric syndrome',
         'organic brain syndrome', 'altered state of consciousness', 'mental status changes', 'amnesia',
         'anterograde amnesia', 'memory impairment', 'paramnesia', 'retrograde amnesia',
         'transient global amnesia', 'seizure', 'epilepsy', 'tonic clonic movements', 'seizure like phenomena',
         'status epilepticus', 'seizure cluster', 'convulsive threshold lowered', 'convulsions local',
         'clonic convulsion', 'change in seizure presentation', 'atonic seizures', 'simple partial seizures',
         'parietal lobe epilepsy']"""
terms = ['agitation', 'restlessness', 'logorrhoea']
#'Generalised onset non-motor seizure', 'Juvenile absence epilepsy', 'Petit mal epilepsy', 'Generalised tonic-clonic seizure', 'Automatism epileptic'
#'Epileptic psychosis', 'Focal dyscognitive seizures


def main():
    df_f = pd.read_csv(path + 'Disprop_analysis_female_with_HTs.csv')
    df_m = pd.read_csv(path + 'Disprop_analysis_male_with_HTs.csv')
    df_m1 = df_m[df_m['AE'].isin(terms)]
    df_f1 = df_f[df_f['AE'].isin(terms)]
    df_m1 = df_m1.drop_duplicates(['DRUG', 'AE', 'IC025'])
    df_f1 = df_f1.drop_duplicates(['DRUG', 'AE', 'IC025'])
    df_m1 = df_m1.sort_values(by=['IC025'], ascending=True)
    df_m1['IC025'] = df_m1['IC025'].apply(lambda x: round(x, 2))
    df_f1['IC025'] = df_f1['IC025'].apply(lambda x: round(x, 2))
    df_m1 = df_m1.drop(df_m1[df_m1.IC025 < 2].index)
    df_f1 = df_f1.drop(df_f1[df_f1.IC025 < 2].index)

    df_f1 = df_f1.sort_values(by=['AE'], ascending=False)
    aes = df_f1['AE'].tolist()
    aes = list(dict.fromkeys(aes))
    df_m1 = df_m1.sort_values(by=['DRUG'], ascending=True)
    df_f1 = df_f1.sort_values(by=['DRUG'], ascending=True)
    drugs = df_f1['DRUG'].tolist()
    drugs = list(dict.fromkeys(drugs))
    fig1 = go.Figure(data=go.Heatmap(z=df_m1['IC025'].tolist(), x=df_m1['DRUG'].tolist(), y=df_m1['AE'].tolist(),
                                     colorscale='Bluyl', colorbar={"title": 'IC025'}))
    fig1.update_layout(
        title_text="Male reports with their IC025 for the chose paradoxical reactions",
        yaxis_nticks=len(df_m1['AE'].tolist()),
        xaxis_nticks=len(df_m1['DRUG'].tolist())
    )
    #                                     category_order={'DRUG':sorted(df_m1.DRUG.unique()),
    #                                                 'AE':sorted(df_m1.AE.unique())}
    fig1.update_xaxes(categoryorder='category ascending')
    fig1.update_yaxes(categoryorder='category descending')
    fig1.update_traces(text=df_m1['IC025'], texttemplate="%{text}")
    fig1.show()


if __name__ == '__main__':
    main()
