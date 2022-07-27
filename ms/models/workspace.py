import datetime
import uuid
from ms.db import db


class Workspace(db.Model):
    __tablename__ = 'workspace'

    _fillable = [
        'name',
        'description',
        'user_id',
    ]

    id = db.Column(
        db.String(length=36),
        default=lambda: str(uuid.uuid4()),
        primary_key=True)
    name = db.Column(db.String(length=120), nullable=False)
    description = db.Column(db.String(length=255), nullable=True)
    user_id = db.Column(db.String(length=36), nullable=False)
    created_at = db.Column(
        db.DateTime,
        default=datetime.datetime.utcnow,
        nullable=False)
    deleted_at = db.Column(
        db.DateTime,
        nullable=True)

    sections = db.relationship(
        "Section",
        back_populates="workspace",
        lazy='dynamic',
        cascade="all, delete")

    def __init__(self, data=None):
        if data is not None:
            self.setAttrs(data)

    def __repr__(self):
        return f"<Workspace {self.id}>"
