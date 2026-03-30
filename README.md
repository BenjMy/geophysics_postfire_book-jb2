# Geophysics with Python: resipy and emagpy Course

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/BenjMy/geophysics-python-course/HEAD)

Welcome to the Geophysics with Python course! This comprehensive course teaches geophysical data analysis using resipy (resistivity) and emagpy (electromagnetic) Python packages.

## 📚 Course Overview

This course covers:
- Python fundamentals for geophysics
- Electrical resistivity imaging with resipy
- Electromagnetic data processing with emagpy
- Real-world case studies and applications
- Data visualization and interpretation

## 🚀 Getting Started

### Prerequisites
- Python 3.9 or higher
- Basic understanding of geophysics (helpful but not required)
- Jupyter Notebook or JupyterLab

### Installation

#### Option 1: Using Poetry (Recommended)
```bash
# Clone the repository
git clone https://github.com/yourusername/geophysics-python-course.git
cd geophysics-python-course

# Install Poetry (if not already installed)
curl -sSL https://install.python-poetry.org | python3 -

# Install dependencies and create virtual environment
poetry install

# Activate the virtual environment
poetry shell

# Launch Jupyter
jupyter lab
```

#### Option 2: Using Conda
```bash
# Clone the repository
git clone https://github.com/yourusername/geophysics-python-course.git
cd geophysics-python-course

# Create conda environment
conda env create -f environment.yml
conda activate geophysics-course

# Launch Jupyter
jupyter lab
```

## 📖 Course Structure

1. **Introduction** - Python basics and scientific computing
2. **resipy Module** - Resistivity data processing and inversion
3. **emagpy Module** - Electromagnetic methods
4. **Case Studies** - Real-world applications

## 🎯 Learning Outcomes

By the end of this course, you will be able to:
- Process and analyze geophysical data using Python
- Perform resistivity inversions with resipy
- Process electromagnetic data with emagpy
- Create professional visualizations
- Apply techniques to real-world scenarios

## 📂 Repository Structure

- `notebooks/` - Interactive Jupyter notebooks
- `data/` - Sample datasets
- `exercises/` - Practice problems
- `src/` - Reusable Python utilities
- `docs/` - Additional documentation

## 🤝 Contributing

Contributions are welcome! Please read [CONTRIBUTING.md](CONTRIBUTING.md) for details.

## 📝 License

This project is licensed under the MIT License - see [LICENSE](LICENSE) file for details.

## 📧 Contact

For questions or feedback, please open an issue or contact [your-email@example.com]

## 🙏 Acknowledgments

- resipy developers
- emagpy developers
- All contributors to this course

## 📚 Additional Resources

- [resipy documentation](https://gitlab.com/hkex/resipy)
- [emagpy documentation](https://gitlab.com/hkex/emagpy)
