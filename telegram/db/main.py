import db.tables as tables


class Database:
    def __init__(self, session):
        self.session = session
        self.users = tables.UsersTable(self.session)
        self.energy = tables.EnergyTable(self.session)
        self.upgrades = tables.UpgradesTable(self.session)
        # self.coins = tables.CoinsTable(self.session)
        # self.squads = tables.SquadsTable(self.session)

    def create(self) -> None:
        """
        Создание таблиц в БД
        """
        self.users.create()
        self.energy.create()
        self.upgrades.create()
        # self.coins.create()
        # self.squads.create()
