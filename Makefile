CXX = g++
CXXFLAGS = -std=c++17 -Iinclude -I/opt/homebrew/include -Iexternal/SoftPosit/source/include
LDFLAGS = -L/opt/homebrew/lib
LIBS = external/SoftPosit/build/Linux-x86_64-GCC/softposit.a -lmpfr -lgmp

SRCS = src/main.cpp \
       src/ieee.cpp \
       src/posit.cpp \
       src/mpfr_ref.cpp \
       src/benchmarks.cpp \
       src/utils.cpp

OBJS = $(SRCS:.cpp=.o)
TARGET = main

all: $(TARGET)

$(TARGET): $(OBJS)
	$(CXX) $(CXXFLAGS) $(LDFLAGS) -o $(TARGET) $(OBJS) $(LIBS)

%.o: %.cpp
	$(CXX) $(CXXFLAGS) -c $< -o $@

clean:
	rm -f $(OBJS) $(TARGET)

.PHONY: all clean
