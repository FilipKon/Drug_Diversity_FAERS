import pandas as pd
import warnings
import networkx as nx
import plotly.graph_objects as go
from matplotlib.pyplot import figure
import matplotlib.pyplot as plt
from bokeh.io import output_notebook, show, save
from bokeh.models import Range1d, Circle, ColumnDataSource, MultiLine
from bokeh.plotting import figure
from bokeh.plotting import from_networkx
from bokeh.palettes import Blues8, Reds8, Purples8, Oranges8, Viridis8, Spectral8
from bokeh.transform import linear_cmap
from networkx.algorithms import community

warnings.filterwarnings("ignore")
pd.set_option('display.max_columns', 1000)  # or None
pd.set_option('display.max_rows', 1000)  # or None
pd.set_option('display.max_colwidth', 100)  # or None

path = 'C:\\Users\\TARIQOPLATA\\PycharmProjects\\FAERS_final\\data\\data\\Old_gold\\'


# path = '/Users/ftk/Documents/Work/FAERS_final/data/Old_gold/'


def main2():
    df_f = pd.read_csv(path + 'Disprop_analysis_female_with_HTs.csv')
    df_m = pd.read_csv(path + 'Disprop_analysis_male_with_HTs.csv')
    hts = ['psychiatric disorders', 'nervous system disorders']
    drug = ['midazolam', 'flurazepam', 'nordazepam', 'quazepam', 'ethyl loflazepate']
    df_m1 = df_m[df_m['DRUG'].isin(drug)]
    df_f1 = df_f[df_f['DRUG'].isin(drug)]
    df_m1 = df_m1[df_m1['HT'].isin(hts)]
    df_f1 = df_f1[df_f1['HT'].isin(hts)]
    df_f1['Sex'] = 'F'
    df_m1['Sex'] = 'M'
    frames = [df_f1, df_m1]
    df = pd.concat(frames)
    G = nx.from_pandas_edgelist(df_f1, 'DRUG', 'AE', edge_attr=True)
    """
    sources = list(df['DRUG'])
    destinations = list(df['AE'])

    g_from_data = nx.Graph(height='600px', width='50%',
                              bgcolor='white', font_color="black",
                              heading="A Networkx Graph from DataFrame", directed=True)

    for i in range(len(sources)):
        try:
            g_from_data.add_node(sources[i], label=sources[i], title=sources[i])
        except:
            pass

    for (i, j) in zip(sources, destinations):
        try:
            g_from_data.add_edge(i, j)
        except:
            pass

    nx.draw(g_from_data, with_labels=True, font_weight='bold')
    plt.show()"""

    labels = {
        n: (G.nodes[n]['label']
            if len(list(nx.all_neighbors(G, n))) > 3
            else '')
        for n in G.nodes
    }
    nx.draw(G, with_labels=False, node_size=30, node_color="skyblue", node_shape="s", alpha=0.5, linewidths=20,
            font_size=12, labels=labels)
    pos = nx.drawing.layout.spring_layout(G)
    #labels = {}
    #for node in G.nodes():
    #    if node in df['DRUG']:
    #        labels[node] = node,
    #nx.draw(G, with_labels=False)
    #nx.draw_networkx_labels(G, pos, labels, font_size=16, font_color='r')
    plt.show()

    nx.set_node_attributes(G, pos, 'pos')
    #drugs = df['DRUG'].tolist()
    #drugs = list(dict.fromkeys(drugs))

    edge_x = []
    edge_y = []
    for edge in G.edges():
        x0, y0 = G.nodes[edge[0]]['pos']
        x1, y1 = G.nodes[edge[1]]['pos']
        edge_x.append(x0)
        edge_x.append(x1)
        edge_x.append(None)
        edge_y.append(y0)
        edge_y.append(y1)
        edge_y.append(None)

    edge_trace = go.Scatter(
        x=edge_x, y=edge_y,
        line=dict(width=0.5, color='#888'),
        hoverinfo='none',
        mode='lines')

    node_x = []
    node_y = []
    for node in G.nodes():
        x, y = G.nodes[node]['pos']
        print(G.nodes[node])
        node_x.append(x)
        node_y.append(y)

    node_trace = go.Scatter(
        x=node_x, y=node_y,
        mode='markers',
        hoverinfo='text',
        #text=drugs,
        marker=dict(
            showscale=True,
            colorscale='YlGnBu',
            reversescale=True,
            color=[],
            size=10,
            colorbar=dict(
                thickness=15,
                title='Node Connections',
                xanchor='left',
                titleside='right'
            ),
            line_width=2))

    node_adjacencies = []
    node_text = []
    for node, adjacencies in enumerate(G.adjacency()):
        node_adjacencies.append(len(adjacencies[1]))
        node_text.append('# of connections: ' + str(len(adjacencies[1])))

    node_trace.marker.color = node_adjacencies
    node_trace.text = node_text

    fig = go.Figure(data=[edge_trace, node_trace],
                    layout=go.Layout(
                        title='<br>Network graph made with Python',
                        titlefont_size=16,
                        showlegend=False,
                        hovermode='closest',
                        margin=dict(b=20, l=5, r=5, t=40),
                        annotations=[dict(
                            text="Python code: <a href='https://plotly.com/ipython-notebooks/network-graphs/'> https://plotly.com/ipython-notebooks/network-graphs/</a>",
                            showarrow=False,
                            xref="paper", yref="paper",
                            x=0.005, y=-0.002)],
                        xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
                        yaxis=dict(showgrid=False, zeroline=False, showticklabels=False))
                    )
    fig.show()


