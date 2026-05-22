# MaTra - Map Transformer for Wathe to StarRailExpress Fork

Simply replace modid from `wathe` to `trainmurdermystery` should work for
most cases.

## Docker usage

The container expects an input and output file path. By default it runs:

`convert input.litematic output.litematic`

Mount your current directory to `/data`:

```bash
# expects ./input.litematic and writes ./output.litematic
docker run --rm -v "$(pwd):/data" ghcr.io/huluqq888/matra-sre:latest
```

To use different filenames, pass explicit arguments:

```bash
docker run --rm -v "$(pwd):/data" ghcr.io/huluqq888/matra-sre:latest convert my-input.litematic my-output.litematic
```

On Windows PowerShell, use `${PWD}` instead of `$(pwd)`:

```powershell
docker run --rm -v "${PWD}:/data" ghcr.io/huluqq888/matra-sre:latest convert my-input.litematic my-output.litematic
```
