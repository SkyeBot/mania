from quart import Quart, Blueprint
import discord
from discord.ext import commands

views = Blueprint("views", __name__)


@views.route("/")
async def home():
    return "Hello World!"
