import json
from redis import Redis
from ms import app
from ms.helpers.time import epoch_now


class Cache:
    def __init__(self):
        self.chunk_size = 5000
        self.config = app.config.get("REDIS", dict())
        self.conn = self.connection()

    def connection(self):
        return Redis(
            host=self.config.get("HOST"),
            port=self.config.get("PORT"),
            username=self.config.get("USERNAME"),
            password=self.config.get("PASSWORD"),
            db=self.config.get("DATABASE")
        )

    def set(self, key, value, exp=None):
        data = json.dumps({
            "data": value,
            "key": key,
            "created_at": epoch_now(),
            "exp": exp
        })
        return self.conn.set(key, data, ex=exp)

    def get(self, key):
        data = self.get_raw(key)
        return None if data is None else data.get("data")

    def get_raw(self, key):
        data = self.conn.get(key)
        if data is not None:
            data = json.loads(data)
        return data

    def delete(self, key):
        return self.conn.delete(key)

    def truncate(self):
        cursor = '0'
        while cursor != 0:
            cursor, keys = self.conn.scan(
                cursor=cursor,
                match="*",
                count=self.chunk_size)
            if keys:
                self.conn.delete(*keys)
        return True

    def exists(self, key):
        return self.conn.exists(key) > 0

    def ping(self):
        return self.conn.ping()
