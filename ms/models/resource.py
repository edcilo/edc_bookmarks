import datetime
import uuid
from ms.db import db


class Resource(db.Model):
    __tablename__ = 'resource'

    _fillable = [
        "url",
        "name",
        "section_id",
    ]

    id = db.Column(
        db.String(length=36),
        default=lambda: str(uuid.uuid4()),
        primary_key=True)
    url = db.Column(db.String(length=512), nullable=False)
    name = db.Column(db.String(length=120), nullable=False)
    section_id = db.Column(
        db.String(length=36),
        db.ForeignKey('section.id'),
        nullable=False)
    created_at = db.Column(
        db.DateTime,
        default=datetime.datetime.utcnow,
        nullable=False)

    section = db.relationship(
        "Section",
        back_populates="resources")

    def __init__(self, data=None):
        if data is not None:
            self.setAttrs(data)

    def __repr__(self):
        return f"<Resource {self.id}>"
