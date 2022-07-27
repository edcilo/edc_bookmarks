import datetime
import uuid
from ms.db import db


class Section(db.Model):
    __tablename__ = 'section'

    _fillable = [
        'name',
        'description',
        'workspace_id',
    ]

    id = db.Column(
        db.String(length=36),
        default=lambda: str(uuid.uuid4()),
        primary_key=True)
    name = db.Column(db.String(length=120), nullable=False)
    description = db.Column(db.String(length=255), nullable=True)
    workspace_id = db.Column(
        db.String(length=36),
        db.ForeignKey('workspace.id'),
        nullable=False)
    created_at = db.Column(
        db.DateTime,
        default=datetime.datetime.utcnow,
        nullable=False)
    deleted_at = db.Column(
        db.DateTime,
        nullable=True)

    workspace = db.relationship(
        "Workspace",
        back_populates="sections")
    resources = db.relationship(
        "Resource",
        back_populates="section",
        lazy='dynamic',
        cascade="all, delete")

    def __init__(self, data=None):
        if data is not None:
            self.setAttrs(data)

    def __repr__(self):
        return f"<Section {self.id}>"
