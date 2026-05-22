from pathlib import Path

import typer
from litemapy import Schematic


app = typer.Typer()


@app.command("convert")
def convert(
    in_path: Path = typer.Argument(..., metavar="in"),
    out_path: Path = typer.Argument(..., metavar="out"),
) -> None:
    schem = Schematic.load(str(in_path))

    for reg in schem.regions.values():
        for x in reg.xrange():
            for y in reg.yrange():
                for z in reg.zrange():
                    b = reg[x, y, z]
                    if b.id.startswith("wathe:"):
                        new_block_id = b.id.replace("wathe:", "trainmurdermystery:")
                        reg[x, y, z] = getattr(b, "with_blockid")(new_block_id)

    schem.save(str(out_path))

    print(f"Schematic successfully saved to {out_path}!")


@app.callback()
def main():
    pass


if __name__ == "__main__":
    app()
