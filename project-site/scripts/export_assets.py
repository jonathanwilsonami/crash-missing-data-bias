"""Export figures and notebook pages from the executed analysis notebooks into the Quarto site.

Run from the repository root after re-executing the notebooks:

    python project-site/scripts/export_assets.py

* Every notebook cell tagged ``fig-*`` has its PNG output written to ``project-site/assets/figures/<tag>.png``.
* Each notebook is rendered to a standalone HTML page in ``project-site/`` (published as a site resource).
"""
import base64
import subprocess
from pathlib import Path

import nbformat

ROOT = Path(__file__).resolve().parents[2]
SITE = ROOT / "project-site"
FIG_DIR = SITE / "assets" / "figures"
NOTEBOOKS = {
    "missing_data_analysis.ipynb": "notebook-missing-data.html",
    "rural_severity_model.ipynb": "notebook-rural-model.html",
}


def export_figures(nb_path: Path) -> int:
    nb = nbformat.read(nb_path, as_version=4)
    n = 0
    for cell in nb.cells:
        tags = [t for t in cell.get("metadata", {}).get("tags", []) if t.startswith("fig-")]
        pngs = [o["data"]["image/png"] for o in cell.get("outputs", []) if "image/png" in o.get("data", {})]
        for tag in tags:
            if not pngs:
                raise RuntimeError(f"{nb_path.name}: cell tagged {tag} has no PNG output (re-execute the notebook)")
            (FIG_DIR / f"{tag}.png").write_bytes(base64.b64decode(pngs[0]))
            n += 1
    return n


def export_html(nb_path: Path, out_name: str) -> None:
    subprocess.run(["jupyter", "nbconvert", "--to", "html", "--output-dir", str(SITE),
                    "--output", out_name.removesuffix(".html"), str(nb_path)], check=True)


if __name__ == "__main__":
    FIG_DIR.mkdir(parents=True, exist_ok=True)
    for nb_name, html_name in NOTEBOOKS.items():
        path = ROOT / nb_name
        print(f"{nb_name}: {export_figures(path)} figures")
        export_html(path, html_name)
