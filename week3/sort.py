import matplotlib.pyplot as plt

sort1rand = [0.064, 0.207, 6.320]
sort2rand = [0.029, 0.070, 0.853]
sort3rand = [0.046, 0.182, 3.297]
sort1reserved = [0.076, 0.265, 6.103]
sort2reserved = [0.030, 0.067, 1.291]
sort3reserved = [0.052, 0.149, 3.381]
x = [5000, 10000, 50000]
plt.plot(x, sort1rand, label="sort1rand")
plt.plot(x, sort2rand, label="sort2rand")
plt.plot(x, sort3rand, label="sort3rand")
plt.plot(x, sort1reserved, label="sort1reserved")
plt.plot(x, sort2reserved, label="sort2reserved")
plt.plot(x, sort3reserved, label="sort3reserved")

plt.xlabel("Number of data")
plt.ylabel("Time[s]")
plt.legend()
plt.show()
