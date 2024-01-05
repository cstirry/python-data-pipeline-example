# Python-Data-Pipeline-Template

Example Python data pipeline to experiment with python packages for operationalizing data pipelines.

Pipeline ingests, processes, and validates data from the Baltimore City API.

### Packages/Tools

- [Pandera](https://pandera.readthedocs.io/en/stable/index.html) for data validation
- [unittest](https://docs.python.org/3/library/unittest.html) for unit tests in CI
- [logging](https://docs.python.org/3/howto/logging.html) for logging
- Github Actions

### File Structure

- .github/workflows/ci.yml: GitHub Actions workflow file for continuous integration.
- src/main.py: Main python script containing data fetching, loading, processing, and validation logic.
- src/utils.py: Utility functions for data processing and validation schema.
- src/tests/test_utils.py: Unit tests for utility functions.
- requirements.txt: Project dependencies