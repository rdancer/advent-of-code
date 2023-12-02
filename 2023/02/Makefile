.PHONY: all clean solution1.txt solution2.txt
all: solution1.txt solution2.txt
	@test -e input.txt || { echo "Input data not found. Please log into your account on adventofcode.com and save the input data as 'input.txt'." >&2; exit 1; }

solution1.txt:
	python3 solution1.py | tail -n1 | tee $@

solution2.txt:
	python3 solution2.py | tail -n1 | tee $@

