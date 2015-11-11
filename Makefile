CXX=clang++
CXXFLAGS=-O3 -Wall -Werror -pedantic -std=c++14

read: read.cc

clean:
	rm -f read
