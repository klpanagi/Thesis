cmake_minimum_required(VERSION 2.8)
project( CvtColorPerfTest )
find_package( OpenCV REQUIRED )


add_executable( cvtColorTest runTest.cpp cvtColorTest.cpp )
target_link_libraries( cvtColorTest testEngine testBase ${OpenCV_LIBS} )
