import matplotlib.pyplot as plt
programming_languages = ["C++", "C#", 
            "Python", "Go", 'Java']
number_of_users = [40, 120, 250,
                   115, 8] 
explode = [0,0,0.05,0,0]
plt.pie(number_of_users, 
        labels=programming_languages,
        explode=explode , autopct='%1.1f%%')
plt.show()