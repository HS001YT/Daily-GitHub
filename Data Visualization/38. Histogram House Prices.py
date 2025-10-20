import matplotlib.pyplot as plt
import seaborn as sns

# Load Titanic dataset
titanic = sns.load_dataset("titanic")

ages = titanic['age']       
# Other columns list- [survived, pclass, sex, age, sibsp, parch, fare, embarked, class, who, adult_male, deck, embark_town, alive, alone]

sns.histplot(data=titanic, x="age", bins=20, kde=True, color="skyblue", element="step") # Remove element to see normal histogram view
plt.title("Age Distribution Histogram (Titanic Dataset)")
plt.xlabel("Age")
plt.ylabel("Numbers")

plt.annotate("Source: Seaborn", 
             xy=(0.7, 0.8), xycoords="figure fraction",
             ha="left", fontsize=9, color="gray")

plt.get_current_fig_manager().set_window_title("Day 14")
# plt.savefig("D:\Daily-GitHub\Data Visualization\other_files\Day14.png", dpi=300, bbox_inches="tight")

plt.show()
