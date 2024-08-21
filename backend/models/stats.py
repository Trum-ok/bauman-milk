from pydantic import BaseModel
from typing import Any, List


class StatData(BaseModel):
    minedCoins: int
    burnedCoins: int
    balanceCoins: int
    teamCoins: int
    online: int
    onlineToday: int
    users: int
    teams: int
    loading: bool


class AllStatData(BaseModel):
    leaderboard: List[Any]
    loading: bool
