import matplotlib.pyplot as plt
programming_languages = ["C++", "C#", "Python", "Go", 'Java']
number_of_users = [40, 120, 250, 115, 8] 
plt.pie(number_of_users, labels=programming_languages, autopct='%1.1f%%')
plt.title("Distribution of Programming Languages Among Programmers")
plt.show()