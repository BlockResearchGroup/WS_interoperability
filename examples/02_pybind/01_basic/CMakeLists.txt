# CMakeLists file for building a shared library called basic
# the shared library will expose the functionality of basic.cpp
# as a python module called basic
# the shared library will be built in the current directory

# to compile on Mac
#
# mkdir build
# cd build
# cmake -DCMAKE_BUILD_TYPE=Release ..
# make -j4

# to compile on Windows
#
# mkdir build
# cd build
# cmake -DCMAKE_BUILD_TYPE=Release -G"Visual Studio 15 2017 Win64" ..
# cmake --build . --config Release -- -j4

cmake_minimum_required(VERSION 3.12)
set(CMAKE_CXX_STANDARD 11)

project(basic)

# Pybind11
set(PYBIND11_CPP_STANDARD -std=c++11)
set(PYBIND11_PYTHON_VERSION 3.7)

# Setting the python executable like this
# will only work if you issue the build commands from
# the command line with the correct environment activated
if (WIN32)
    set(PYTHON_EXECUTABLE "$ENV{CONDA_PREFIX}/python.exe")
else()
    set(PYTHON_EXECUTABLE "$ENV{CONDA_PREFIX}/bin/python")
endif()

add_subdirectory(${CMAKE_SOURCE_DIR}/ext/pybind11)

# the basic module
pybind11_add_module(basic MODULE basic.cpp)

# properies of the target shared library
set_target_properties(basic PROPERTIES LIBRARY_OUTPUT_DIRECTORY "${CMAKE_SOURCE_DIR}")
