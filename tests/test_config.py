from ms.config.dbConfig import configuration, db_connection


def test_dbconfig():
    configuration["default"] = "sqlite"
    configuration["connections"]["sqlite"]["database"] = "/tmp/db.sqlite"
    configuration["connections"]["psql"]["host"] = "localhost"
    configuration["connections"]["psql"]["port"] = "5432"
    configuration["connections"]["psql"]["database"] = "postgres"
    configuration["connections"]["psql"]["username"] = "postgres"
    configuration["connections"]["psql"]["password"] = "secret"


    db_conf = db_connection(configuration)
    assert "SQLALCHEMY_DATABASE_URI" in db_conf
    assert "SQLALCHEMY_TRACK_MODIFICATIONS" in db_conf
    assert db_conf.get("SQLALCHEMY_DATABASE_URI") == "sqlite:////tmp/db.sqlite"

    configuration["default"] = "psql"
    db_conf = db_connection(configuration)
    assert db_conf.get("SQLALCHEMY_DATABASE_URI") == "postgresql://postgres:secret@localhost:5432/postgres"

    try:
        configuration["default"] = "foo"
        db_conf = db_connection(configuration)
    except Exception as e:
        assert str(e) == "The database engine does not exist"
