electricity_consumption = [450, 475, 510, 540, 580, 620, 650, 680, 710, 740, 775, 800]
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
import matplotlib.pyplot as plt

# Create a line plot
plt.bar(months, electricity_consumption)

# Add a title
plt.title('Electricity Consumption Over 12 Months')

# Add x and y labels
plt.xlabel('Months')
plt.ylabel('Electricity Consumption (kWh)')

# Show the plot
plt.show()