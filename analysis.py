import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

df = pd.read_csv('data/standard_stats.csv')

## scatter graph to show expected goals against actual goals in the season
plt.scatter(df['xG'], df['Gls'])

# indexing through all players in the data frame under these columns and making the points
for i in range(len(df)):
    plt.text(df['xG'][i], df['Gls'][i], df['Player'][i], fontsize=10)

# plotting scatter graph
plt.title('xG vs Actual Goals')
plt.xlabel('Expected Goals')
plt.ylabel('Actual Goals')
plt.grid(True)
# label for the equal line through grid
plt.axline((0, 0), slope=1, linestyle='--', color='gray', label='xG = Goals')
plt.legend()
plt.show()

## bar chart showing top 5 most carded players in the season
# sorting players by most number of cards
df = df.sort_values(by='CrdY', ascending=False)
# picking the top 5
top5 = df.head(5)
# plotting bar chart
plt.bar(top5['Player'], top5['CrdY'], color='gold')
plt.xticks(fontsize=7.5)
plt.savefig('yellow_cards.png')
plt.show()

## stacked bar chart showing distribution of G+As
# calculating total and getting the top 5 players
df['total'] = df['Gls']+df['Ast']
top5 = df.nlargest(5, 'total')
# plotting bars
x = np.arange(len(top5['Player']))
plt.bar(x, top5['Ast'], label='Assists')
plt.bar(x, top5['Gls'], bottom=top5['Ast'], label='Goals')

plt.xticks(x, top5['Player'])
plt.xlabel('Player')
plt.ylabel('Goals and Assists')
plt.title('Assists vs Goals')
plt.xticks(fontsize=7.5)
plt.legend()
plt.show()