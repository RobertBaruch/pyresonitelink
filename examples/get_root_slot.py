"""Example showing connecting and getting root slot data."""
import sys

from pyresonitelink import client
from pyresonitelink.data import messages


def main(port: int):
    resolink = client.Client()
    resolink.sync_connect(port)
    print("Connected, getting root slot...")
    slot = resolink.get_slot(messages.GetSlot(slotId="Root"))
    print(slot)
    resolink.sync_close()


if __name__ == "__main__":
    main(int(sys.argv[1]))
