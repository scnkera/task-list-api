from sqlalchemy.orm import Mapped, mapped_column
from ..db import db
from typing import Optional
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
            is_complete=complete_status
        )

    @classmethod
    def from_dict(cls, task_data):
        if "completed_at" in task_data:
            return cls(
            title=task_data["title"],
            description=task_data["description"],
            completed_at=task_data["completed_at"]
            )

        return cls(
            title=task_data["title"],
            description=task_data["description"],
        )