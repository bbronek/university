all: main.far

main.far: main.grm
	thraxcompiler --input_grammar=$< --output_far=$@

.PHONY: all clean
clean:
	rm -f main.far
