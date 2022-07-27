import abc
from sqlalchemy import or_
from ms.db import db
from ms.helpers import time


class Repository(abc.ABC):
    def __init__(self) -> None:
        self.session = db.session
        self._model = self.get_model()

    @abc.abstractmethod
    def get_model(self):
        pass

    def db_save(self, model=None):
        self.session.add(model)
        self.session.commit()

    def db_delete(self, model):
        self.session.delete(model)
        self.session.commit()

    def add(self, data):
        user = self._model(data)
        self.db_save(user)
        return user

    def all(
            self,
            order_column='created_at',
            order='desc',
            filter=lambda q: q,
            paginate=False,
            page=1,
            per_page=15,
            deleted=False,
            with_deleted=False):
        column = getattr(self._model, order_column)
        order_by = getattr(column, order)
        q = self._model.query
        q = filter(q)
        if hasattr(self._model, 'deleted_at'):
            if deleted:
                q = q.filter(self._model.deleted_at.is_not(None))
            elif not with_deleted:
                q = q.filter(self._model.deleted_at.is_(None))
        q = q.order_by(order_by())
        return q.paginate(page, per_page=per_page) if paginate else q.all()

    def find(self, id, fail=True, with_deleted=False):
        if isinstance(id, self._model):
            return id
        filters = {'id': id}
        if hasattr(self._model, 'deleted_at') and not with_deleted:
            filters['deleted_at'] = None
        q = self._model.query.filter_by(**filters)
        return q.first_or_404() if fail else q.first()

    def find_by_attr(self, column, value, fail=True, with_deleted=False):
        q = self._model.query.filter_by(**{column: value})
        if hasattr(self._model, 'deleted_at') and not with_deleted:
            q = q.filter(self._model.deleted_at.is_(None))
        return q.first_or_404() if fail else q.first()

    def find_optional(self, filter, fail=True, with_deleted=False):
        filters = [
            getattr(self._model, key) == val for key,
            val in filter.items()]
        q = self._model.query.filter(or_(*filters))
        if hasattr(self._model, 'deleted_at') and not with_deleted:
            q = q.filter(self._model.deleted_at.is_(None))
        return q.first_or_404() if fail else q.first()

    def update(self, id, data, fail=True, with_deleted=False):
        model = self.find(id, fail=fail, with_deleted=with_deleted)
        if model is not None:
            model.update(data)
            self.db_save(model)
        return model

    def soft_delete(self, id, fail=True):
        model = self.find(id, fail=fail)
        if not hasattr(model, 'deleted_at'):
            raise Exception('Model does not have a deleted_at column')
        if model is not None:
            model.deleted_at = time.now()
            self.db_save(model)
        return model

    def restore(self, id, fail=True):
        model = self.find(id, fail=fail)
        if not hasattr(model, 'deleted_at'):
            raise Exception('Model does not have a deleted_at column')
        if model is not None:
            model.deleted_at = None
            self.db_save(model)
        return model

    def delete(self, id, fail=True):
        model = self.find(id, fail=fail)
        if model is not None:
            self.db_delete(model)
        return model
