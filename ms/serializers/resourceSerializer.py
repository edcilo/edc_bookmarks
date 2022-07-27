from ms.helpers import time
from ms.serializers import Serializer


class ResourceSerializer(Serializer):
    response = {
        "id": str,
        "name": str,
        "url": str,
        "created_at": time.datetime_to_epoch,
    }
