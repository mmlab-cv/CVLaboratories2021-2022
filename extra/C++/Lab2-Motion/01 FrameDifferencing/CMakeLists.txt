cmake_minimum_required(VERSION 2.8)
project( frameDifferencing )
find_package( OpenCV REQUIRED )
include_directories( ${OpenCV_INCLUDE_DIRS} )
include_directories( ${PROJECT_SOURCE_DIR} )
add_executable( frameDifferencing frameDifferencing.cpp )
target_link_libraries( frameDifferencing ${OpenCV_LIBS} )
