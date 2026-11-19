
import numpy as np
import matplotlib.pyplot as plt

# Load the CSV data
data = np.genfromtxt(
    'June-2021-Provo-River-Streamflow-Rates.csv',
    delimiter=',',
    dtype=str,
    skip_header=1
)

# Create x and y values
x = data[:, 0]

y_1 = data[:, 1].astype(float)
y_2 = data[:, 2].astype(float)
y_3 = data[:, 3].astype(float)
y_4 = data[:, 4].astype(float)
y_5 = data[:, 5].astype(float)

# Convert dates
x = np.array(x, dtype='datetime64[m]')

# Graph the data
plt.figure(figsize=(10, 7))

plt.plot(x, y_1, label='10163000')
plt.plot(x, y_2, label='10155200')
plt.plot(x, y_3, label='10155500')
plt.plot(x, y_4, label='10154200')
plt.plot(x, y_5, label='10155000')

plt.title('Provo River Streamflow Data (2021)')
plt.xlabel('Date')
plt.ylabel('Flowrate (cfs)')

plt.xticks(rotation=45)

plt.grid(True)
plt.legend(title='Site Numbers')

plt.tight_layout()
plt.show()
