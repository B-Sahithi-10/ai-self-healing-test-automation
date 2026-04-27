import subprocess


def python_compile_check(file_path):
    result = subprocess.run(
        ["python", "-m", "py_compile", file_path],
        capture_output=True,
        text=True,
    )
    return {
        "returncode": result.returncode,
        "stdout": result.stdout.strip(),
        "stderr": result.stderr.strip(),
    }
