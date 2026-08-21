import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

os.makedirs("charts", exist_ok=True)

sns.set_theme(style="whitegrid")
plt.rcParams.update({'font.size': 12})

print("Generating charts for presentation...")


try:
    df1 = pd.read_csv("results/job1_country_result.txt", sep="\t", names=["Country", "Avg_Usage_Hrs", "User_Count"])
    df1 = df1.sort_values(by="Avg_Usage_Hrs", ascending=False).head(10) # Top 10 for clean visual

    plt.figure(figsize=(10, 6))
    sns.barplot(data=df1, x="Avg_Usage_Hrs", y="Country", palette="viridis")
    plt.title("Job 1: Average Daily Social Media Usage by Country (Top 10)", fontweight='bold')
    plt.xlabel("Average Usage (Hours)")
    plt.ylabel("")
    plt.tight_layout()
    plt.savefig("charts/job1_country_chart.png", dpi=300)
    plt.close()
except FileNotFoundError:
    print("Job 1 data not found")

try:
    df2 = pd.read_csv("results/job2_bucketed_result.txt", sep="\t", names=["Usage_Bucket", "Avg_MH_Score", "Count"])
    
    order = ["0-2h", "2-4h", "4-6h", "6-8h", "8h+"]
    df2['Usage_Bucket'] = pd.Categorical(df2['Usage_Bucket'], categories=order, ordered=True)
    df2 = df2.sort_values("Usage_Bucket")

    plt.figure(figsize=(8, 5))
    ax = sns.barplot(data=df2, x="Usage_Bucket", y="Avg_MH_Score", palette="mako")
    
    ax.plot(range(len(df2)), df2["Avg_MH_Score"], color="red", marker="o", linewidth=2.5, label="Trend (r = -0.76)")
    
    plt.title("Job 2: Mental Health Score vs. Daily Usage", fontweight='bold')
    plt.xlabel("Daily Usage (Hours)")
    plt.ylabel("Average Mental Health Score")
    plt.legend()
    plt.tight_layout()
    plt.savefig("charts/job2_bucketed_chart.png", dpi=300)
    plt.close()
except FileNotFoundError:
    print("Job 2 data not found")

try:
    df4 = pd.read_csv("results/job4_result.txt", sep="\t", names=["Composite_Key", "Count"])
    
    df4[['Platform', 'Addiction']] = df4['Composite_Key'].str.split('|', expand=True)
    
    pivot_df4 = df4.pivot(index="Platform", columns="Addiction", values="Count").fillna(0)
    
    if set(["Low", "Medium", "High"]).issubset(pivot_df4.columns):
        pivot_df4 = pivot_df4[["Low", "Medium", "High"]]

    pivot_df4.plot(kind="bar", stacked=False, figsize=(12, 6), colormap="coolwarm")
    plt.title("Job 4: Social Media Addiction Levels by Platform", fontweight='bold')
    plt.xlabel("Social Media Platform")
    plt.ylabel("Number of Users")
    plt.xticks(rotation=45)
    plt.legend(title="Addiction Level")
    plt.tight_layout()
    plt.savefig("charts/job4_addiction_chart.png", dpi=300)
    plt.close()
except FileNotFoundError:
    print("Job 4 data not found")

