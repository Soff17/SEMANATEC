#!/usr/bin/env python
# coding: utf-8

# In[28]:


import pandas, seaborn, matplotlib
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

data = pd.read_table("data1.txt")
plt.boxplot(data)
plt.title('Grafica Boxplot',
          fontweight ="bold")
plt.show()


# In[29]:


import pandas, seaborn, matplotlib
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

data = pd.read_csv("data1.csv")
df = pd.DataFrame(data)

x =  df['x']
num_bins=60
n, bins, patches = plt.hist(x, num_bins, 
                            density = 1, 
                            color ='green',
                            alpha = 0.7)
y = df['y']

plt.plot(bins, y, '--', color ='black')
  
plt.xlabel('X-Axis')
plt.ylabel('Y-Axis')
  
plt.title('Grafica Funcion Hist',
          fontweight ="bold")
  
plt.show()


# In[25]:


import pandas, seaborn, matplotlib
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

data = pd.read_table("data1.txt")
data[:10]
data.corr(method ='pearson')


# In[30]:


import pandas
import seaborn as sns, matplotlib
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

data = pd.read_table("data1.txt")
sns.pairplot(data)
plt.title('Grafica Correlacion',
          fontweight ="bold")
plt.show()


# In[33]:


import pandas
import seaborn as sns, matplotlib
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

data = pd.read_table("data1.txt")
np.random.seed(0)
sns.set_theme()

ax = sns.heatmap(data)


# In[ ]:




