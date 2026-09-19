# Nondeterministic finite automata

Run an example from this directory:

```sh
./run automaton.1.txt < in.1.txt
```

State `0` is the start state. A line containing one state marks an accepting
state; a three-field line defines `source destination character`.
Each input line is a separate word. The output is `yes` or `no`.
Both `1` and `3` have matching `automaton`, `in`, and `out` sample files.
