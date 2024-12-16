class QueueService:
    def __init__(self):
        self.queue = []  

    def add_to_queue(self, data):

        self.queue.append(data)
        return {"message": "Elemento añadido a la cola correctamente", "data": data}

    def get_queue(self):

        return {"queue": self.queue}
