import matplotlib.pyplot as plt
data =  [(83000, 8.7), (88000, 8.1),
        (48000, 0.7), (76000, 6),
        (69000, 6.5), (76000, 7.5),
        (60000, 2.5), (83000, 10),
        (48000, 1.9), (63000, 4.2)]
years_experience = [i[1] for i in data]
salaries = [i[0] for i in data]
plt.scatter(years_experience, salaries)
plt.xlabel("Years Experience")
plt.ylabel("Salary")
plt.show()

