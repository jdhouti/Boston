import matplotlib.pyplot as plt
import datetime as dt

#create some data
x_series = [10, 11, 12]
y_series_1 = [1, 2, 3]
#y_series_2 = [x**3 for x in x_series]

#plot the two lines
plt.plot(x_series, y_series_1, label="Julien")
#plt.plot(x_series, y_series_2, label="Jesse")
plt.title(dt.datetime.today().strftime("%m/%d/%Y"))

plt.legend(loc="upper left")

plt.savefig("example.png")
