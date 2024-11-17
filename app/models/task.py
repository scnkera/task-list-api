from sqlalchemy.orm import Mapped, mapped_column
from ..db import db
from datetime import datetime

class Task(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    title: Mapped[str]
    description: Mapped[str]
    completed_at:Mapped[datetime] = mapped_column(default=None, nullable=True)

    def to_dict(self):
        complete_status=False

        if self.completed_at:
            complete_status = True

        return dict(
            id=self.id,
            title=self.title,
            description=self.description,
            completed_at=complete_status
        )
