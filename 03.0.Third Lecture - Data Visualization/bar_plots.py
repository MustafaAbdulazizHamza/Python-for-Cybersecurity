import matplotlib.pyplot as plt
programming_languages = ["C++", "C#",
                "Python", "Go",
                'Java']
votes = [40, 120, 250, 115, 8]
plt.bar(programming_languages, votes,
        color='purple', width=0.5)
plt.xlabel("Languages")
plt.ylabel("Votes")
plt.show()