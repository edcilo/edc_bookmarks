import os


class Make:
    def __init__(self, entity_path: str, template: str) -> None:
        self.appPath = os.path.realpath("")
        self.templatesPath = "ms/commands/templates"
        self.entityPath = entity_path
        self.templateFile = template
        self.entityName = None

    def set_entityname(self, name):
        self.entityName = name

    @property
    def placeholders(self):
        return [
            {
                'placeholder': '<CLASSNAME>',
                'value': 'entityName',
            },
        ]

    @property
    def source(self):
        return os.path.join(self.appPath, self.templatesPath, self.templateFile)

    @property
    def filename(self):
        return f"{self.entityName[0].lower()}{self.entityName[1:]}.py"

    @property
    def destination(self):
        return os.path.join(self.appPath, self.entityPath, self.filename)

    def check(self):
        return os.path.exists(self.destination)

    def make(self, name: str):
        if self.entityName is None:
            self.set_entityname(name)

        src = open(self.source, "rt")
        dest = open(self.destination, "wt")

        for line in src:
            for placeholder in self.placeholders:
                key = placeholder.get('placeholder')
                value = getattr(self, placeholder.get('value'))
                line = line.replace(key, value)
            dest.write(line)

        src.close()
        dest.close()
