# Большая просьба не сильно ругать за этот код, так как я до этого вообще ни разу не слышал про pyspark ^_^

from pyspark.sql import SparkSession
from pyspark.sql.functions import col

def get_product_category_pairs_with_uncategorized_products(df):
    product_category_pairs = df.select("Product", "Category")

    uncategorized_products = df.filter(col("Category").isNull()).select("Product").distinct()

    result_df = product_category_pairs.union(uncategorized_products.withColumn("Category", col("Product")))

    return result_df

def main():
    spark = SparkSession.builder.appName("ProductCategory").config("#", "#").getOrCreate()

    database_url = "#"
    table_name = "pyspark.sql.DataFrame"
    properties = {
        "user": "#",
        "password": "#",
        "driver": "#.postgresql.#"
    }

    df = spark.read.jdbc(url=database_url, table=table_name, properties=properties)

    df.printSchema()

    df.show() 

if __name__ == "__main__":
    main()
