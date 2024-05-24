from data.Database import Database

class UserRepository(Database):
    def __init__(self):
        Database.__init__(self, 'localhost', 'root', "VannyLamorte25!", 'manageo')
        self.connect()

    def check_credentials(self, email, password):
        sql = "SELECT * FROM user WHERE email = %s AND password = %s"
        values = (email, password)
        user = self.fetch_one(sql, values)
        return user is not None

    def get_user(self, email, password):
        sql = "SELECT * FROM user WHERE email = %s AND password = %s"
        values = (email, password)
        user = self.fetch_one(sql, values)
        return user
    
    def add_user(self, first_name, last_name, email, password):
        sql = "INSERT INTO user (first_name, last_name, email, password) VALUES (%s, %s, %s, %s)"
        values = ( first_name, last_name, email, password)
        self.execute_query(sql, values)

    def user_info(self):
        sql = "SELECT * user"
        return self.fetch(sql)

    def first_name_user(self):
        sql = "SELECT first_name FROM user"
        return self.fetch(sql)

    def last_name_user(self):
        sql = "SELECT last_name FROM user"
        return self.fetch(sql)
    
    def update_user(self, id, first_name, last_name, email):
        sql = 'UPDATE user SET first_name = %s, last_name = %s, email = %s WHERE id = %s'
        params = (first_name, last_name, email, id)
        self.execute_query(sql, params)

    def first_name_user(self):
        sql = "SELECT first_name FROM user"
        return self.fetch(sql)