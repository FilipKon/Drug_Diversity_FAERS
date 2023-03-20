import pandas as pd
import numpy as np
import warnings
warnings.filterwarnings("ignore", category=FutureWarning)


#IDX,DRUG,ADVERSE_EVENT,A,B,C,D,N

def get_bpcn(a, b, c, d):
    bpcn = np.log2(a)*(a+b+c+d)*(a+c)*(a+b)
    return bpcn


def get_ic(a, b, c, d):
    aexp = ((a + b) * (a + c)) / (a + b + c + d)
    ic = np.log2(((a + 0.5) / (aexp + 0.5)))
    IC025 = ic - 3.3 * np.power((a + 0.5), (-1/2)) - 2 * np.power((a + 0.5), (-3/2))
    #print(['IC', ic, IC025])
    return ic, IC025


def get_prr(a, b, c, d):
    prr = (a/(a + c)) / (b/(b + d)) # from mdpi paper
    #prr = (a / (a+b)) / (c/(c+d))
    #print(['PRR', prr, prr2])
    return prr


def get_ror(a, b, c, d):
    ROR = (a*d) / (b*c)
    #print(['ROR', ROR])
    return ROR
  
def main():
    df_m = pd.read_csv('C:\\Users\\TARIQOPLATA\\PycharmProjects\\FAERS_BZD-Gender\\Disprop_G\\contingency_table_NEWESTOKE_M.csv')
    df_f = pd.read_csv('C:\\Users\\TARIQOPLATA\\PycharmProjects\\FAERS_BZD-Gender\\Disprop_G\\contingency_table_NEWESTOKE_F.csv')
    dis_m = pd.DataFrame(columns=['DRUG', 'AE', 'IC', 'IC025', 'PRR', 'ROR', 'Reports'])
    dis_f = pd.DataFrame(columns=['DRUG', 'AE', 'IC', 'IC025', 'PRR', 'ROR', 'Reports'])
    i = 0
    for index, row in df_m.iterrows():
        if row['A'] == 0:
            continue
        if row['B'] == 0:
            continue
        print([row['A'], row['B'], row['C'], row['D'], row['DRUG'], row['AE']])
        prr = get_prr(row['A'], row['B'], row['C'], row['D'])
        ic, ic025 = get_ic(row['A'], row['B'], row['C'], row['D'])
        ror = get_ror(row['A'], row['B'], row['C'], row['D'])
        #bpcn = get_bpcn(row['A'], row['B'], row['C'], row['D'])
        dis_m = dis_m.append({'DRUG': row['DRUG'], 'AE': row['AE'], 'IC': ic, 'IC025': ic025,
                              'PRR': prr, 'ROR': ror, 'Reports': row['A']}, ignore_index=True)
        i += 1
        #print(i)
        if i == 1000:
            print(dis_m)
    print('MALE DONE')
    dis_m.to_csv('Disproportionate_analysis_male_NEWNEW.csv')
    for index, row in df_f.iterrows():
        if row['A'] == 0:
            continue
        if row['B'] == 0:
            continue
        prr = get_prr(row['A'], row['B'], row['C'], row['D'])
        ic, ic025 = get_ic(row['A'], row['B'], row['C'], row['D'])
        ror = get_ror(row['A'], row['B'], row['C'], row['D'])
        #bpcn = get_bpcn(row['A'], row['B'], row['C'], row['D'])
        dis_f = dis_f.append({'DRUG': row['DRUG'], 'AE': row['AE'], 'IC': ic, 'IC025': ic025,
                              'PRR': prr, 'ROR': ror, 'Reports': row['A']}, ignore_index=True)
        print(dis_f)
        print('FEMALE')
    dis_f.to_csv('Disproportionate_analysis_female_NEWNEW.csv')


if __name__ == '__main__':
    main()
