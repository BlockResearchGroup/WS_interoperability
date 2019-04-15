# CMakeLists.txt

cmake_minimum_required(VERSION 3.12)
set(CMAKE_CXX_STANDARD 11)

project(basic)

# Pybind11
set(PYBIND11_CPP_STANDARD -std=c++11)
set(PYBIND11_PYTHON_VERSION 3.7)
set(PYTHON_EXECUTABLE "$ENV{CONDA_PREFIX}/bin/python3.7")
add_subdirectory(${CMAKE_SOURCE_DIR}/ext/pybind11)

pybind11_add_module(basic MODULE basic.cpp)

set_target_properties(basic PROPERTIES LIBRARY_OUTPUT_DIRECTORY "${CMAKE_SOURCE_DIR}")
