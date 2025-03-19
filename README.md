# Bezier-surfaces-and-geological-structures

We use Bézier surfaces to obtain a 3D model of a geological structure


How to use

The data directory contains all the data needed to build the model. These data are saved in csv files that must be read during model building.

The code can be found in the repository, it can be downloaded as ZIP by clicking in the green Code button. There are five Jupyter notebooks in which the process is fully described. The order in which these notebooks should be read is as follows:

- geological_map.ipynb
- crossed_sections.ipynb
- 3dtopography.ipynb
- 3dcomplete_model.ipynb
- blocks.ipynb
  
The figures directory contains png image files with the cross section representations and html files with the 3d models. Note that the html files in this directory may be larger than GitHug supports, so to be viewed they must be downloaded and opened in a local web browser

Download the code

The code can be found in the repository, it can be downloaded as ZIP by clicking in the green Code button. The necessary files are the five Jupyter notebook mentioned above. In these notebook we use libraries and packages like: plotlib, matplotli, pandas, numpy, sympy, etc. that must be imported at the begining. 


We also use the files copernico.py https://github.com/carlosg-m/goose-lab and bezier.py from the repository https://github.com/torresjrjr/Bezier.py. This file is also hosted here.

To reduce the code in the notebooks we have created files like: functions.py, topo.py, sector1.py, sector2.py, sector3.py and sector4.py that can be found in this repository

How to run the notebook

You can run the notebooks in Jupyter-Notebook or Visual Studio Code, you also need a Python kernel installed in your computer with all the libraries and packages installed.

To successfully run the notebook, you need to locate it in the same folder as the data directory and the files .py. In order to do this, you may just extract the ZIP file with the whole repository. Then, launch Jupyter Notebook and select the notebook geologicalmap.ipynb. 

You're now ready to go!

Authors:

Manuel Bullejos, Manuel Martín-Martín
