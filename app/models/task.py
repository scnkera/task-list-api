class Task:
    def __init__(self, id, title, description, is_complete):
        self.id = id
        self.title = title
        self.description =  description
        self.is_complete = is_complete

    def to_dict(self):
        return dict(
            id=self.id,
            title=self.title,
            description=self.description,
            is_complete=self.is_complete
        )

tasks = [
    Task(1, "Breakfast", "Eat eggs", "True"),
    Task(2, "Brush Teeth", "Colgate", "True"),
    Task(3, "Bathe", "Shampoo and conditioner", "False"),
    Task(4, "Breakfast", "Eat eggs", "True"),
    Task(5, "Brush Teeth", "Colgate", "True"),
    Task(6, "Bathe", "Shampoo and conditioner", "False")
]
