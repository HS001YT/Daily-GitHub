import seaborn as sns
import matplotlib.pyplot as plt

data = sns.load_dataset('iris')

# sns.jointplot(x = "sepal_length", y = "petal_length", data = data)

sns.pairplot(data, hue="species", kind="kde", aspect=1.5, height=1.8)
# hue - used for another dimension
# kind - parameter is used for different types of plot (kind="kde")

plt.get_current_fig_manager().set_window_title("Day 24.2 with kind")
# plt.savefig("D:\Daily-GitHub\Data Visualization\other_files\Day24.2.png", dpi=300, bbox_inches="tight")

plt.show()