def main():
    df_f = pd.read_csv(path + 'Disprop_analysis_female_with_HTs.csv')
    df_m = pd.read_csv(path + 'Disprop_analysis_male_with_HTs.csv')
    hts = ['psychiatric disorders', 'nervous system disorders']
    drug = ['midazolam', 'flurazepam', 'nordazepam', 'quazepam', 'ethyl loflazepate']
    df_m1 = df_m[df_m['DRUG'].isin(drug)]
    df_f1 = df_f[df_f['DRUG'].isin(drug)]
    df_m1 = df_m1[df_m1['HT'].isin(hts)]
    df_f1 = df_f1[df_f1['HT'].isin(hts)]
    df_f1['Sex'] = 'F'
    df_m1['Sex'] = 'M'
    frames = [df_f1, df_m1]
    df = pd.concat(frames)
    G = nx.from_pandas_edgelist(df_f1, 'DRUG', 'AE', 'IC025')
    degrees = dict(nx.degree(G))
    nx.set_node_attributes(G, name='degree', values=degrees)
    number_to_adjust_by = 5
    adjusted_node_size = dict([(node, degree + number_to_adjust_by) for node, degree in nx.degree(G)])
    nx.set_node_attributes(G, name='adjusted_node_size', values=adjusted_node_size)
    # Choose attributes from G network to size and color by — setting manual size (e.g. 10) or color (e.g. 'skyblue') also allowed
    size_by_this_attribute = 'adjusted_node_size'
    color_by_this_attribute = 'adjusted_node_size'

    # Pick a color palette — Blues8, Reds8, Purples8, Oranges8, Viridis8
    color_palette = Blues8

    # Choose a title!
    title = 'FAERS Network'

    # Establish which categories will appear when hovering over each node
    HOVER_TOOLTIPS = [
        ("Name", "@index"),
        ("Degree", "@degree")
    ]

    # Create a plot — set dimensions, toolbar, and title
    plot = figure(tooltips=HOVER_TOOLTIPS,
                  tools="pan,wheel_zoom,save,reset", active_scroll='wheel_zoom',
                  x_range=Range1d(-10.1, 10.1), y_range=Range1d(-10.1, 10.1), title=title)

    # Create a network graph object
    # https://networkx.github.io/documentation/networkx-1.9/reference/generated/networkx.drawing.layout.spring_layout.html\
    network_graph = from_networkx(G, nx.spring_layout, scale=10, center=(0, 0))

    # Set node sizes and colors according to node degree (color as spectrum of color palette)
    minimum_value_color = min(network_graph.node_renderer.data_source.data[color_by_this_attribute])
    maximum_value_color = max(network_graph.node_renderer.data_source.data[color_by_this_attribute])
    network_graph.node_renderer.glyph = Circle(size=size_by_this_attribute,
                                               fill_color=linear_cmap(color_by_this_attribute, color_palette,
                                                                      minimum_value_color, maximum_value_color))

    # Set edge opacity and width
    network_graph.edge_renderer.glyph = MultiLine(line_alpha=0.5, line_width=1)

    plot.renderers.append(network_graph)

    show(plot)
    # save(plot, filename=f"{title}.html")


