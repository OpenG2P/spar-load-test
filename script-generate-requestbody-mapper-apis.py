import psycopg2
from psycopg2 import sql
import json
from datetime import datetime


def fetch_and_save_to_file(table_name, column_name, output_file):
    dbname = "spardb"
    user = "postgres"
    password = "c8HyT30ME0"
    host = "loadtest.openg2p.net"
    port = "5432"

    # Establish a connection to the PostgreSQL database
    connection = psycopg2.connect(
        dbname=dbname, user=user, password=password, host=host, port=port
    )
    cursor = connection.cursor()

    try:
        query = sql.SQL("SELECT {} FROM {}").format(
            sql.Identifier(column_name),
            sql.Identifier(table_name)
        )
        cursor.execute(query)
        rows = cursor.fetchall()
        json_data_list = []

        for row in rows:
            id_value = row[0]
            json_data = {
                "reference_id": "string",
                "timestamp": datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%S.%f")[:-3]
                + "Z",
                "additional_info": [
                    {
                        "name": "string",
                        "value": 0,
                    }
                ],
                "locale": "eng",
                "fa": "",
                "id": id_value,
                "name": "string",
                "scope": "details",
            }
            json_data_list.append(json_data)
        with open(output_file, "w") as file:
            json.dump(json_data_list, file, indent=2)

        print(f"Data saved to {output_file}")

    except Exception as e:
        print("Error: ", e)

    finally:
        cursor.close()
        connection.close()


if __name__ == "__main__":
    table_name = "id_fa_mappings"
    column_name = "id_value"
    output_file = 'output.json'
    fetch_and_save_to_file(table_name, column_name, output_file)
