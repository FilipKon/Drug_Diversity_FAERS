import pandas as pd


path = 'C:\\Users\\TARIQOPLATA\\PycharmProjects\\FAERS_final'
#path = '\Users\'


def find_HT(df_fin):
    df_meddra = pd.read_csv('C:\\Users\\TARIQOPLATA\\PycharmProjects\\FAERS_final\\data\\mdhier_last.asc')
    df_meddra = df_meddra.drop('7', axis=1)
    df_meddra = df_meddra.drop('6', axis=1)
    df_meddra = df_meddra.drop('5', axis=1)
    df_meddra = df_meddra.drop('4', axis=1)
    df_meddra = df_meddra.drop('3', axis=1)
    df_meddra = df_meddra.drop('2', axis=1)
    df_meddra = df_meddra.drop('1', axis=1)
    df_meddra = df_meddra.drop('id1', axis=1)
    df_meddra = df_meddra.drop('id2', axis=1)
    df_meddra = df_meddra.drop('id3', axis=1)
    df_meddra = df_meddra.drop('Y', axis=1)
    df_meddra = df_meddra.drop('Z', axis=1)
    found = []
    not_found = []
    aes = df_fin['AE'].tolist()
    aes = list(map(lambda x: x.lower(), aes))
    df_meddra['id4'] = df_meddra['id4'].str.lower()
    terms = df_meddra['id4'].tolist()
    term_ht = df_meddra['term3'].tolist()
    term_ht2 = df_meddra['term2'].tolist()
    term_ht3 = df_meddra['term1'].tolist()
    i = 0
    aes_ht = []
    for item in aes:
        j = 0
        item = item.lower()
        while j < len(terms):
            if str(terms[j]) == str(item):
                found.append(item)
                aes_ht.append([item.lower(), term_ht[j].lower(), term_ht2[j].lower(), term_ht3[j].lower()])
                i = 1
            j += 1
        if i == 0:
            not_found.append(item)
        i = 0
    not_found = list(dict.fromkeys(not_found))
    print(['NOT FOUND', len(not_found)])
    print(not_found)
    df_m = pd.DataFrame(aes_ht, columns=['AE', 'HT', 'HT_l2', 'HT_l3'])
    df = pd.merge(df_fin, df_m, on="AE")
    df.drop_duplicates(inplace=True, keep='first')
    return df


def main():
    df_m = pd.read_csv(path + '\\data\\New\\Disproportionate_analysis_male_NEWNEW.csv')
    df_m = df_m.drop(df_m[df_m.IC025 < 0].index)
    df_m = df_m.drop(df_m[df_m.Reports < 5].index)
    df_m = df_m.drop(df_m[df_m.PRR < 2].index)
    df = find_HT(df_m)
    df_m.to_csv('C:\\Users\\TARIQOPLATA\\PycharmProjects\\FAERS_final\\data\\New\\Male_data_Final_HTs_Filtered.csv')


if __name__ == '__main__':
    main()
