import json
import pypresence

with open("config.json") as f:
    config = json.load(f)

    rpc = pypresence.Presence(config["discord_config"]["id"])


def init():
    rpc.connect()


def update_presence(state_presence, desc):
    rpc.update(
        state=state_presence,
        details=desc,
        large_image="logo"
    )
