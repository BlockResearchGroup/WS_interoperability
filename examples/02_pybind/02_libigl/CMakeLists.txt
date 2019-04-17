cmake_minimum_required(VERSION 3.12)
set(CMAKE_CXX_STANDARD 11)
set(CMAKE_MODULE_PATH ${CMAKE_MODULE_PATH} "${CMAKE_SOURCE_DIR}/cmake")

# if(MSVC)
# 	add_definitions(-D_ENABLE_EXTENDED_ALIGNED_STORAGE=1)
# 	set(CMAKE_RUNTIME_OUTPUT_DIRECTORY "${CMAKE_SOURCE_DIR}/modules/")
# endif()

# message(${CMAKE_MODULE_PATH})
# set(EIGEN3_INCLUDE_DIR "${CMAKE_SOURCE_DIR}/ext/eigen")
# find_package(Eigen3 REQUIRED)
# include_directories(${EIGEN3_INCLUDE_DIR})

# Pybind11
set(PYBIND11_CPP_STANDARD -std=c++11)
set(PYBIND11_PYTHON_VERSION 3.7)
if (WIN32)
	set(PYTHON_EXECUTABLE "C:\\Users\\user\\Anaconda3\\envs\\interop\\python.exe")
else ()
	set(PYTHON_EXECUTABLE "$ENV{CONDA_PREFIX}/bin/python")
endif()
add_subdirectory(${CMAKE_SOURCE_DIR}/ext/pybind11)

# Libigl
find_package(LIBIGL REQUIRED)

# add the extension modules folder
add_subdirectory(${CMAKE_SOURCE_DIR}/src)
