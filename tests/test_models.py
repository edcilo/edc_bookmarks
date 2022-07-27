from ms.db import Model


def test_model():
    mock = Model()
    mock._fillable = ["foo"]
    mock.setAttrs({"foo": "bar", "zoo": False})
    assert mock.foo == "bar"
    assert getattr(mock, "zoo", None) is None
    mock.update({"foo": "zoo"})
    assert mock.foo == "zoo"
