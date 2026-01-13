import pandas as pd
import matplotlib.pyplot as plt 
import numpy as np
import seaborn as sns

file = input("Enter CSV file name: ")
try:
    df = pd.read_csv(file)
    print(" Data loaded successfully!")
except Exception as e:
    print("Error loading file!")
    print("Error details:", e)

def calculate(df):
    if df is None:
        print("Data not found")
        return
    
most_borrowed = df['Book Title'].mode()[0]
Avg_duration = df['Borrowing Duration (Days)'].mean()
Busy_day = df['Borrowing Duration (Days)'].max()

print(most_borrowed)
print(Avg_duration)
print(Busy_day)

calculate(df)

def filter_transactions(df, condition):
    if df is None:
        print("No Data.")
        return
    
    try:
        result = df.query(condition)
        print(result)
    except Exception as e:
        print("invalid result.",e)

filter_transactions(df, 'Genre == "Fantasy"')

def generate_report(df):
    if df is None:
        print("Invalid Report.")
        return
    
total = len(df)
users = df['User ID'].unique()
books = df['Book Title'].nunique()
avg_days = round(df['Borrowing Duration (Days)'].mean())

print(total)
print(users)
print(books)
print(avg_days)

durations = df['Borrowing Duration (Days)'].dropna().to_numpy()
print(np.min(durations))
print(np.max(durations))
print(np.mean(durations))
print(np.std(durations))

print(df.groupby('Genre')['Transaction ID'].count())
print(df.groupby('Genre')['Borrowing Duration (Days)'].mean())

print("Missing values:\n", df.isnull().sum())
df = df.drop_duplicates()
print(df)

top_books = df['Book Title'].value_counts().head(5)
top_books.plot(kind='bar', color='skyblue')
plt.title("Top 5 Most Borrowed Books")
plt.xlabel("Book Title")
plt.ylabel("Borrow Count")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

df['Month'] = pd.to_datetime(df['Date']).dt.to_period('M')
monthly_trend = df.groupby('Month').size()
monthly_trend.plot(kind='line', marker='o')
plt.title("Monthly Borrowing Trend")
plt.xlabel("Month")
plt.ylabel("Transactions")
plt.grid(True)
plt.show()

genre_counts = df['Genre'].value_counts()
genre_counts.plot(kind='pie', autopct='%1.1f%%', startangle=90)
plt.title("Genre Distribution")
plt.ylabel("")  
plt.show()
    
df['Day'] = pd.to_datetime(df['Date']).dt.day_name()
df['Hour'] = pd.to_datetime(df['Date']).dt.hour
heatmap_data = df.groupby(['Day', 'Hour']).size().unstack(fill_value=0)

sns.heatmap(heatmap_data, cmap='YlGnBu')
plt.title("Borrowing Activity by Day & Hour")
plt.show()