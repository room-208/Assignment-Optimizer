from pathlib import Path


def cleanup_csv(dir: Path) -> None:
    csv_files = dir.glob("*.csv")

    for csv_file in csv_files:
        csv_file.unlink()


def cleanup_gif(dir: Path) -> None:
    gif_files = dir.glob("*.gif")

    for gif_file in gif_files:
        gif_file.unlink()
