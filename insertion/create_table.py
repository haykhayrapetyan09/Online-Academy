from connect import ConnectionManager

def create_tables():
    fd = open('./recourses/create_table.sql', 'r')
    commands = fd.read()
    fd.close()
    connector.execute(commands)


if __name__ == '__main__':
    connector = ConnectionManager()
    create_tables()
    connector.close()
