from cassandra.cluster import Session
from cassandra.query import SimpleStatement
from typing import Union


class User:
    def __init__(self, **kwargs):
        self.user_id: int = kwargs.get('user_id')
        self.status: str = kwargs.get('status', 'active')


class UsersTable:
    """Users Table"""

    def __init__(self, session: Session) -> None:
        self.session = session
    
    def create(self) -> None:
        """Create the table"""
        query = \
        """
            CREATE TABLE IF NOT EXISTS users (
                user_id BIGINT PRIMARY KEY,
                balance INT,
                energy SMALLINT,
                squad BOOLEAN
            );
        """
        self.session.execute(query)
   
    def insert(self, user_id: int) -> None:
        """Insert a new user only if the user doesn't already exist"""

        query = \
        """
            INSERT INTO users (user_id, balance, squad)
            VALUES (%s, %s, %s)
            IF NOT EXISTS
        """
        self.session.execute(query, (user_id, 0, False))

    def update(self, user_id: int, status: str = None) -> None:
        """Update status by telegram ID"""
        
        query = \
        """
            UPDATE users
            SET status=%s
            WHERE user_id=%s
        """
        self.session.execute(query, (status, user_id))

    def delete(self, user_id: int) -> None:
        """Delete user by telegram ID"""
        
        query = \
        """
            DELETE FROM users
            WHERE user_id=%s
        """
        self.session.execute(query, (user_id,))

    def get(self, user_id: int) -> Union[User, None]:
        """Get a user by telegram ID"""

        query = \
        """
            SELECT * FROM users
            WHERE user_id=%s
        """
        result = self.session.execute(query, (user_id,))
        record = result.one()

        if not record:
            return None

        user = User(
            user_id=record.user_id,
            status=record.status
        )

        return user
