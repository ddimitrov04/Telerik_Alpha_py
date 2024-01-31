from core.application_data import ApplicationData
from core.command_factory import CommandFactory
from core.engine import Engine
from models import *
from models.category import Category
from models.product import Product

app_data = ApplicationData()
cmd_factory = CommandFactory(app_data)
engine = Engine(cmd_factory)

engine.start()

