cmake_minimum_required(VERSION 3.23)

project({{Project}}-workspace)

include(${CMAKE_BINARY_DIR}/conanworkspace.cmake)
conan_workspace_subdirectories()
