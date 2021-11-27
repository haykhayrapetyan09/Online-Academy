from connect import ConnectionManager


def create_tables():
    print("Creating tables...")
    with open('../recourses/create_table.sql', 'r') as file:
        commands = file.read()
    connector.execute(commands)


def create_procedures():
    print("Creating procedures...")
    with open('../recourses/create_procedure.sql', 'r') as file:
        commands = file.read()
    connector.execute(commands)


if __name__ == '__main__':
    connector = ConnectionManager()
    create_tables()
    create_procedures()
    connector.close()
