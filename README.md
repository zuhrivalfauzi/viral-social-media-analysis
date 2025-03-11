# PostgreSQL-Portofolio

Welcome to my Data Engineer Portfolio! I am a data engineer with experience in building, managing, and optimizing data infrastructure. I am proficient in various technologies such as Python, SQL (PostgreSQL), BigQuery, Apache Spark, Airflow, and visualization tools like Power BI and Looker Studio.

This repository showcases my skills and projects that I have worked on during my studies and professional experience using PostgreSQL.

# Objectives
- Apply data normalization techniques
- Design ERD based on real-world problems
- Create and manage databases in PostgreSQL (DDL)
- Perform data ingestion and transformation (DML)

# Dataset Information
The dataset used in this project is available in the repository as movies.csv. Below is the column information:

|Column|Data Type|
|---|---|
|Post_ID|VARCHAR|
|Platform|VARCHAR|
|Hastag|VARCHAR|
|Content_Type|VARCHAR|
|Region|VARCHAR|
|Views|INT|
|Likes|INT|
|Shares|INT|
|Comments|INT|
|Engagement_Level|VARCHAR|


# Case Study
As a Data Engineer, you are responsible for managing movie data for a streaming service provider. The tasks include:

# 1. Database Structure
```sql
CREATE TABLE Viral_Social_Media_Trends (
    Post_ID VARCHAR(20) PRIMARY KEY,
    Platform VARCHAR(20),
    Hashtag VARCHAR(50),
    Content_Type VARCHAR(20),
    Region VARCHAR(30),
    Views INT,
    Likes INT,
    Shares INT,
    Comments INT,
    Engagement_Level VARCHAR(10)
);
```

# 2. Data Cleaning
Before analyzing the data, it was cleaned using SQL queries:
- Removing duplicates
```sql
DELETE FROM Viral_Social_Media_Trends
WHERE Post_ID IN (
    SELECT Post_ID FROM (
        SELECT Post_ID, ROW_NUMBER() OVER(PARTITION BY Platform, Hashtag, Views ORDER BY Post_ID) AS row_num
        FROM Viral_Social_Media_Trends
    ) temp
    WHERE row_num > 1
);
```
- Filtering out negative values
```sql
DELETE FROM Viral_Social_Media_Trends
WHERE Views < 0 OR Likes < 0 OR Shares < 0 OR Comments < 0;
```

# 3. Data Analysis Quiries
Here are some insights obtained from the data:

## 📌 Top Platforms with the Highest Engagement rates
```sql
SELECT Platform, 
       AVG((Likes + Shares + Comments) * 1.0 / Views) AS avg_engagement_rate
FROM Viral_Social_Media_Trends
WHERE Views > 0
GROUP BY Platform
ORDER BY avg_engagement_rate DESC;
```
![image](https://github.com/user-attachments/assets/2af25806-63c5-4498-96a0-3c47a8790dff)

## 📌 Top 5 Most Used Hashtags
```sql
SELECT Hashtag, COUNT(*) AS TotalPosts
FROM Viral_Social_Media_Trends
WHERE Hashtag IS NOT NULL
GROUP BY Hashtag
ORDER BY TotalPosts DESC
LIMIT 5;
```
![image](https://github.com/user-attachments/assets/ce140cc0-8ab7-4050-b04f-fb5b76e68f39)

## 📌 Engagement Performance by Region
```sql
SELECT Region, 
       SUM(Likes) AS TotalLikes, 
       SUM(Shares) AS TotalShares, 
       SUM(Comments) AS TotalComments
FROM Viral_Social_Media_Trends
GROUP BY Region
ORDER BY TotalLikes DESC;
```
![image](https://github.com/user-attachments/assets/4a57f2f9-28fd-48cb-a977-3edd6e078451)


