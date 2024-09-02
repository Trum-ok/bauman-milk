from asyncpg import Pool
from typing import Union


class CoinsTable:
    """Coins Table"""

    def __init__(self, pool: Pool) -> None:
        self.pool = pool
    
    async def create(self) -> None:
        """Create the table"""
        await self.pool.execute(
            """
            CREATE TABLE IF NOT EXISTS coins (
                tg_id INT PRIMARY KEY,
                coins INT DEFAULT 0,
                energy INT DEFAULT 2000
            )
            """)

   
    async def insert(self, 
                     tg_id: int, 
                    ) -> None:
        """Insert a new account"""

        query = f"""
            INSERT INTO users (tg_id) VALUES ({tg_id})
        """
        await self.pool.execute(query)
