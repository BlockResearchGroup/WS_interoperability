cmake_minimum_required(VERSION 3.12)
set(CMAKE_CXX_STANDARD 11)

project(compas_meshx)

pybind11_add_module(isolines MODULE isolines.cpp)
pybind11_add_module(planarization MODULE planarization.cpp)

target_link_libraries(isolines PRIVATE igl::core)
target_link_libraries(planarization PRIVATE igl::core)

set_target_properties(isolines PROPERTIES LIBRARY_OUTPUT_DIRECTORY "${CMAKE_SOURCE_DIR}/src/compas_meshx/isolines")
set_target_properties(planarization PROPERTIES LIBRARY_OUTPUT_DIRECTORY "${CMAKE_SOURCE_DIR}/src/compas_meshx/planarization")
