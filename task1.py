import matplotlib.pyplot as plt
import pandas as pd
data={'age_groups' : ['0-9', '10-19', '20-29', '30-39', '40-49', '50-59', '60-69', '70-79', '80+'],'population' : [150, 250, 400, 600, 550, 700, 800, 500, 200]}
dataset=pd.DataFrame(data)
print(dataset)
dataset.plot(kind='bar',x='age_groups',y='population')
plt.xlabel('Age Group')
plt.ylabel('Number of People')
plt.title('Distribution of Ages in a Population')
plt.show()