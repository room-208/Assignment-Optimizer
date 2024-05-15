from pathlib import Path

COMMON_DIR = Path(__file__).resolve().parent

ROOT_DIR = COMMON_DIR.parents[1]

DATA_DIR = ROOT_DIR / "data"
SRC_DIR = ROOT_DIR / "src"
OUTPUTS_DIR = ROOT_DIR / "outputs"

PARAMS_JSON_PATH = DATA_DIR / "params.json"
LOTS_CSV_PATH = DATA_DIR / "lots.csv"
YARDS_CSV_PATH = DATA_DIR / "yards.csv"

ASSIGNMENTS_CSV_PATH = (
    lambda stage: OUTPUTS_DIR / f"assignments_stage_{str(stage).zfill(4)}.csv"
)
ANIMATION_GIT_PATH = OUTPUTS_DIR / "animation.gif"

SEED = 0
N = 60
M = 2
H = 50
W = 20
T = 20

NUM_COLS = 2
