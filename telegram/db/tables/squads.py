from asyncpg import Pool
from typing import Union


class SquadsTable:
    """Squads Table"""

    def __init__(self, pool: Pool) -> None:
        self.pool = pool
    
    async def create(self) -> None:
        """Create the table"""
        await self.pool.execute(
            """
            CREATE TABLE IF NOT EXISTS squads (
                squad_id SERIAL PRIMARY KEY,
                name VARCHAR(16) NOT NULL,
                users INT[] NOT NULL,
                avatar_url TEXT
            )
            """)

   
    async def insert(self, 
                     tg_id: int, 
                    ) -> None:
        """Insert a new squad"""

        query = f"""
            INSERT INTO users (tg_id) VALUES ({tg_id})
        """
        await self.pool.execute(query)
