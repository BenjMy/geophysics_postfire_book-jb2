# Sample Electromagnetic Data

This folder contains sample electromagnetic data for practice exercises.

## Data Format

- `.csv` files: Processed EM data
- Columns vary by instrument type

## Usage

```python
from emagpy import Problem

k = Problem()
k.importData('data/sample_em/survey.csv')
k.invert()
```
