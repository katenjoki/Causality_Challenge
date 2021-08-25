import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

#Count plot
def plot_count(data:pd.DataFrame,col:str)->None:
    sns.countplot(data[col],palette = 'RdYlGn')
    plt.xlabel(f'Cancer {col}')
    plt.ylabel('Count')
    plt.title(f'Count of Cancer {col}')
    plt.show()
    
#Correlation matrix    
def plot_corr(data:pd.DataFrame)->None:
    corr = data.corr()
    plt.figure(figsize=(20,20))
    sns.heatmap(corr, cbar=True, square= True, fmt='.1f', annot=True, annot_kws={'size':15}, cmap='summer_r')
    plt.savefig("../figures/correlation.png")
    plt.show()

#Scatter plot
def plot_scatter(df,col1,col2):
    plt.figure(figsize=(12, 7))
    sns.scatterplot(data = df, x=col1, y=col2, hue="diagnosis",palette='summer_r')
    plt.title(f'{col1} vs {col2}', size=16)
    plt.xticks(fontsize=14)
    plt.yticks( fontsize=14)
    plt.show()
    
#Distribution plot    
def plot_distribution(data:pd.DataFrame,col:str)->None:
    sns.FacetGrid(data, hue="diagnosis", height=6,palette='summer_r').map(sns.distplot, col).add_legend()
    plt.show()