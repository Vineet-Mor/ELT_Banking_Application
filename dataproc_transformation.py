from pyspark.sql import SparkSession

def transform_data():
    spark = SparkSession.builder \
        .appName('Dataproc Transformation') \
        .getOrCreate()

    # Read data from BigQuery
    staging_table = 'quixotic-treat-419302.transactions.credit'
    df = spark.read.format('bigquery').option('table', staging_table).load()

    # Perform transformations
    transformed_df = df.withColumn('new_column', df['existing_column'] * 2)
    
    # Write transformed data back to BigQuery
    transformed_table = 'quixotic-treat-419302.transactions.credit'
    transformed_df.write.format('bigquery').option('table', transformed_table).mode('overwrite').save()

    spark.stop()

if __name__ == "__main__":
    transform_data()
