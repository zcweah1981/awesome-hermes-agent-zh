import subprocess
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MAX_TRACKED_BYTES = 5 * 1024 * 1024


def main() -> int:
    output = subprocess.check_output(["git", "ls-files", "-z"], cwd=ROOT)
    files = [Path(item.decode("utf-8")) for item in output.split(b"\0") if item]
    oversized = [
        (relative, (ROOT / relative).stat().st_size)
        for relative in files
        if (ROOT / relative).is_file() and (ROOT / relative).stat().st_size > MAX_TRACKED_BYTES
    ]
    if oversized:
        for relative, size in oversized:
            print(f"{relative.as_posix()}: {size / 1024 / 1024:.2f} MiB")
        raise SystemExit("tracked files above 5 MiB require an explicit storage decision")
    print(f"repository hygiene verified tracked_files={len(files)} max_file_mib=5")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
