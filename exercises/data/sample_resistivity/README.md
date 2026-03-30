# Sample Resistivity Data

This folder contains sample electrical resistivity data for practice exercises.

## Data Format

- `.dat` files: Standard resistivity data format
- Columns: A, B, M, N, Resistance

## Usage

```python
from resipy import Project

k = Project()
k.createSurvey('data/sample_resistivity/survey.dat')
k.invert()
```

## Data Sources

Sample data is synthetic or from open sources with appropriate attribution.
