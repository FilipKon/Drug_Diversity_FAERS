import pandas as pd
import numpy as np
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
import plotly.express as px
import sys
from scipy.cluster.hierarchy import dendrogram, linkage
from sklearn.cluster import AgglomerativeClustering
import seaborn as sns
import plotly.graph_objects as go
import plotly.figure_factory as ff
pd.set_option('display.max_rows', 1000)
#pd.set_option('display.max_columns', 1000)
import matplotlib.pyplot as plt

path = 'C:\\Users\\TARIQOPLATA\\PycharmProjects\\FAERS_final\\'
# path = '\Users\'


def thomas_results():
    df_combo = pd.read_csv('C:\\Users\\TARIQOPLATA\\PycharmProjects\\FAERS_final\\data\\dist_mtx_combo.csv')
    #df_combo = df_combo.set_index('Unnamed: 0')
    #sns.clustermap(df_combo, metric="correlation", method="single")
    #plt.show()
    labels = df_combo['DRUG'].tolist()
    dfs = df_combo.loc[:, df_combo.columns != 'DRUG']
    cluster(dfs, labels)
    #cluster(dfs, labels)
    fig = ff.create_dendrogram(dfs, labels=labels)
    fig.update_layout(width=1400, height=1050)
    fig.update_layout(
        font=dict(
            size=18
        )
    )
    fig.write_html('Thomas_Results.html')
    fig.show()


def cluster(df, labels):
    g = sns.clustermap(df, cmap="vlag", yticklabels=1, xticklabels=1)
    g.ax_heatmap.set_xticklabels(labels, rotation=90)
    g.ax_heatmap.set_yticklabels(labels, rotation=0)
    #plt.setp(cg.ax_heatmap.yaxis.get_majorticklabels(), rotation=0)
    linkage_data = linkage(df, method='ward', metric='euclidean')
    dendrogram(linkage_data, labels=labels)
    ax = plt.gca()
    ax.tick_params(axis='x', which='major', labelsize=12)
    ax.tick_params(axis='y', which='major', labelsize=8)
    #plt.savefig('clustering_figure_thomas.png')
    plt.show()
    #dn = dendrogram(df, labels=labels)
    #plt.show()


def pca(data, labels, title):
    pca = PCA(n_components=3)
    X = pca.fit_transform(data)
    df = pd.DataFrame(X)
    df['labels'] = labels
    df.columns = ['PC1', 'PC2', 'PC3', 'labels']
    try:
        fig = px.scatter_3d(df, x='PC1', y='PC2', z='PC3', color='labels', title=title)
    except ValueError:
        fig = px.scatter_3d(df, x='PC1', y='PC2', z='PC3', color='labels', title=title)
    fig.show()
    return df


def pca_proc(df):
    #df = pd.read_csv('C:\\Users\\TARIQOPLATA\\PycharmProjects\\FAERS_BZD-Gender\\Female_for_pca.csv')
    labels = []
    dfs = []
    labels = df['DRUG'].tolist()
    dfs = df.loc[:, df.columns != 'DRUG']
    #dfs.append(df[1:])
    df2 = pca(dfs, labels, 'Male FAERS pca')
    labels = df2['labels'].tolist()
    dfs = df2.loc[:, df2.columns != 'labels']
    fig = ff.create_dendrogram(dfs, labels=labels)
    fig.update_layout(width=1400, height=1050, title='Male FAERS PCA')
    fig.update_layout(
        font=dict(
            size=18
        )
    )
    fig.write_html('Male_FAERS_PCA.html')
    fig.show()
    

def main():
    df_f = pd.read_csv(path + '\\data\\Female_for_pca.csv')
    df_m = pd.read_csv(path + '\\data\\Male_for_pca.csv')
    pca_proc(df_m)


if __name__ == '__main__':
    thomas_results()
