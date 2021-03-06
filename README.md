# Log_Analysis_for_DDoS_Attacks
Detects DDoS attacked IPaddresses from the Log Data

# Introduction to DDoS Attacks
* DDoS attack is a special sort of cyber-crime which tries to make a service or a server unavailable. In order to do so attackers infect one or various computers with malware. The attackers use this infected computer network, known as botnet, to launch their DDoS attack. Using the botnet, they attack their target by sending a large number of requests to the infrastructure. 
* DDoS attack is an incredible amount of traffic sent to your server that means an IP address makes x requests over y seconds.

### In this project we are trying to find out if a range of IP addresses sends too many connection requests over a small window of time.

# Data Pipeline
![image](https://user-images.githubusercontent.com/10507993/57264698-0fadb580-7039-11e9-816a-e94039aceaf3.png)

# Data Ingestion - Workflow in Apache NiFi
![image](https://user-images.githubusercontent.com/10507993/57264776-7f23a500-7039-11e9-8a46-02053169c4cf.png)

* “**Tail File**” processor is used to tail a file, or multiple files, ingesting data from the file as it is written to the file. 
*	“**Replace Text**” Processor converting the log data into CSV.
*	“**PutHDFS**” Processor ingest data in HDFS.

# Detection of DDoS Attacks from logs	 
* Using PySpark program reading the HDFS file and Created DataFrame.
* Using SparkSQL detected the DDoS attacked Ipaddress in the log data.
* Extracted the attacked Ipaddress into a HDFS file.

