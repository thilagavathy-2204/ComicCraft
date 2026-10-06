from pathlib import Path
import shutil


def generate_image(prompt: str, panel_number: int) -> str:
    output_dir = Path("static") / "panels"
    output_dir.mkdir(parents=True, exist_ok=True)

    asset_path = Path("static") / "comic_assets" / f"panel_{panel_number}.png"
    output_path = output_dir / f"panel_{panel_number}.png"

    if not asset_path.exists():
        raise FileNotFoundError(f"Comic panel asset not found: {asset_path}")

    shutil.copy2(asset_path, output_path)

    return f"/static/panels/panel_{panel_number}.png"
