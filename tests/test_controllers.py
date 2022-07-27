from ms.controllers.controller import Controller, BadMethodCallException


def test_controller():
    class MockController(Controller):
        def method(self):
            return True

    assert MockController.action('method') == True

    try:
        MockController.action('missing')
    except BadMethodCallException as e:
        assert str(e) == "Method MockController.missing does not exist."
