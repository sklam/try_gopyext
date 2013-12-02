all: bar.so

bar.so: foo.o bar.c
	gcc -shared -o bar.so foo.o bar.c

foo.o: foo.go
	gccgo -shared -c foo.go -o foo.o -fgo-prefix=example

clean:
	rm -f bar.so *.o


