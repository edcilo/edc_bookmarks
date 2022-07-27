from ms.helpers import time
from ms.serializers import Serializer


class SectionSerializer(Serializer):
    response = {
        "id": str,
        "name": str,
        "description": str,
        "created_at": time.datetime_to_epoch,
        "deleted_at": lambda date: time.datetime_to_epoch(date) if date else None,
    }
