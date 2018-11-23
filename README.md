# IPython Coverage
An IPython Cell Magic to Run Coverage from Jupyter notebook / JupyterLab.

Presents the coverage HTML report as an IFrame.

# Installation

    pip install ipycoverage
    
# Usage

### Load the extension
    %load_ext ipycoverage

### Use the magic
```python
%%coverage
from your_module import your_function  # or your calss

your_module.your_function()
```

> This is not a fully developed magic, it has only been tested against:
> * `coverage==4.5.2`
> * `IPython==7.0.1`.
> * `JupyterLab==0.35.1`

## Missing Features / Future Work
* Add more options (potentially dynamically load them from `coverage`).
* Add tests.
