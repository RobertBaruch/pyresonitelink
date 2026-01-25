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

### `pyresonitelink.cli.gencomponent`: Component class generator

Generates Python dataclass components from Resonite JSON Schema files. The generated classes include serialization (`to_json()`) and deserialization (`from_json()`) with optional jsonschema validation.

**Basic usage:**

```bash
# Generate all components from a schema directory
python -m pyresonitelink.cli.gencomponent /path/to/schemas

# Generate with custom output directory
python -m pyresonitelink.cli.gencomponent /path/to/schemas --output-dir ./my_components

# Preview generated code without writing files
python -m pyresonitelink.cli.gencomponent /path/to/schemas --dry-run

# Verbose output
python -m pyresonitelink.cli.gencomponent /path/to/schemas --verbose
```

**Generating a non-generic component:**

```bash
# Generate a single non-generic component like UnlitMaterial
python -m pyresonitelink.cli.gencomponent /path/to/schemas --component FrooxEngine.UnlitMaterial --dry-run
```

This produces a single Python class:

```python
@dataclass
class UnlitMaterial(GeneratedComponent):
    """UnlitMaterial component."""

    COMPONENT_TYPE: ClassVar[str] = "[FrooxEngine]FrooxEngine.UnlitMaterial"
    SCHEMA_FILE: ClassVar[str] = "FrooxEngine.UnlitMaterial.schema.json"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "persistent": "persistent",
        "update_order": "UpdateOrder",
        "enabled": "Enabled",
        # ... more fields
    }

    persistent: FieldBool | None = None
    update_order: FieldInt | None = None
    enabled: FieldBool | None = None
    # ... more fields
```

**Generating a generic component:**

```bash
# Generate a generic component like ValueField<T>
python -m pyresonitelink.cli.gencomponent /path/to/schemas --component FrooxEngine.ValueField_1 --dry-run
```

Generic components (those with `oneOf` in their schema) produce:
1. A base class with common fields
2. Variant classes for each type parameter
3. A type alias union of all variants

```python
@dataclass
class ValueFieldBase(GeneratedComponent):
    """Base class for ValueField<T> variants."""

    SCHEMA_FILE: ClassVar[str] = "FrooxEngine.ValueField_1.schema.json"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "persistent": "persistent",
        "update_order": "UpdateOrder",
        "enabled": "Enabled",
    }

    persistent: FieldBool | None = None
    update_order: FieldInt | None = None
    enabled: FieldBool | None = None


@dataclass
class ValueFieldBool(ValueFieldBase):
    """ValueField<bool> component."""

    COMPONENT_TYPE: ClassVar[str] = "[FrooxEngine]FrooxEngine.ValueField`1[[System.Boolean, System.Private.CoreLib]]"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "value": "Value",
    }

    value: FieldBool | None = None


@dataclass
class ValueFieldFloat(ValueFieldBase):
    """ValueField<float> component."""

    COMPONENT_TYPE: ClassVar[str] = "[FrooxEngine]FrooxEngine.ValueField`1[[System.Single, System.Private.CoreLib]]"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "value": "Value",
    }

    value: FieldFloat | None = None

# ... more variants ...

# Type alias for any ValueField variant
ValueField = ValueFieldBool | ValueFieldFloat | ValueFieldInt | ...
```

**Using generated components:**

```python
from pyresonitelink.components.generated.unlit_material import UnlitMaterial
from pyresonitelink.data.fields import FieldBool

# Create a component
material = UnlitMaterial(
    id="some-id",
    enabled=FieldBool(value=True),
)

# Serialize to JSON
json_data = material.to_json()

# Deserialize from JSON (with optional schema validation)
material2 = UnlitMaterial.from_json(json_data, validate=False)
```

## Ideas

* Add specific component models

## Bugs

The first connection to ResoniteLink fails after sending the first message, during the await for the response, with a `websockets.exceptions.ConnectionClosedError: no close frame received or sent` error. Subsequent connections seem to work normally. In the Resonite logs, we see `WebSocket closed in ResoniteLink. WasClean: False, Code: 1006`. Code 1006 is abnormal closure (connection lost unexpectedly).
