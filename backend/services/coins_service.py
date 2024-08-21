from config import get_pool

async def get_coin_count() -> int:
    pool = await get_pool()
    async with pool.acquire() as connection:
        result = await connection.fetchval("SELECT SUM(coins) FROM coins")
    await pool.close()
    return result if result else 0

async def add_coin(tg_id: int, n: int = 1):
    pool = await get_pool()
    async with pool.acquire() as connection:
        await connection.execute(f"UPDATE players SET coins = coins + {n} WHERE tg_id = {tg_id}")
    await pool.close()
    return "Coin added"
