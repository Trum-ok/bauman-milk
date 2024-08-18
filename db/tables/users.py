from asyncpg import Pool
from typing import Union


class User:
    def __init__(self, **kwargs):
        self.tg_id: int = kwargs.get('tg_id')
        self.status: str = kwargs.get('status', 'active')


class UsersTable:
    """Users Table"""

    def __init__(self, pool: Pool) -> None:
        self.pool = pool
    
    async def create(self) -> None:
        """Create the table"""
        await self.pool.execute(
            """
            CREATE TABLE IF NOT EXISTS users (
                tg_id INT PRIMARY KEY,
                status TEXT DEFAULT 'active'
            )
            """)

   
    async def insert(self, 
                     tg_id: int, 
                    ) -> None:
        """Insert a new account"""
        await self.pool.execute(
            """
            INSERT INTO users ($1)
            """,
            tg_id
        )


    async def update(self, 
                     tg_id: int,
                     status: str = None,
                    ) -> None:
        """Обновление статуса по telegram ID"""
        
        query = f"""
            UPDATE users
            SET status={status}
            WHERE tg_id={tg_id}
        """
        await self.pool.execute(query)


    async def delete(self, 
                     tg_id: int, 
                    ) -> None:
        query = f"""
            DELETE FROM users
            WHERE tg_id={tg_id}
        """

        await self.pool.execute(query)

    
    async def get(self,
                tg_id: int,
                ) -> Union[User, None]:
        """Получить аккаунт по telegram ID"""

        query = f"""
            SELECT *
            FROM users
            WHERE tg_id={tg_id}
            """

        record = await self.pool.fetchrow(query)
        
        if not record:
            return None

        user = User(
            id=record["id"],
            email=record["email"],
            password=record["password"],
            tg=record["tg"],
            chats=record["chats"],
            status=record["status"]
        )

        return user
