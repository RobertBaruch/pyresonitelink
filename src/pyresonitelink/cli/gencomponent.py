"""CLI tool for generating Python component classes from JSON schemas."""

from __future__ import annotations

import argparse
import pathlib
import sys

from pyresonitelink import codegen


def main() -> int:
    """Main entry point for the component generator CLI.

    Parses command-line arguments and generates Python component classes
    from Resonite JSON schema files.

    Returns:
        Exit code: 0 on success, 1 on error.
    """
    parser = argparse.ArgumentParser(
        description="Generate Python component classes from Resonite JSON schemas",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Generate all components from a schema directory
  python -m pyresonitelink.cli.gencomponent /path/to/schemas

  # Generate a single component
  python -m pyresonitelink.cli.gencomponent /path/to/schemas --component FrooxEngine.StaticLocaleProvider

  # Preview without writing files
  python -m pyresonitelink.cli.gencomponent /path/to/schemas --dry-run
        """,
    )

    parser.add_argument(
        "schema_dir",
        type=pathlib.Path,
        help="Directory containing component .schema.json files",
    )

    parser.add_argument(
        "--output-dir",
        "-o",
        type=pathlib.Path,
        default=None,
        help="Output directory for generated Python files "
        "(default: src/pyresonitelink/components/generated)",
    )

    parser.add_argument(
        "--common-schema",
        type=pathlib.Path,
        default=None,
        help="Path to common.schema.json (auto-detected from schema_dir if not specified)",
    )

    parser.add_argument(
        "--component",
        "-c",
        type=str,
        default=None,
        help="Generate only a specific component (by schema filename without .schema.json)",
    )

    parser.add_argument(
        "--dry-run",
        "-n",
        action="store_true",
        help="Print generated code without writing files",
    )

    parser.add_argument(
        "--verbose",
        "-v",
        action="store_true",
        help="Print verbose output",
    )

    args = parser.parse_args()

    # Validate schema directory
    schema_dir: pathlib.Path = args.schema_dir
    if not schema_dir.exists():
        print(f"Error: Schema directory not found: {schema_dir}", file=sys.stderr)
        return 1

    if not schema_dir.is_dir():
        print(f"Error: Not a directory: {schema_dir}", file=sys.stderr)
        return 1

    # Find common schema
    common_schema_path: pathlib.Path | None = args.common_schema
    if common_schema_path is None:
        common_schema_path = schema_dir / "common.schema.json"
        if not common_schema_path.exists():
            print(
                f"Warning: common.schema.json not found in {schema_dir}",
                file=sys.stderr,
            )
            common_schema_path = None

    # Determine output directory
    output_dir: pathlib.Path | None = args.output_dir
    if output_dir is None:
        # Try to find the pyresonitelink package
        # Look for src/pyresonitelink relative to cwd
        cwd = pathlib.Path.cwd()
        possible_paths = [
            cwd / "src" / "pyresonitelink" / "components" / "generated",
            cwd / "pyresonitelink" / "components" / "generated",
        ]
        for p in possible_paths:
            if p.parent.exists():
                output_dir = p
                break
        if output_dir is None:
            output_dir = cwd / "generated"

    # Create output directory if needed
    if not args.dry_run:
        output_dir.mkdir(parents=True, exist_ok=True)

    # Initialize parser and generator
    schema_parser = codegen.SchemaParser(common_schema_path)
    generator = codegen.CodeGenerator(schema_parser)

    # Find schema files to process
    if args.component:
        # Single component
        schema_name = args.component
        if not schema_name.endswith(".schema.json"):
            schema_name = f"{schema_name}.schema.json"
        schema_files = [schema_dir / schema_name]
        if not schema_files[0].exists():
            print(f"Error: Schema file not found: {schema_files[0]}", file=sys.stderr)
            return 1
    else:
        # All component schemas
        schema_files = list(schema_dir.glob("*.schema.json"))
        # Exclude common.schema.json
        schema_files = [f for f in schema_files if f.name != "common.schema.json"]

    if not schema_files:
        print("No schema files found to process.", file=sys.stderr)
        return 1

    if args.verbose:
        print(f"Processing {len(schema_files)} schema file(s)...")
        print(f"Output directory: {output_dir}")

    # Process each schema
    success_count = 0
    error_count = 0

    for schema_path in sorted(schema_files):
        try:
            if args.verbose:
                print(f"  Processing: {schema_path.name}")

            generated = generator.generate_from_schema(schema_path)

            if args.dry_run:
                print(f"\n{'='*60}")
                print(f"# {generated.filename}")
                print(f"{'='*60}")
                print(generated.content)
            else:
                output_path = output_dir / generated.filename
                with open(output_path, "w", encoding="utf-8") as f:
                    f.write(generated.content)
                if args.verbose:
                    print(f"    -> {output_path}")

            success_count += 1

        except Exception as e:
            print(f"Error processing {schema_path.name}: {e}", file=sys.stderr)
            error_count += 1

    # Summary
    if not args.dry_run:
        print(f"\nGenerated {success_count} file(s)", end="")
        if error_count > 0:
            print(f", {error_count} error(s)")
        else:
            print()

    return 0 if error_count == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
