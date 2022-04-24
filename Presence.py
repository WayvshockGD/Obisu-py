import json
import pypresence

with open("config.json") as f:
    config = json.load(f)

    rpc = pypresence.Presence(config["discord_config"]["id"])


def init():
    try:
        rpc.connect()
    except pypresence.InvalidPipe:
        print("Unable to connect to discord, running without presence")


def update_presence(state_presence, desc):
    try:
        rpc.update(
            state=state_presence,
            details=desc,
            large_image="logo"
        )
    except AssertionError:
        pass
