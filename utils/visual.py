import os
from io import BytesIO
from pathlib import Path

from PIL import Image, ImageChops

SNAPSHOT_DIR = Path(__file__).resolve().parent.parent / "snapshots"


def assert_matches_baseline(image_bytes, name):
    SNAPSHOT_DIR.mkdir(exist_ok=True)
    baseline = SNAPSHOT_DIR / f"{name}.png"

    update = os.getenv("UPDATE_SNAPSHOTS", "false").lower() == "true"
    if update or not baseline.exists():
        baseline.write_bytes(image_bytes)
        return

    actual = Image.open(BytesIO(image_bytes)).convert("RGB")
    expected = Image.open(baseline).convert("RGB")
    assert actual.size == expected.size, "Screenshot size changed"

    diff = ImageChops.difference(actual, expected).convert("L")
    changed = diff.point(lambda value: 255 if value > 25 else 0)
    assert changed.getbbox() is None, f"Visual change found in {name}"