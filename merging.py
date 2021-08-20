import pandas as pd 
import csv

df = pd.read_csv("brown_dwarf_stars.csv")

df = df[df["name"].notna()]
df = df[df["distance"].notna()]
df = df[df["mass"].notna()]
df = df[df["radius"].notna()]
# df['mass']=df['mass'].apply(lambda x: x.replace('$', '').replace(',', '')).astype('float')
df["radius"] = 0.102763*df["radius"]
df["mass"] = 0.000954588*df["mass"]

df1=df.to_csv("main.csv")
#print(df)
dataf = []
with open("main.csv","r") as f:
    csvreader = csv.reader(f)
    for row in csvreader:
        dataf.append(row)
h=dataf[0]
m_r=dataf[1:]
print(h)
# for ninja in m_r:
    
#     if(ninja[5].notna()):
#         print("yes .notna()")
#     ninja[4] = float(ninja[4])*0.000954588
#     ninja[5] = float(ninja[5])*0.102763


with open("final.csv","w") as f:
    csvwriter = csv.writer(f)
    csvwriter.writerow(h)
    csvwriter.writerows(m_r)
dataf2=[]
with open("bright_stars.csv", "r") as f:
    csvreader = csv.reader(f)
    for row in csvreader: 
        dataf2.append(row)

headers_1 = dataf[0]
planet_data_1 = dataf[1:]

headers_2 = dataf2[0]
planet_data_2 = dataf2[1:]

headers = headers_1 + headers_2
planet_data = []

# for index, data_row in enumerate(planet_data_1):
#     planet_data.append(planet_data_1[index] + planet_data_2[index])

for dialga in planet_data_1:
    planet_data.append(dialga)
for palkia in planet_data_2:
    planet_data.append(palkia)


with open("final1.csv", "a+") as f:
    csvwriter = csv.writer(f)
    csvwriter.writerow(headers)
    csvwriter.writerows(planet_data)
