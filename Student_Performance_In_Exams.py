import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import hashlib


# # Load the data
df = pd.read_csv("StudentsPerformance.csv")

#Cleaning dataset
df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')
pridf = df.drop_duplicates()
df = df.drop_duplicates()


# Set clean visual style globally
sns.set_theme(style="whitegrid")

##################################################### TREND 1 #####################################################
grouped_scores = df.groupby('test_preparation_course')[['math_score', 'reading_score', 'writing_score']].mean()
print(grouped_scores)

grouped_scores.plot(
    kind='bar',
    figsize=(8, 6),
    color=['#5DADE2', "#BA65FF", "#FF38A5"]
)
plt.title("Average Exam Scores by Test Preparation Course Completion", fontsize=14, fontweight='bold')
plt.ylabel("Average Score")
plt.xlabel("Test Preparation Course")
plt.xticks(rotation=0)
plt.legend(title="Subject")
plt.tight_layout()
plt.show()

##################################################### TREND 2 #####################################################

reading = df["reading_score"]
writing = df["writing_score"]

plt.figure(figsize=(8, 6))
sns.scatterplot(x=reading, y=writing, color='#AF7AC5', edgecolor='black', alpha=0.7)
plt.title("Reading Score vs. Writing Score", fontsize=14, fontweight='bold')
plt.xlabel("Reading Score")
plt.ylabel("Writing Score")
plt.grid(True)
plt.tight_layout()
plt.show()

print(df["reading_score"].corr(df["writing_score"]))

##################################################### TREND 3 #####################################################

# A. Subject-specific averages by education level
parental_education = df.groupby("parental_level_of_education")[['math_score', 'reading_score', 'writing_score']].mean()
parental_education.plot(
    kind='bar',
    figsize=(10, 6),
    color=['#F1948A', '#85C1E9', '#F7DC6F']
)
plt.title("Average Subject Scores by Parental Level of Education", fontsize=14, fontweight='bold')
plt.ylabel("Average Score")
plt.xlabel("Parental Level of Education")
plt.xticks(rotation=45)
plt.legend(title="Subject")
plt.tight_layout()
plt.show()

# B. Overall average score by education level
df['average_score'] = df[['math_score', 'reading_score', 'writing_score']].mean(axis=1)
avg_by_education = df.groupby('parental_level_of_education')['average_score'].mean()

avg_by_education.plot(
    kind='bar',
    color="#FF82FF",
    figsize=(8, 6)
)
plt.title("Average Total Score by Parental Education Level", fontsize=14, fontweight='bold')
plt.ylabel("Average Total Score")
plt.xlabel("Parental Level of Education")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


##################################################### Encryption #####################################################
#Example: encrypting a 'student_id' column
def encrypt_value(val):
    return hashlib.sha256(str(val).encode()).hexdigest()

# Apply to a column
df['student_id_encrypted'] = df['student_id'].apply(encrypt_value)

# (Optional) drop original column if needed
df.drop('student_id', axis=1, inplace=True)
