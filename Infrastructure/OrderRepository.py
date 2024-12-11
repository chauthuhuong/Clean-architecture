from Entities.Order import Order

class OrderRepository:
    def __init__(self, session):
        self.session = session

    def save(self, order: Order):
        self.session.add(order)
        self.session.commit()

    def find_by_id(self, order_id: int):
        return self.session.query(Order).filter_by(id=order_id).first()

    def get_all(self):
        return self.session.query(Order).all()

    def delete(self, order_id: int):
        order = self.session.query(Order).filter_by(id=order_id).first()
        if order:
            self.session.delete(order)
            self.session.commit()