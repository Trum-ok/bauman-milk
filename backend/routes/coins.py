from fastapi import APIRouter, Depends
from services.coins_service import get_coin_count, add_coin

from models import StatData, AllStatData

router = APIRouter()


@router.get("/clicker/core/stat")
async def get_stat():
    stats = StatData(
        minedCoins=await get_coin_count(),
        burnedCoins=50,
        balanceCoins=200,
        teamCoins=10,
        online=5,
        onlineToday=50,
        users=1000,
        teams=10,
        loading=False
    )
    print(stats.minedCoins)
    return stats
    

@router.post("/api/coins/add")
async def add_coin_route(pool=Depends(add_coin)):
    return {"status": await pool()}

@router.get("/clicker/league/leaderboard/public/user/silver/all")
async def user_stat():
    all = AllStatData(
        leaderboard=["1", "2"],
        loading=False
    )
    return all

@router.get("/clicker/league/leaderboard/public/team/silver/all")
async def team_stat():
    all = AllStatData(
        leaderboard=["5", "6"],
        loading=False
    )
    return all
