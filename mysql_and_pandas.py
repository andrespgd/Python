import pandas as pd
import random


print('\n\n################### 1 - CREATE DATA AND DATAFRAMES  ###################') 

f_first_names = ['Mary', 'Julia', 'Sandy']
m_first_names = ['Andrew', 'Joe', 'Matt']

last_names = ['Smith', 'Roberts', 'Connor']

cities_lat_lon = [ \
['Crawfordsville',40.044075,-86.911057],
['Connersville',39.653687,-85.147896],
['Bloomington',39.168804,-86.536659],
['Bedford',38.866512,-86.511833],
]
    
# DF     
df_cities_lat_lon = pd.DataFrame(cities_lat_lon, columns=['city', 'latitude', 'longitude'])   

# Create random list of first, last, gender, cities
first_last_gender_age_cities_ref = []
cities_ref_cities_visited = []
#
for i in range(1_000_000):
    gender     = random.choice(['f', 'm'])
    first_name = random.choice(f_first_names) if gender=='f' else random.choice(m_first_names)
    last_name  = random.choice(last_names)
    age        = random.randint(18,80)
    cities_ref = i
    first_last_gender_age_cities_ref.append([first_name, last_name, gender, age, cities_ref])
    #
    for j in range(random.randint(1, 10)):
        cities_ref_cities_visited.append([cities_ref, random.choice(df_cities_lat_lon['city'])])
     
# DFs  
df_first_last_gender_age_cities_ref = pd.DataFrame(first_last_gender_age_cities_ref, columns=['first_name', 'last_name', 'gender', 'age', 'cities_ref'])
df_cities_ref_cities_visited        = pd.DataFrame(cities_ref_cities_visited, columns=['cities_ref', 'city'])


print('\n\n################### 2 - INSTALL MYSQL IN LINUX  ###################') 

'''
INSTALL MYSQL IN UBUNTU
sudo apt update
sudo apt upgrade
sudo apt install mysql-server

SECURE
sudo service mysql status
sudo mysql
>ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY 'SetRootPasswordHere';
sudo mysql_secure_installation

ADD ADMIN OR USER ACCOUNT
mysql -u root -p
>CREATE USER 'admin'@'localhost' IDENTIFIED BY 'setAdminOrUserPasswordHere';
>GRANT ALL PRIVILEGES ON *.* TO 'admin'@'localhost' WITH GRANT OPTION;
>FLUSH PRIVILEGES; 
>SHOW DATABASES;
>exit

ADD DATABASE
sudo mysql -u username\root -p
(Replace username\root with your username. )
>CREATE DATABASE travel;
>USE travel;
'''


print('\n\n####################  3 - PYMSQL - CHECK VERSION AND DATABASES  ###################') 

import pymysql

conn = pymysql.connect(host='localhost', user='admin', password = "setPasswordHere", db='travel',)
cur = conn.cursor()
#
cur.execute("select @@version")
print(cur.fetchall())
#
cur.execute("show databases")
print(cur.fetchall())
#
conn.close()



print('\n\n####################  4 - SQLALCHEMY - UPLOAD DATAFRAMES TO DATABASE  ###################') 

import sqlalchemy

engine = sqlalchemy.create_engine("mysql+pymysql://{user}:{pw}@localhost/{db}".format(user="admin",pw="setPasswordHere",db="travel"))
#
df_cities_lat_lon.to_sql('cities',                      con = engine,  chunksize = 1000,  index=False, index_label=None, if_exists='replace') # if_exists = 'append'
df_first_last_gender_age_cities_ref.to_sql('travelers', con = engine,  chunksize = 1000,  index=False, index_label=None, if_exists='replace') # if_exists = 'append'
df_cities_ref_cities_visited.to_sql('cities_visited',   con = engine,  chunksize = 1000,  index=False, index_label=None, if_exists='replace') # if_exists = 'append'



print('\n\n#################### 5 - CONNECT TO MYSQL USING PYMSQL - RUN A QUERY SEARCH  ###################') 

print('Connecting\n')
conn = pymysql.connect(host='localhost', user='admin', password = "setPasswordHere", db='travel',)
cur = conn.cursor()

#
query = "SELECT * from cities"
print('Running query:\n', query, '\n')
cur.execute(query)
result = cur.fetchall()
df1 = pd.DataFrame(list(result))

#
query = "SELECT * from travelers"
print('Running query:\n', query, '\n')
cur.execute(query)
result = cur.fetchall()
df2 = pd.DataFrame(list(result))

#
query = "SELECT * from cities_visited"
print('Running query:\n', query, '\n')
cur.execute(query)
result = cur.fetchall()
df3 = pd.DataFrame(list(result))

#
query = '''
SELECT * FROM travel.travelers
WHERE age < 30
'''
print('Running query:\n', query, '\n')
cur.execute(query)
result = cur.fetchall()
df4 = pd.DataFrame(list(result))

#
query = '''
SELECT *
FROM travel.travelers
INNER JOIN travel.cities_visited
ON travel.travelers.cities_ref = travel.cities_visited.cities_ref
'''
print('Running query:\n', query, '\n')
cur.execute(query)
result = cur.fetchall()
df5 = pd.DataFrame(list(result))

#
query = '''
	SELECT *
      FROM travel.travelers
INNER JOIN travel.cities_visited
        ON travel.travelers.cities_ref = travel.cities_visited.cities_ref
INNER JOIN travel.cities
		ON travel.cities_visited.city = travel.cities.city
'''
print('Running query:\n', query, '\n')
cur.execute(query)
result = cur.fetchall()
df6 = pd.DataFrame(list(result))

#
print('Closing connection')
conn.close()



print('\n\n####################  6 - INSTALL MYSQL WORKBENCH     ###################') 

# sudo snap install mysql-workbench-community



print('\n\n###################  7 - RUN MYSQL WORKBENCH  ###################') 

# sudo snap connect mysql-workbench-community:password-manager-service :password-manager-service
# mysql-workbench-community


