# A simple makefile for CSE 100 P3

CC=g++
CXXFLAGS=-std=c++11 -g -Wall
LDFLAGS=-g

all: predict util.o

predict: predict.cpp util.o DictionaryTrie.o DictionaryBST.o DictionaryHashtable.o

DictionaryTrie.o: DictionaryTrie.hpp 

DictionaryBST.o: DictionaryBST.hpp

DictionaryHashtable.o: DictionaryHashtable.hpp

util.o: util.hpp



clean:
	rm -f predict *.o core* *~

