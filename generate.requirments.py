markdown_table = """
|Package|Purpose|Homepage|PyPI|⭐ on Github|Forks on Github|Version|Latest release date|License|Are the bugs in GH issues?|
|-------|-------|--------|----|------------|---------------|-------|-------------------|-------|--------------------------:|
|Flask|A simple framework for building complex web applications|[link](https://flask.palletsprojects.com/en/2.2.x/)|[link](https://pypi.org/project/Flask/)|62260|15503|3.0.0|15 February, 2023|BSD|Yes|
|Requests|Python HTTP for Humans|[link](https://docs.python-requests.org/en/master/)|[link](https://pypi.org/project/requests/)|45766|8390|2.31.0|18 July, 2021|Apache 2.0|Yes|
|Tabulate|Pretty-print tabular data in Python|[link](https://github.com/astanin/python-tabulate)|[link](https://pypi.org/project/tabulate/)|1845|188|0.9.0|Oct 6, 2022|MIT License (MIT)|Yes|
|NumPy|Essential for numerical computing, providing support for arrays, matrices, and mathematical operations|[link](https://numpy.org/)|[link](https://pypi.org/project/numpy/)|25148|8881|1.26.2|Nov 12, 2023|BSD License|Yes|
|Pandas|Offers high-performance data manipulation and analysis tools|[link](https://pandas.pydata.org/)|[link](https://pypi.org/project/pandas/)|40531|16999|2.1.3|Nov 10, 2023|BSD License|Yes|
|PyGame|library for the development of multimedia applications like video games using Python|[link](https://www.pygame.org/)|[link](https://pypi.org/project/pygame/)|6551|2922|2.5.2|Sep 18, 2023|GNU Library or Lesser General Public License (LGPL) (LGPL)|Yes|
|Pytest|A testing framework for writing simple unit tests|[link](https://docs.pytest.org/en/latest/)|[link](https://pypi.org/project/pytest//)|10858|2455|7.4.3|Oct 24, 2023|MIT License (MIT)|Yes|
|Matplotlib|Matplotlib is a comprehensive library for creating static, animated, and interactive visualizations|[link](https://matplotlib.org/)|[link](https://pypi.org/project/matplotlib/)|18524|7330|3.8.2|Nov 17, 2023|Python Software Foundation License (PSF)|Yes|
|SymPy|library for symbolic mathematics|[link](https://sympy.org//)|[link](https://pypi.org/project/sympy/)|11608|4143|1.12|May 10, 2023|BSD License (BSD)|Yes|
|Dash|From exploring data to monitoring your experiments, Dash is like the front end to the analytical Python backend|[link](https://plotly.com/dash)|[link](https://pypi.org/project/dash/)|19738|2017|2.14.2|Nov 28, 2023|MIT License (MIT)|Yes|
"""

lines = markdown_table.strip().split('\n')

requirements = []

for line in lines[2:]: 
    parts = line.split('|')
    package = parts[1]
    version = parts[7]
    requirements.append(f"{package}=={version}")

with open('requirements.txt', 'w') as file:
    for requirement in requirements:
        file.write(f"{requirement}\n")
