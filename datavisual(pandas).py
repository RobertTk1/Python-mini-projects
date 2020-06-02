
import pandas as pd
import matplotlib.pyplot as plt

x = [1,2,3]
y = [1,4,9]
z = [2,4,7]

'''plt.plot(x,y)
plt.title('Text plot')
plt.xlabel('X axis')
plt.ylabel('Y axis')
plt.legend(['this is y','this is z'])

plt.show()'''

sdata = pd.read_csv('sample_data.csv')

print(sdata.column_a)