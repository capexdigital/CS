import subprocess
import glob

def test_scripts_run_without_error():
    scripts = glob.glob("Python/**/*.py", recursive=True)
    for script in scripts:
        result = subprocess.run(["python", script], input="", capture_output=True, timeout=10)
        assert result.returncode == 0, f"{script} falhou: {result.stderr}"