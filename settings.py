drugs_alpha = {'alprazolam': 962, 'bromazepam': 963, 'brotizolam': 964, 'chlordiazepoxide': 965, 'cinolazepam': 966,
               'clobazam': 967, 'clonazepam': 968, 'clorazepate': 969, 'clotiazepam': 970, 'cloxazolam': 971,
               'diazepam': 972, 'estazolam': 973, 'eszopiclone': 974, 'ethyl loflazepate': 975, 'etizolam': 976,
               'flumazenil': 977, 'flunitrazepam': 978, 'flurazepam': 979, 'ketazolam': 980, 'lorazepam': 981,
               'lormetazepam': 982, 'medazepam': 983, 'mexazolam': 984, 'midazolam': 985, 'nimetazepam': 986,
               'nitrazepam': 987,
               'nordazepam': 988, 'oxazepam': 989, 'oxazolam': 990, 'prazepam': 991, 'quazepam': 992, 'temazepam': 993,
               'tetrazepam': 994, 'tofisopam': 995, 'triazolam': 996, 'triazulenone': 997, 'zaleplon': 998,
               'zolpidem': 999, 'zopiclone': 1000}

colors_d = {'alprazolam': '#FF5733', 'diazepam': '#75A7AB', 'lorazepam': '#B73C22', 'clonazepam': '#906056',
            'zolpidem': '#9DF8DF', 'tetrazepam': '#ff9d5c', 'cloxazolam': '#4b4c07', 'clotiazepam': '#e9fe92',
            'flumazenil': '#D6DA03', 'triazulenone': '#FFD4EB', 'quazepam': '#F9C469', 'nordazepam': '#68D6DF',
            'tofisopam': '#C3C553', 'mexazolam': '#BEFC8B', 'medazepam': '#27FFC4', 'ketazolam': '#636161',
            'cinolazepam': '#C5A9A3', 'oxazolam': '#5FB815', 'lormetazepam': '#66953E', 'prazepam': '#FF0087',
            'flunitrazepam': '#FB11FF', 'nitrazepam': '#E49C20', 'estazolam': '#8E3564', 'ethyl loflazepate': '#FBB4FC',
            'etizolam': '#0CC492', 'brotizolam': '#B498FF', 'clorazepate': '#0CC44C', 'triazolam': '#1349C4',
            'chlordiazepoxide': '#4a8c12', 'flurazepam': '#75AB9C', 'zaleplon': '#18E4F5', 'eszopiclone': '#00B9FF',
            'temazepam': '#82F721', 'zopiclone': '#458AA4', 'bromazepam': '#4562A4', 'oxazepam': '#A585C4',
            'clobazam': '#2C6CFF', 'midazolam': '#98B7FF', 'remimazolam': '#8000FF'}

colors_g = {'F': '#e5a2bd', 'M': '#9aceeb'}

symbols_d = {'alprazolam': "/", 'diazepam': ".", 'lorazepam': "x", 'clonazepam': "-",
            'zolpidem': "/", 'tetrazepam': "+", 'cloxazolam': ".",
            'flumazenil': "/", 'triazulenone': "x", 'quazepam': "-", 'nordazepam': "|",
            'tofisopam': "+", 'mexazolam': ".", 'ketazolam': "/",
            'cinolazepam': "x", 'oxazolam': "-", 'lormetazepam': "|", 'prazepam': "+",
            'flunitrazepam': ".", 'estazolam': "/", 'ethyl loflazepate': "",
            'etizolam': "-", 'brotizolam': "|", 'clorazepate': "+", 'triazolam': ".",
            'flurazepam': "/", 'zaleplon': "x", 'eszopiclone': "-",
            'zopiclone': "+", 'bromazepam': "/", 'oxazepam': "x", "nitrazepam": "x",
            'clobazam': "/", 'midazolam': "x", 'remimazolam': "-"}

symbols_d = {'nervous system neoplasms benign': "/", 'adjustment disorders (incl subtypes)': ".", 'demyelinating disorders': "x",
             'headaches': "-",
            'nervous system neoplasms malignant and unspecified nec': "/", 'central nervous system infections and inflammations': "+",
             'neurological disorders of the eye': ".",
            'spinal cord and nerve root disorders': "/", 'triazulenone': "x", 'quazepam': "-", 'nordazepam': "|",
            'tofisopam': "+", 'mexazolam': ".", 'ketazolam': "/",
            'cinolazepam': "x", 'oxazolam': "-", 'lormetazepam': "|", 'prazepam': "+",
            'flunitrazepam': ".", 'estazolam': "/", 'ethyl loflazepate': "",
            'etizolam': "-", 'brotizolam': "|", 'clorazepate': "+", 'triazolam': ".",
            'flurazepam': "/", 'zaleplon': "x", 'eszopiclone': "-",
            'zopiclone': "+", 'bromazepam': "/", 'oxazepam': "x", "nitrazepam": "x",
            'clobazam': "/", 'midazolam': "x", 'remimazolam': "-"}

symbols = {'alprazolam': 'circle', 'diazepam': 'hexagon', 'lorazepam': 'star', 'clonazepam': 'square',
           'zolpidem': 'diamond', 'tetrazepam': 'cross', 'cloxazolam': 'x', 'clotiazepam': 'star-triangle-up-open',
           'flumazenil': 'pentagon', 'triazulenone': 'hourglass', 'quazepam': 'octagon', 'nordazepam': 'arrow',
           'tofisopam': 'arrow-down', 'mexazolam': 'circle-cross', 'medazepam': 'diamond-wide', 'ketazolam': 'bowtie',
           'cinolazepam': 'star-square', 'oxazolam': 'hexagram', 'lormetazepam': 'diamond-open',
           'prazepam': 'circle-open',
           'flunitrazepam': 'x-open', 'nitrazepam': 'circle-x', 'estazolam': 'triangle-ne',
           'ethyl loflazepate': 'pentagon-open',
           'etizolam': 'star-open', 'brotizolam': 'triangle-left', 'clorazepate': 'square-open',
           'triazolam': 'arrow-open',
           'chlordiazepoxide': 'square-open', 'flurazepam': 'triangle-right', 'zaleplon': 'diamond-tall',
           'eszopiclone': 'star-square-open',
           'temazepam': 'bowtie-open', 'zopiclone': 'asterisk-open', 'bromazepam': 'triangle-right-open',
           'oxazepam': 'hexagon2-open', 'clobazam': 'triangle-se', 'triangle-sw': 'hash', 'remimazolam': 'diamond-open'}