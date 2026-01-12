# Python bindings for [ResoniteLink](https://github.com/Yellow-Dog-Man/ResoniteLink/tree/master)

The minimum Python version for this library is 3.13.

Note that because Python's native numeric types are infinite-precision integers and 64-bit floats, and Resonite has stricter types than that, this library uses `numpy` for numeric types, such as `np.uint8, np.uint16, np.float32`, and so on. It does not, however, use numpy arrays, so for example `byte2` is still a struct of two `np.uint8` values (see `src/pyresonitelink/data/primitives.py` class `byte2`). See the example code for more details, especially the `test_update_component` test in `tests/test_values.py`.

## Release

I have released a pip package. Check the Releases section on the right. Install with `pip install <wheel-file>`.

## Remember to start ResoniteLink in your world!

You can do this in your dashboard, under Settings (Enable ResoniteLink). It will show you the port it chose. Use that for connections.

## Sample code

Take a look at `examples/get_root_slot.py` for a very quick and dirty method to get root slot data. You can run it as `python examples/get_root_slot.py <port>`

You can also look at `tests/test_values.py` to see more complex usage.

## Command-line tools

### `pyresonitelink.cli.dumptree`: Slot hierarchy dumper

Run `python -m pyresonitelink.cli.dumptree [--depth=<0|1|-1>] [--include_components] <port> <output-file>`.

This will download the slot hierarchy at the given depth (0 = only requested slot, 1 = slot and immediate children, -1 = all children recursively, default -1), and includes full component data if `--include_components` is present. The slot hierarchy is then saved to the given file as formatted JSON.

### `pyresonitelink.cli.tree`: Tree browser

Run `python -m pyresonitelink.cli.tree <port>`. It will download the slot hierarchy and then you can browse it.

![Screenshot of the tree browser](docs/tree_example.png "Example of the tree browser")

## Ideas

* Add specific component models

## Bugs

The first connection to ResoniteLink fails after sending the first message, during the await for the response, with a `websockets.exceptions.ConnectionClosedError: no close frame received or sent` error. Subsequent connections seem to work normally. In the Resonite logs, we see `WebSocket closed in ResoniteLink. WasClean: False, Code: 1006`. Code 1006 is abnormal closure (connection lost unexpectedly).
