import matplotlib.pyplot as plt
import pandas as pd

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

