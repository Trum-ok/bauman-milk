from cassandra.cluster import Session

class UpgradesTable:
    def __init__(self, session: Session) -> None:
        self.session = session
        
    def create(self) -> None:
        query = \
        """
        CREATE TABLE IF NOT EXISTS upgrades (
			user_id BIGINT PRIMARY KEY,
			click_value INT,
			auto_click BOOLEAN,
			energy INT
		);
        """
        self.session.execute(query)


    def insert(self, user_id: int, click_value: int = 1, auto_click: bool = False, energy: int = 1) -> None:
        query = \
        """
        INSERT INTO upgrades (user_id, click_value, auto_click, energy)
        VALUES (%s, %s, %s, %s)
        IF NOT EXISTS
        """
        self.session.execute(query, (user_id, click_value, auto_click, energy))


    def update(self, user_id: int, column_name: str, value: int) -> None:
        """Update a specific upgrade column for a given user."""

        query = f"""
        UPDATE upgrades
        SET {column_name} = %s
        WHERE user_id = %s
        """
        self.session.execute(query, (value, user_id))

