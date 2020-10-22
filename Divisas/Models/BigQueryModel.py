# -*- coding: utf-8 -*-

# standard library
from google.cloud import bigquery

# local variables
CS = bigquery.Client()

class BigQueryConfiguration():

    def create_table(self, table):
        dataset_ref = bigquery.DatasetReference('taco-tech', 'Cumplo')
        table_ref = dataset_ref.table(table)

        schema = [
            bigquery.SchemaField("date", "DATE"),
            bigquery.SchemaField("idSerie", "STRING"),
            bigquery.SchemaField("dato", "FLOAT"),
            bigquery.SchemaField("currency", "STRING"),
        ]

        table = bigquery.Table(table_ref, schema=schema)

        table.time_partitioning = bigquery.TimePartitioning(
            type_=bigquery.TimePartitioningType.DAY,
            field="date",  # name of column to use for partitioning
        ) 

        table = CS.create_table(table)

        print(
            "Created table {}, partitioned on column {}".format(
                table.table_id, table.time_partitioning.field
            )
        )

if __name__ == "__main__":
    app = BigQueryConfiguration()
    app.create_table('RegistryDaily')