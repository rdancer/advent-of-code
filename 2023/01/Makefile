.PHONY: all
all:
	@test -e input.txt || { echo "Input data not found. Please log into your account on adventofcode.com and save the input data as 'input.txt'." >&2; exit 1; }
	make solution1.txt
	make solution2.txt

solution1.txt:
	python3 solution1.py | tail -n1 | tee $@

solution2.txt:
	python3 solution2.py | tail -n1 | tee $@
