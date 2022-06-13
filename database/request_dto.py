class Request:
    def __init__(self, req_id, user_id, amount, desc, status):
        self.req_id = req_id
        self.user_id = user_id
        self.amount = amount
        self.desc = desc
        self.status = status    

    def to_dict(self):
        dictionary = {
            'req_id': self.req_id,
            'user_id': self.user_id,
            'amount': float(self.amount),
            'desc': self.desc,
            'status': self.status
        }
        return dictionary