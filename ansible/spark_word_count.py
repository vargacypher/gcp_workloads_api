import sys
from pyspark.sql import SparkSession

PROJECT_ID = sys.argv[1]

spark = SparkSession \
  .builder \
  .master('yarn') \
  .appName('spark-bigquery-demo') \
  .getOrCreate()

# Use the Cloud Storage bucket for temporary BigQuery export data used
# by the connector.
bucket = "test_spk"
spark.conf.set('temporaryGcsBucket', bucket)

words = spark.read.format('bigquery') \
  .option('table', 'bigquery-public-data:samples.shakespeare') \
  .load()
words.createOrReplaceTempView('words')

word_count = spark.sql(
    'SELECT word, SUM(word_count) AS word_count FROM words GROUP BY word')
word_count.show()
word_count.printSchema()

word_count.write.format('bigquery') \
  .option("parentProject", PROJECT_ID)  \
  .option('table', 'wordcount_dataset.wordcount_output') \
  .mode("overwrite") \
  .save()

spark.stop()
