import os


cache_config = {
    "REDIS": {
        "HOST": os.getenv("REDIS_HOST", "127.0.0.1"),
        "USERNAME": os.getenv("REDIS_USERNAME"),
        "PASSWORD": os.getenv("REDIS_PASSWORD"),
        "PORT": os.getenv("REDIS_PORT", "6379"),
        "DATABASE": os.getenv("REDIS_DB", "0"),
    },
}
