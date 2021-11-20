from connect import ConnectionManager


def create_tables():
    print("Creating tables...")
    fd = open('../recourses/create_table.sql', 'r')
    commands = fd.read()
    fd.close()
    connector.execute(commands)

def create_procedeures():
    print("Creating procedures...")
    fd = open('../recourses/create_procedure.sql', 'r')
    commands = fd.read()
    fd.close()
    connector.execute(commands)


if __name__ == '__main__':
    connector = ConnectionManager()
    create_tables()
    create_procedeures()
    connector.close()
