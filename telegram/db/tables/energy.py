from cassandra.cluster import Session


class EnergyTable:
    """Energy Table"""

    def __init__(self, session: Session) -> None:
        self.session = session


    def create(self) -> None:
        """Create user_energy table"""
        
        query = """
		CREATE TABLE IF NOT EXISTS user_energy (
			user_id BIGINT PRIMARY KEY,
			energy COUNTER
		);
        """
        self.session.execute(query)
    
    
    def first(self, user_id: int, amount: int) -> None:
        """Ensure the user has an energy row and update their energy"""
        
        check_query = "SELECT user_id FROM user_energy WHERE user_id = %s"
        result = self.session.execute(check_query, (user_id,)).one()

        if result is None:
            update_query = """
                UPDATE user_energy
                SET energy = energy + %s
                WHERE user_id = %s;
            """
            self.session.execute(update_query, (amount, user_id))
        else:
            pass


    def update(self, user_id: int, amount: int) -> None:
        update_query = """
                UPDATE user_energy
                SET energy = energy + %s
                WHERE user_id = %s;
            """
        self.session.execute(update_query, (amount, user_id))
