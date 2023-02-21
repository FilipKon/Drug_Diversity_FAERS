from rdkit import Chem
from rdkit.Chem import AllChem
from rdkit import DataStructs
from rdkit.Chem import RDKFingerprint, SDMolSupplier
from PyBioMed.PyMolecule import connectivity, topology
from PyBioMed.PyMolecule.cats2d import CATS2D
from PyBioMed.PyMolecule.ghosecrippen import GhoseCrippenFingerprint
from PyBioMed.PyMolecule import moe
from PyBioMed.PyInteraction import PyInteraction
#from PyBioMed.PyMolecule.fingerprint import CalculateFP2Fingerprint
import pybel
import pandas as pd
import plotly.figure_factory as ff
import numpy as np

from sklearn.decomposition import PCA
import plotly.graph_objs as go
import plotly.express as px
import os


def get_sdfs():
    directory = 'C:\\Users\\TARIQOPLATA\\Documents\\Filip\\SDFs\\BZD_sdfs\\'
    All = ''
    fullfile = open('All_sdfs.sdf', 'w')
    for file in os.listdir(directory):
        filename = os.fsdecode(file)
        full = os.path.join(directory, filename)
        txt = open(full, 'r')
        txt = txt.readlines()
        print(txt)
        for item in txt:
            All = All + item
    fullfile.write(All)
    fullfile.close()
    fullfile = open('All_sdfs.sdf', 'r')
    return fullfile


def get_names():
    file = open('C:\\Users\\TARIQOPLATA\\PycharmProjects\\FAERSA\\backend\\Mol_Sim\\All_sdfs.sdf', 'r')
    file = file.readlines()
    i = 0
    names = []
    for line in file:
        if i == 0:
            mol = line
            mol = mol[:-1]
            names.append(mol)
            i += 1
        if '$$$$' in line:
            i = 0
    print(names)
    return names


def biomed():
    SDFFile = 'C:\\Users\\TARIQOPLATA\\PycharmProjects\\FAERSA\\backend\\Mol_Sim\\All_sdfs.sdf'
    #SDFFile = get_sdfs()
    suppl = SDMolSupplier(SDFFile)
    mols = [mol for mol in suppl if mol is not None]
    print(mols)
    i = 0
    names = get_names()
    for item in mols:
        #alldes = item.GetAllDescriptor()
        #print(alldes)
        #print(len(alldes))
        molecular_descriptor = connectivity.GetConnectivity(item)
        #print(molecular_descriptor)
        molecular_descriptor2 = topology.GetTopology(item)
        #print(molecular_descriptor2)
        cats = CATS2D(item, PathLength=10, scale=3)
        #print(cats)
        ghoseFP = GhoseCrippenFingerprint(item)
        #print(ghoseFP)
        mol_des = moe.GetMOE(item)
        mol_mol_interaction1 = PyInteraction.CalculateInteraction1(mol_des, mol_des)
        #print(mol_mol_interaction1)
        mol_mol_interaction2 = PyInteraction.CalculateInteraction2(mol_des, mol_des)
        #print(mol_mol_interaction2)
        mol_mol_interaction3 = PyInteraction.CalculateInteraction3(mol_des, mol_des)
        #print(mol_mol_interaction3)
        #name = {'Name': names[i]}
        #all_descriptors = molecular_descriptor | molecular_descriptor2 | cats | ghoseFP | mol_mol_interaction1 | mol_mol_interaction2 | mol_mol_interaction3
        all_descriptors = molecular_descriptor | molecular_descriptor2 | cats | ghoseFP | mol_des
        print(all_descriptors)
        if i == 0:
            df = pd.DataFrame(all_descriptors, index=[0])
        else:
            df = df.append(all_descriptors, ignore_index=True)
        i += 1
    print(df)
    #df = df.drop('Chi0', axis=1)
    data = df.to_numpy()
    print(data)
    #data.astype(float)
    pca(data, names)
        #molecular_descriptor = item.GetEstate()
        #print(molecular_descriptor)
        #molecular_descriptor = item.GetCharge()
        #print(molecular_descriptor)
        #molecular_descriptor = item.GetKappa()
        #print(molecular_descriptor)
    #fps = [RDKFingerprint(mol) for mol in mols]
    #print(fps)
    #BRDLigs = PandasTools.LoadSDF(SDFFile)
    #print(BRDLigs.info())
    #BRDLigs['NumHeavyAtoms'] = BRDLigs.apply(lambda x: x['ROMol'].GetNumHeavyAtoms(), axis=1)
    #print(BRDLigs)


def tanimoto_calc(smi1, smi2):
    mol1 = Chem.MolFromSmiles(smi1)
    mol2 = Chem.MolFromSmiles(smi2)
    fp1 = AllChem.GetMorganFingerprintAsBitVect(mol1, 3, nBits=2048)
    fp2 = AllChem.GetMorganFingerprintAsBitVect(mol2, 3, nBits=2048)
    s = round(DataStructs.TanimotoSimilarity(fp1,fp2),3)
    print(s)
    return s


def main():
    data = open('', 'r')
    mol1 = ''
    fp1 = AllChem.GetMorganFingerprintAsBitVect(mol1, 3, nBits=2048)


def pca(data, labels):
    pca = PCA(n_components=3)
    X = pca.fit_transform(data)
    df2 = pd.DataFrame(X)
    df2['labels'] = labels
    df2.columns = ['PC1', 'PC2', 'PC3', 'labels']
    fig = px.scatter_3d(df2, x='PC1', y='PC2', z='PC3', color='labels')
    """
    Scene = dict(xaxis=dict(title='PC1', showgrid=True, gridwidth=1, gridcolor='black'),
                 yaxis=dict(title='PC2', showgrid=True, gridwidth=1, gridcolor='black'),
                 zaxis=dict(title='PC3', showgrid=True, gridwidth=1, gridcolor='black'))
    trace = go.Scatter3d(x=df2['PC1'], y=df2['PC2'], z=df2['PC3'], hovertext=df2['labels'])
                         #marker_symbol=df2['markers'], #symbol=df2['markers'],
                         #marker=dict(color=df2['labels'], size=10, line=dict(color='black', width=10)))
    data = [trace]
    layout = go.Layout(margin=dict(l=0, r=0), scene=Scene, height=800, width=1200)
    fig = go.Figure(data=data, layout=layout)
    """
    fig.show()
    #fig.write_html('BZD_Fingerprints.html')
    labels = df2['labels'].tolist()
    dfs = df2.loc[:, df2.columns != 'labels']
    fig = ff.create_dendrogram(dfs, labels=labels)
    fig.update_layout(width=1400, height=1050, title='Ligand Fingerprints')
    fig.update_layout(
        font=dict(
            size=18
        )
    )
    #fig.write_html('Male_FAERS_PCA.html')
    fig.show()


if __name__ == '__main__':
    biomed()
