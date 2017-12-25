cmake_minimum_required(VERSION 3.6)
project(sumoSwarmed)

set(CMAKE_CXX_STANDARD 11)

set(SOURCE_FILES
        MainLan.cc
        MainSeq.cc
        MainWan.cc
        mpi.h
        PSO.hh
        PSO.pro.cc
        PSO.req.cc
        PSOstructures.hh)

add_executable(sumoSwarmed ${SOURCE_FILES})