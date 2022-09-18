from databricks import sql
import os

with sql.connect(server_hostname = os.getenv("DATABRICKS_SERVER_HOSTNAME"),
                 http_path       = os.getenv("DATABRICKS_HTTP_PATH"),
                 access_token    = os.getenv("DATABRICKS_TOKEN")) as connection:

  with connection.cursor() as cursor:
    cursor.execute("SELECT * FROM default.co2_emission_by_countries_csv LIMIT 2")
    result = cursor.fetchall()

    for row in result:
      print(row)