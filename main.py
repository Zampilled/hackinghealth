from scipy import stats
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# https://github.com/Zampilled/SnippetGeneration/blob/main/bin/eval/graph.py (My Own Code from different project )
def graph_metrics(men:  pd.Series, women :pd.Series, outputdir: str):
    colors = sns.color_palette()
    sns.set_theme()
    plt.figure(figsize=(12, 6))


    sns.kdeplot(men, label="Men", fill=True, color=colors[0], warn_singular=False)
    sns.kdeplot(women, label="Women", fill=True, color=colors[1], warn_singular=False)


    mean_value = men.mean()
    plt.axvline(x=mean_value, linestyle='--', label='Men Mean', alpha=0.7, color=colors[0])
    mean_value = women.mean()
    plt.axvline(x=mean_value, linestyle='--', label='Women Mean', alpha=0.7, color=colors[1])

    plt.xlabel('Values')
    plt.ylabel('Density')
    plt.title('Distribution of Heavy Activity')
    plt.legend()
    plt.savefig(outputdir)
    plt.show()



if __name__ == '__main__':
    #Reads data of input file and divides by sex
    df = pd.read_csv("data.csv")
    print(df.head())
    df_men = df[df["sex"]=="Male"]
    df_women = df[df["sex"] =="Female"]


    # source https://neuraldatascience.io/5-eda/ttests.html
    # Stat to test
    test_stat = "heavy_total"

    # Runs independent t-test on stat
    myStats = stats.ttest_ind(df_women[test_stat], df_men[test_stat])
    # saves p-value in file
    with open("out.txt", "a") as f:
        f.write(str(myStats.pvalue))
    # Graphs distribution of stat
    graph_metrics(df_men[test_stat], df_women[test_stat], outputdir="output.png")