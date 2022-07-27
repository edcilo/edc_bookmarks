from flaskFormRequest import FormRequest
from flaskFormRequest.validators import Required


class <CLASSNAME>(FormRequest):
    def rules(self):
        return {
            "foo": [Required()],
        }
