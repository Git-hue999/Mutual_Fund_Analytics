"""
Master pipeline for the Bluestock Fintech Mutual Fund Analytics project.

Runs the main data ingestion, cleaning, validation, database loading,
and analytical scripts in sequence.
"""

import subprocess
import sys


SCRIPTS = [
    "data_ingestion.py",
    "clean_nav_history.py",
    "clean_scheme_performance.py",
    "clean_investor_transactions.py",
    "validate_data.py",
    "load_to_sqlite.py",
    "eda_fund_master.py",
]


def run_script(script):
    """Run a project Python script and stop if it fails."""
    print(f"\nRunning {script}...")
    subprocess.run([sys.executable, script], check=True)
    print(f"Completed {script}")


def main():
    """Run the complete project pipeline."""
    for script in SCRIPTS:
        run_script(script)

    print("\nPipeline completed successfully.")


if __name__ == "__main__":
    main()