import pandas as pd
import matplotlib.pyplot as plt

# Create a dictionary with the data
data = {
    'Computer': {'Nairobi': 22.7, 'Kiambu': 19.6, 'Kajiado': 14.6, 'Uasin Gishu': 10.1, 'Kisumu': 9.8},
    'Refrigerator': {'Nairobi': 23.5, 'Kiambu': 19.6, 'Kajiado': 15.8, 'Kisumu': 11.6, 'Machakos': 9.4}
}

# Create a pandas DataFrame with the data
df = pd.DataFrame(data)

# Plot the data as a bar chart
df.plot(kind='bar', figsize=(10, 5))
plt.ylabel('Percentage of Households')
plt.xlabel('Counties')
plt.title('Highest Share of Households with a Computer or Refrigerator')
plt.show()
