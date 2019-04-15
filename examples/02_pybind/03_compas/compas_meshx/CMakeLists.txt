cmake_minimum_required(VERSION 3.12)
set(CMAKE_CXX_STANDARD 11)

# Eigen
find_package(Eigen3 3.3 REQUIRED)

# Pybind11
set(PYBIND11_CPP_STANDARD -std=c++11)
set(PYBIND11_PYTHON_VERSION 3.7)
set(PYTHON_EXECUTABLE "$ENV{CONDA_PREFIX}/bin/python3.7")
add_subdirectory(${CMAKE_CURRENT_SOURCE_DIR}/ext/pybind11)

# Libigl
find_package(LIBIGL REQUIRED)

# add the extension modules folder
add_subdirectory(${CMAKE_CURRENT_SOURCE_DIR}/modules)
