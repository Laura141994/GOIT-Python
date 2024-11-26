import pandas as pd
file_path= r"C:\Users\Apetrei\Documents\Python\facebook_ads_data.csv"
df=pd.read_csv(file_path)
import matplotlib.pyplot as plt

#Cerinta 1 - Grupează datele după zile și creează două grafice pentru datele grupate:
                  # Un grafic cu suma totală a cheltuielilor publicitare în anul 2021;
                  # Un grafic cu ROMI-ul zilnic în anul 2021.

# Convertim coloana 'ad_date' la format datetime
df['ad_date'] = pd.to_datetime(df['ad_date'])

# Filtrăm datele pentru anul 2021
data_2021 = df[df['ad_date'].dt.year == 2021]

# Grupăm datele după zile și calculăm suma cheltuielilor și valorile medii pentru ROMI
grouped_2021 = data_2021.groupby('ad_date').agg({
    'total_spend': 'sum',  # Suma cheltuielilor totale
    'romi': 'mean'         # Media ROMI
}).reset_index()

# Graficul 1: Suma totală a cheltuielilor publicitare în 2021
plt.figure(figsize=(12, 6))
plt.bar(grouped_2021['ad_date'], grouped_2021['total_spend'], color='teal')
plt.title('Suma totală a cheltuielilor publicitare în 2021', fontsize=16)
plt.xlabel('Ziua', fontsize=12)
plt.ylabel('Cheltuieli totale (USD)', fontsize=12)
plt.xticks(ticks=grouped_2021['ad_date'][::30], labels=grouped_2021['ad_date'][::30].dt.strftime('%Y-%m-%d'), rotation=45)
plt.tight_layout()
plt.show()

#  Graficul 2: ROMI zilnic în 2021
plt.figure(figsize=(12, 6))
plt.plot(grouped_2021['ad_date'], grouped_2021['romi'], marker='o', linestyle='-', color='blue')
plt.axhline(0, color='red', linestyle='--', linewidth=1, label='Pragul de referință ROMI=0')
plt.title('ROMI zilnic în 2021', fontsize=16)
plt.xlabel('Ziua', fontsize=12)
plt.ylabel('ROMI', fontsize=12)
plt.xticks(ticks=grouped_2021['ad_date'][::30], labels=grouped_2021['ad_date'][::30].dt.strftime('%Y-%m-%d'), rotation=45)
plt.legend()
plt.tight_layout()
plt.show()

#  Cerinta 2: Grupează datele după numele campaniei și creează două grafice:
                   # Un grafic cu suma totală a cheltuielilor publicitare pentru fiecare campanie;
                  # Un grafic cu ROMI-ul total pentru fiecare campanie.

#  Grupăm datele după numele campanie
group_by_campaign=df.groupby("campaign_name").agg({"total_spend":"sum","romi": "sum"}).reset_index()

#  Graficul 1: Suma totală a cheltuielilor publicitare pe campanie
plt.bar(group_by_campaign["campaign_name"],group_by_campaign["total_spend"],color="red")
plt.title("Suma totală a cheltuielilor publicitare pentru fiecare campanie")
plt.xlabel("Campanie")
plt.ylabel("Cheltuieli totale")
plt.xticks(rotation=45)
plt.show()

# Grafic 2: Total Romi per campaign
plt.bar(group_by_campaign["campaign_name"],group_by_campaign["romi"],color="olive")
plt.title("ROMI-ul total pentru fiecare campanie")
plt.xlabel("Campanie")
plt.ylabel("Romi")
plt.xticks(rotation=50)
plt.show()

# Cerinta 3: Utilizând un box plot, determină distribuția ROMI-ului zilnic în fiecare campanie (după numele campaniei).
import seaborn as sns
sns.boxplot(x="campaign_name", y="romi",data=df)
plt.title('Distribuția ROMI-ului zilnic în fiecare campanie')
plt.xlabel('Campanie')
plt.ylabel('ROMI')
plt.xticks(rotation=50)
plt.show()

# Cerinta 4 : Creează o histogramă cu distribuția valorilor ROMI din tabelul facebook_ads_data.csv.
plt.hist(df["romi"], color="blue")
plt.title('Distribuția valorilor ROMI')
plt.xlabel('ROMI')
plt.ylabel('Frecvență')
plt.grid(False)
plt.show()

# Cerinta 5:Creează un heat map a corelației între toți indicatorii numerici din tabelul facebook_ads_data.csv. Care indicatori au cea mai mare și cea mai mică corelație? Cu ce corelează “total_value”?
coloane_numerice = df.select_dtypes(include=['number']).columns
datafr_numeric = df[coloane_numerice]
correlation_matrix = datafr_numeric.corr()
print(correlation_matrix)
max_correlation = correlation_matrix.max().max()
max_correlation_indicators = correlation_matrix[correlation_matrix == max_correlation].stack().index.tolist()
min_correlation = correlation_matrix.min().min()
min_correlation_indicators = correlation_matrix[correlation_matrix == min_correlation].stack().index.tolist()
print("Cea mai mare corelație:")
for indicator_pair in max_correlation_indicators:
    print(f"- {indicator_pair[0]} și {indicator_pair[1]}: {max_correlation}")

print("\nCea mai mică corelație:")
for indicator_pair in min_correlation_indicators:
    print(f"- {indicator_pair[0]} și {indicator_pair[1]}: {min_correlation}")

total_value_correlation = correlation_matrix['total_value'].drop('total_value')
print("\nCorelația indicatorului 'total_value' cu ceilalți indicatori:")
print(total_value_correlation)

sns.heatmap(correlation_matrix, cmap = 'viridis', annot= True)
plt.title('Heat Map al Corelației între Indicatorii Numerici')
plt.show()

#Cerinta 6 :Creează un grafic cu puncte cu regresie liniară (poți folosi funcția lmplot()), pe baza datelor din “total_spend” și “total_value” pentru a vizualiza relația dintre aceste variabile.
sns.lmplot(x='total_spend', y='total_value', data=df, hue = 'campaign_name', palette='husl', markers = '^')
plt.title('Relația dintre total_spend și total_value')
plt.xlabel('Total Spend')
plt.ylabel('Total Value')
plt.grid(False)
plt.xticks(rotation=50)
plt.show()