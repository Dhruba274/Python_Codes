import matplotlib.pyplot as plt
result=[44,180,200]
parties=["ABC","XYZ","MNP"]
plt.pie(result,labels=parties,startangle=90)
plt.legend()
plt.show()