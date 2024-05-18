import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import dendrogram, linkage

# Load the data
file_path = 'C:\\Users\\leoma\\PycharmProjects\\pythonProject1\\Comparative_Genomics_Statistics\\OrthologuesStats_Totals.tsv'
data = pd.read_csv(file_path, sep='\t', index_col=0)

# Normalize the data (Z-score normalization along the rows)
normalized_data = data.subtract(data.mean(axis=1), axis=0).divide(data.std(axis=1), axis=0)

# Hierarchical clustering
linkage_matrix = linkage(normalized_data, method='ward')

# Create a clustered heatmap without a color bar
sns.set(style="whitegrid", font_scale=0.5)  # Adjust font scale to make text smaller
g = sns.clustermap(normalized_data, cmap='coolwarm', row_linkage=linkage_matrix, col_linkage=linkage_matrix,
                   figsize=(20, 20), linewidths=.5, cbar=False)  # Disable the color bar

# Rotate labels for better visibility
plt.setp(g.ax_heatmap.get_xticklabels(), rotation=90)
plt.setp(g.ax_heatmap.get_yticklabels(), rotation=0)

plt.show()
