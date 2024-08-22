import asyncpg
import db.tables as tables


class Database:
    def __init__(self, pool: asyncpg.Pool):
        self.pool = pool
        self.users = tables.UsersTable(self.pool)
        self.coins = tables.CoinsTable(self.pool)
        self.squads = tables.SquadsTable(self.pool)

    async def create(self) -> None:
        """
        Создание таблиц в БД
        """
        await self.users.create()
        await self.coins.create()
        await self.squads.create()
