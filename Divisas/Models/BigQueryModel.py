# -*- coding: utf-8 -*-

__all__ = ['BigQueryData']

# google cloud library
from google.cloud import bigquery

# errors local library
from Errors.IncorrectRequest import body_error

# local variables
BQ = bigquery.Client()

class BigQueryData():
    """Extract data from Bigquery

    Args:

        year (int): Year request YYYY

        months (str): Months request to get data MM,MM,MM,...,MM

    Returns:
        data (list): Information already structured

    """

    def __init__(self, year, months):
        self.year = year
        self.months = months
        self.query = self.get_query()

    def get_query(self):
        self.query = f"""
                    SELECT 
                        EXTRACT(MONTH FROM date ) as month,
                        EXTRACT(DAY FROM date ) as day,
                        dato,
                        currency
                    FROM `taco-tech.Cumplo.RegistryDaily` 
                    WHERE 
                        EXTRACT(MONTH FROM date ) in ({self.months})
                        AND EXTRACT(YEAR FROM date ) in ({self.year})
                    ORDER BY month, day
                """
        return self.query
    
    def exec_query(self):
        try:
            data = BQ.query(self.query)

            buffer = []

            for item in data:
                aux = {}
                aux['mes'] = item[0]
                aux['dia'] = item[1]
                aux['pesos'] = round(item[2], 2)
                aux['divisa'] = item[3]
                buffer.append(aux)
            return buffer
        
        except:
            return body_error("Error al consultar infromacion")

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

        table = BQ.create_table(table)

        print(
            "Created table {}, partitioned on column {}".format(
                table.table_id, table.time_partitioning.field
            )
        )

"""
if __name__ == "__main__":
    app = BigQueryConfiguration()
    app.create_table('RegistryDaily')
"""