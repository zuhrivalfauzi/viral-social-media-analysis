import pandas as pd

file_path = 'Viral_Social_Media_Trends.csv'  
df = pd.read_csv(file_path, delimiter=';')  

df['Total_Engagement'] = df['Likes'] + df['Shares'] + df['Comments']

df.to_csv('cleaned_data.csv', index=False)

df.to_csv("final_data.csv", index=False)
print("✅ Data berhasil disimpan ke final_data.csv!")