build:
	cd jemdoc_files
	./jemdoc -o ../ *.jemdoc
	cd ..

run:
	php -S localhost:8000