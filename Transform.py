from pyspark.sql import SparkSession
import get_weather

def Transform(list_files):
    spark = SparkSession.builder.master("local").appName("parquet_example").getOrCreate()
    for i in list_files:
        df = spark.read.options(inferSchema='True',delimiter=',').csv(i)
        df.write.mode('Overwrite').parquet(i.split('raw')[0]+"converted"+i.split('raw')[1].split(".csv")[0]+".parquet")
        df.write.mode('Overwrite').json(i.split('raw')[0]+"converted"+i.split('raw')[1].split(".csv")[0]+".json")
        
        year=i.split(".csv")[0].split("tripdata_")[1].split("-")[0]
        month=i.split(".csv")[0].split("tripdata_")[1].split("-")[0]
        get_weather.get_weather(year,month)
        
        
    


