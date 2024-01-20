import numpy as py
import pandas as pd
import matplotlib.pyplot as plt

def calculate_demographic_data(print_data=True):
  # read data
  df = pd.read_csv('adult.data.csv')
  
  # how many of each race
  racecount = df['race'].value_counts()
  
  # average age of men
  avgmenage = round(df.loc[df['sex'] == 'Male']['age'].mean(),1)
  
  # bachelor percentage
  bachper = round(100*df.loc[df['education'] == 'Bachelors', 'education'].count()/df.shape[0],1)
  
  # with and without `Bachelors`, `Masters`, or `Doctorate`
  high_edu = df[df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]
  low_edu = df[~df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]
  
  # higher edu percentage with plus 50K sal
  high_edu_rich = round(100*high_edu.loc[high_edu['salary']=='>50K','education'].count()/high_edu.shape[0],1)
  
  # lower edu percentage with plus 50K sal
  low_edu_rich = round(100*low_edu.loc[low_edu['salary']=='>50K','education'].count()/low_edu.shape[0],1)
  
  # min hrs per week
  min_hrs = df['hours-per-week'].min()
  
  # min hrs and plus 50k sal
  num_minhrs = df.loc[df['hours-per-week']==min_hrs]
  
  minhrsplus50k = round(100*num_minhrs.loc[num_minhrs['salary'] == '>50k', 'education'].count()/num_minhrs.shape[0],1)
  
  # highest country with plus 50k sal 
  hec = (df[df['salary'] == '>50K']['native-country'].value_counts()/df['native-country'].value_counts()).sort_values(ascending=False).fillna(0)
  
  hec.idxmax()
  
  # highest country with plus 50k sal percentage
  hecper = round(len(df[(df['native-country'] == hec) & (df['salary'] == '>50K')]) / len(df[(df['native-country'] == hec)]) * 100,1)
  
  # most pop occ in Ind plus 50k sal
  topindocc = df[(df['salary'] == ">50K") & (df['native-country'] == "India")]["occupation"].value_counts().index[0]
  
  if print_data:
      print("Number of each race:\n", racecount) 
      print("Average age of men:", avgmenage)
      print(f"Percentage with Bachelors degrees: {bachper}%")
      print(f"Percentage with higher education that earn >50K: {high_edu_rich}%")
      print(f"Percentage without higher education that earn >50K: {low_edu_rich}%")
      print(f"Min work time: {min_hrs} hours/week")
      print(f"Percentage of rich among those who work fewest hours: {minhrsplus50k}%")
      print("Country with the highest percentage of rich:", hec)
      print(f"Highest percentage of rich people in the country: {hecper}%")
      print("Top occupations in India:", topindocc)
  
  return {
      'race_count': racecount,
      'average_men_age': avgmenage,
      'percentage_of_bachelors': bachper,
      'higher_education_rich': high_edu_rich,
      'lower_education_rich': low_edu_rich,
      'min_work_hours': min_hrs,
      'min_work_hours_&_>50k_sal': minhrsplus50k,
      'highest_earning_country': hec,
      'highest_earning_country_as_percentage': hecper,
      'top_India_occupation': topindocc
  }