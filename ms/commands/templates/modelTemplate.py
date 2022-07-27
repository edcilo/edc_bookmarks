import datetime
import uuid
from ms.db import db


class <CLASSNAME>(db.Model):
    __tablename__ = '<TABLENAME>'

    _fillable = []

    id = db.Column(
        db.String(length=36),
        default=lambda: str(uuid.uuid4()),
        primary_key=True)
    created_at = db.Column(
        db.DateTime,
        default=datetime.datetime.utcnow,
        nullable=False)

    def __init__(self, data=None):
        if data is not None:
            self.setAttrs(data)

    def __repr__(self):
        return f"<<CLASSNAME> {self.id}>"
