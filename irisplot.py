import seaborn as sns

import matplotlib.pyplot as plt

def main():
    df = sns.load_dataset("iris")
    g = sns.pairplot(df, hue="species")
    g.savefig("iris_pairplot.png", dpi=300)
    plt.close(g.fig)

if __name__ == "__main__":
    main()