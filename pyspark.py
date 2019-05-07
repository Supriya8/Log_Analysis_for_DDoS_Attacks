#spark-submit --packages com.databricks:spark-csv_2.10:1.4.0 pyspark2.py
from pyspark.sql import SQLContext
from pyspark import SparkConf, SparkContext
from pyspark.sql.types import *

#Creating SparkContext and Sql context
sc = SparkContext()
sqlContext = SQLContext(sc)

#Defining custom schema 
customSchema = StructType([ \
    StructField("ipaddress", StringType(), True), \
    StructField("timestamp", StringType(), True), \
    StructField("blank", StringType(), True)])
    
#Creating DataFrame using a csv file
df = sqlContext.read.format('com.databricks.spark.csv').options(header='false', delimiter=',').load('/user/app_svc_cdaingest_d/test/', schema = customSchema)
df.registerTempTable("stage_Table")

#Query to detect the DDoS attack IPaddresses.
sqlDF = sqlContext.sql("SELECT  ipaddress FROM stage_Table GROUP BY ipaddress,substring (timestamp,0,17) having COUNT(ipaddress) > 85")

#Save the output to a file in HDFS.
sqlDF.coalesce(1).write.save(path='/user/app_svc_cdaingest_d/test/output', format='csv')
