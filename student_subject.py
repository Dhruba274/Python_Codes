import matplotlib.pyplot as plt
x=[1,3,5,7,9]
x1=[2,4,6,8,10]
y=[80,90,87,98,88]
y1=[84,85,86,97,98]
plt.bar(x,y,label='first')
plt.bar(x1,y1,label='second')
plt.xlabel("Subject")
plt.ylabel("marks")
plt.show()