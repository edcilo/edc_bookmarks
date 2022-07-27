import os
from fixture import app, runner
from ms.commands import pep8, makecontroller, makeform, makemiddleware, makeseeder, makemodel


def test_command_pep8(runner):
    file = "./tests/pep8file.py"

    f = open(file, "w+")
    f.write("""
def long_function_name(
    var_one, var_two, var_three,
    var_four):
    print(var_one)""")
    f.close()

    runner.invoke(pep8, ["--path", file])

    formated = """
def long_function_name(
        var_one, var_two, var_three,
        var_four):
    print(var_one)
"""
    assert formated == open(file).read()
    os.remove(file)


def test_command_makecontroller(runner):
    nameController = "mockController"
    appPath = os.path.realpath("")
    controllerPath = "ms/controllers"
    fullPath = os.path.join(appPath, controllerPath, f"{nameController}.py")

    runner.invoke(makecontroller, ['--name', nameController])

    assert os.path.exists(fullPath)
    os.remove(fullPath)


def test_command_makeform(runner):
    nameForm = "mockForm"
    appPath = os.path.realpath("")
    formPath = "ms/forms"
    fullPath = os.path.join(appPath, formPath, f"{nameForm}.py")

    runner.invoke(makeform, ["--name", nameForm])

    assert os.path.exists(fullPath)
    os.remove(fullPath)


def test_command_makemiddleware(runner):
    nameController = "mockMiddleware"
    appPath = os.path.realpath("")
    controllerPath = "ms/middlewares"
    fullPath = os.path.join(appPath, controllerPath, f"{nameController}.py")

    runner.invoke(makemiddleware, ['--name', nameController])

    assert os.path.exists(fullPath)
    os.remove(fullPath)


def test_command_makemodel(runner):
    nameModel = "mockModel"
    appPath = os.path.realpath("")
    modelsPath = "ms/models"
    fullPath = os.path.join(appPath, modelsPath, f"{nameModel}.py")

    runner.invoke(makemodel, ['--name', nameModel])

    assert os.path.exists(fullPath)
    os.remove(fullPath)


def test_command_makeseeder(runner):
    nameSeeder = "mockSeeder"
    appPath = os.path.realpath("")
    controllerPath = "ms/db/seeders"
    fullPath = os.path.join(appPath, controllerPath, f"{nameSeeder}.py")

    runner.invoke(makeseeder, ['--name', nameSeeder])

    assert os.path.exists(fullPath)
    os.remove(fullPath)
