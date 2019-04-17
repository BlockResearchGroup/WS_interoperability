# Commands

An overview of useful command line instructions and code snippets...


## conda


```bash
conda info --envs
```
Get a list of all virtual environments created and managed by `conda`.


```bash
conda create -n <environment name> [python=<semantic versioning number>]
```
Create a virtual environment.
Optionally, specify the Python version.
If no Python version is specified, the environment wil use the same Python as the base environment.


```bash
conda activate <environment name>
```
Activate a specific environment.


```bash
conda install COMPAS[=<semantic versioning number>]
```
Install COMPAS in the active environment.
Optionally, specify the version of COMPAS.
If the version of COMPAS is not specified, the latest version available on `conda` will be installed.


```bash
conda remove -n <environment name> --all
```
Delete an environment.
Note that you need to deactivate the environment first.


## pip


```bash
pip install -e .
```
Create an *editable* "from source" install of the package in the current folder.
Note that the current folder should contain the `setup.py` script of the package.
With an *editable* install, you can keep working on the code or keep it synchronised
with an online repository, without having to install it over and over again.

Note that even with *editable* installs, not all changes will always have an immediate
effect. For example, changes you make while an interactive Python session is running will only
have an effect after the session is restarted. The same is true for Rhino/GH and Blender.
If Rhino/GH and/or Blender are running while you make changes to an editable package,
those changes will only have an effect after restarting the software.
Conveniently, in Rhino on Windows, you can simply reset the script engine.
However, this is currently not possible in Rhino on Mac and also not in Blender (AFAIK).


```bash
pip install -r requirements-dev.txt
```
Install all development requirements of a package and at the same time create an
editable install.


```bash
pip uninstall <package name>
```
Uninstall a package previously installed with `pip`.


## COMPAS

```bash
python -m compas_rhino.uninstall
```


```bash
python -m compas_rhino.install [-v <version number>] [-p <list of package names>]
```

## CMake

```bash
# On Mac
# starting from the folder containing the top level CMakeLists.txt

mkdir build
cd build
cmake -DCMAKE_BUILD_TYPE=Release ..
make -j4
```

```bash
# On Windows
# starting from the folder containing the top level CMakeLists.txt

mkdir build
cd build
cmake -DCMAKE_BUILD_TYPE=Release -G"Visual Studio 15 2017 Win64" ..
cmake --build . --config Release -- -j4
```