def boke():
    global community
    df_f = pd.read_csv(path + 'Disprop_analysis_female_with_HTs.csv')
    df_m = pd.read_csv(path + 'Disprop_analysis_male_with_HTs.csv')
    hts = ['psychiatric disorders', 'nervous system disorders']
    drug = ['midazolam', 'flurazepam', 'nordazepam', 'quazepam', 'ethyl loflazepate', 'zolpidem', 'zopiclone', 'eszopiclone',
            'zaleplon', 'brotizolam', 'etizolam']
    df_m = df_m[df_m['DRUG'].isin(drug)]
    df_f = df_f[df_f['DRUG'].isin(drug)]
    df_m1 = df_m[df_m['HT'].isin(hts)]
    df_f1 = df_f[df_f['HT'].isin(hts)]
    df_f1['Sex'] = 'F'
    df_m1['Sex'] = 'M'
    frames = [df_f1, df_m1]
    df = pd.concat(frames)
    print(df_f1)
    G = nx.from_pandas_edgelist(df_f1, 'DRUG', 'AE', 'IC025')
    degrees = dict(nx.degree(G))
    nx.set_node_attributes(G, name='degree', values=degrees)
    number_to_adjust_by = 5
    adjusted_node_size = dict([(node, degree + number_to_adjust_by) for node, degree in nx.degree(G)])
    nx.set_node_attributes(G, name='adjusted_node_size', values=adjusted_node_size)
    communities = None
    communities = community.greedy_modularity_communities(G)
    # Create empty dictionaries
    modularity_class = {}
    modularity_color = {}
    # Loop through each community in the network
    for community_number, community in enumerate(communities):
        # For each member of the community, add their community number and a distinct color
        for name in community:
            modularity_class[name] = community_number
            modularity_color[name] = Spectral8[community_number]
    # Add modularity class and color as attributes from the network above
    nx.set_node_attributes(G, modularity_class, 'modularity_class')
    nx.set_node_attributes(G, modularity_color, 'modularity_color')
    # Choose attributes from G network to size and color by — setting manual size (e.g. 10) or color (e.g. 'skyblue') also allowed
    size_by_this_attribute = 'adjusted_node_size'
    color_by_this_attribute = 'modularity_color'
    # Pick a color palette — Blues8, Reds8, Purples8, Oranges8, Viridis8
    color_palette = Blues8
    # Choose a title!
    title = 'FAERS Network'

    # Establish which categories will appear when hovering over each node
    HOVER_TOOLTIPS = [
        ("Character", "@index"),
        ("Degree", "@degree"),
        ("Modularity Class", "@modularity_class"),
        ("Modularity Color", "$color[swatch]:modularity_color"),
    ]

    # Create a plot — set dimensions, toolbar, and title
    plot = figure(tooltips=HOVER_TOOLTIPS, width=1400, height=1400,
                  tools="pan,wheel_zoom,save,reset, tap", active_scroll='wheel_zoom',
                  title=title, x_range=Range1d(-50.1, 50.1), y_range=Range1d(-50.1, 50.1)) # x_range=Range1d(-50.1, 50.1), y_range=Range1d(-50.1, 50.1),

    # Create a network graph object
    # https://networkx.github.io/documentation/networkx-1.9/reference/generated/networkx.drawing.layout.spring_layout.html
    network_graph = from_networkx(G, nx.kamada_kawai_layout, scale=10, center=(0, 0))

    # Set node sizes and colors according to node degree (color as category from attribute)
    network_graph.node_renderer.glyph = Circle(size=size_by_this_attribute, fill_color=color_by_this_attribute)

    # Set edge opacity and width
    network_graph.edge_renderer.glyph = MultiLine(line_alpha=0.5, line_width=1)

    plot.renderers.append(network_graph)

    show(plot)
    save(plot, filename="Test.html")


if __name__ == '__main__':
    boke()
