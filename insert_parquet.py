import pyarrow as pa
import pyarrow.parquet as pq
from connect import ConnectionManager


def write_parquet(table_name, last_ran):
    print("Writing parquet file:", table_name+'.parquet')
    table_column_names = connector.get_column_names(table_name)

    clause = "WHERE creation_date > '%s'" % last_ran
    rows_list = connector.get_columns(
        "*",
        table_name,
        condition=clause
    )

    length = len(rows_list)
    if length == 0:
        print("There is no rows.")
        return 0

    rotated = list(zip(*rows_list))
    table = pa.table(rotated, names=table_column_names)
    pq.write_table(table, table_name + '.parquet')


def read_parquet(file_name):
    print("Reading parquet file:", file_name+'.parquet')
    reloaded_table = pq.read_table(file_name + '.parquet').to_pandas()
    print(reloaded_table.head())


if __name__ == '__main__':
    connector = ConnectionManager(configpath="config/database.ini")
    write_parquet("assistant", "2021-12-19")
    read_parquet("assistant")
    connector.close()
