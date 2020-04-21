import psycopg2
import csv
#This connects python to the users ssh pathway.
try:
    connection = psycopg2.connect(user = "parkch",
                                  password = "",
                                  host = "localhost",
                                  port = "5432",
                                  database = "parkch")

    cursor = connection.cursor()
    # Print PostgreSQL Connection properties
    print ( connection.get_dsn_parameters(),"\n")
    #This code is our query and it calls for the parks with the same name in both data sets, while accessing their abundance, latitude, longitude, and acres.
    query_code = "SELECT species_id, category, parks.Park_name, abundance, lattitude, longitude, acres FROM flora_fauna4, parks where parks.park_name = flora_fauna4.Park_name;"
    #This executs the query code and runs it into a new csv.
    cursor.execute(query_code)
    
    data = cursor.fetchall()
    # Print PostgreSQL version
    
    #This code opens our csv we made and runs the query and writes all the data our query produces into our csv.
    
    with open("DSProj.csv",'w') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(data)
        
        

    
   
    
except (Exception, psycopg2.Error) as error :
    print ("Error while connecting to PostgreSQL", error)

            


#write out to csv

#for item in category:
#      select
        
##outfile.close()
#finally:
    #closing database connection.
#if(connection):
           # cursor.close()
           # connection.close()
   # print("PostgreSQL connection is closed")
