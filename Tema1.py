import pandas as pd
#Calea catre fisier
file_path = r"C:\Users\Apetrei\Documents\Python\survey_results_public.csv"
#Importa fisierul csv
df=pd.read_csv(file_path)
#Verifica datele
print(df.head())
print(df.info())
print(".....................")

# 1.Câți respondenți au completat sondajul?
response_number=df["ResponseId"].nunique()
print(f"Numarul total de respondenti este {response_number}")
print("...................")

# 2.Câți respondenți au răspuns la toate întrebările?
respondenti_completi=df.dropna().shape[0] #Determină numărul de respondenți care au răspuns la toate întrebările
print(f"Numărul de respondenți care au răspuns la toate întrebările este: {respondenti_completi}")
print(".........................")

# 3.Care sunt valorile măsurilor de tendință centrală pentru experiența respondenților (WorkExp)?
work_exp = df['WorkExp'].dropna() #Eliminam valorile lipsa
media = work_exp.mean()
mediana = work_exp.median()
mod = work_exp.mode().iloc[0] if not work_exp.mode().empty else None
print(f"Media experienței: {media:.2f} ani")
print(f"Mediana experienței: {mediana} ani")
print(f"Modul experienței: {mod} ani")
print(".............................")

# 4.Câți respondenți lucrează de la distanță?
remote = df.loc[df["RemoteWork"]=="Remote"].shape[0]
print(f"Numarul de respondenti ce lucreaza de acasa este {remote}")
print("...........................")

# 5.Ce procent de respondenți programează în Python?
total_respondents = df.shape[0]
python_r=df["LanguageHaveWorkedWith"].dropna().str.contains("Python").sum() # Numărăm respondenții care menționează Python
python_percentage = (python_r / total_respondents) * 100
print(f"Procentul respondenților care programează în Python este: {python_percentage:.2f}%")
print("............................")

# 6.Câți respondenți au învățat să programeze prin cursuri online?
online_learners = df[df['LearnCodeOnline'].notna()]
online_learners_count = df['LearnCodeOnline'].notna().sum()
print(f"Numarul respondentilor care au invatat sa programeze online este {online_learners_count}")
print("...........................")

# 7.Dintre respondenții care programează în Python, grupați pe țări, care este valoarea medie și mediană a remunerației (ConvertedCompYearly) în fiecare țară?
# Filtrăm respondenții care programează în Python
python_respondents = df[df["LanguageHaveWorkedWith"].str.contains("Python", case=False, na=False)]
# Calculăm valoarea medie și mediană a remunerației, grupate pe țară
salary_stats = python_respondents.groupby("Country")["ConvertedCompYearly"].agg(["mean", "median"])
print(salary_stats) 
print(".......................................")

# 8.Ce nivel de educație au cei 5 respondenți cu cea mai mare compensație?
# Sortăm dataframe-ul după compensația anuală (în ordine descrescătoare)
top_5_respondents = df.sort_values(by='ConvertedCompYearly', ascending=False).head(5)
# Afișăm nivelul de educație pentru acești 5 respondenți
education_levels = top_5_respondents[['ConvertedCompYearly', 'EdLevel']]
print(f"Nivelul de educatie a celor 5 respondenti este {education_levels}")