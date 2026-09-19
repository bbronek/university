<div align="center">

# University Coursework

**Seven semesters of computer science, from first algorithms to machine learning.**

Python · C · C++ · Java · Ruby · Haskell · Prolog · R · SQL · Web

[Explore the archive](#explore-the-archive) · [Run an exercise](#run-an-exercise) · [Machine learning](#machine-learning-project) · [Checks](#checks-and-formatting) · [Reports](#reports-and-reference-material)

</div>

---

## Explore the archive

Each course contains independent exercises. Lab numbers preserve the original course sequence; there is no single application to build.

| Semester | Courses | What you will find |
|:---:|---|---|
| **1** | [Programming foundations](semester1/programming-foundations/), [algorithms and data structures](semester1/algorithms-and-data-structures/), [operating systems](semester1/operating-systems/) | Console exercises, searching and sorting, stacks, queues, binary search trees, text processing, matrix multiplication, and a POSIX microshell. |
| **2** | [Linear algebra](semester2/linear-algebra/), [object-oriented programming](semester2/oop/), [databases](semester2/databases/), [internet technologies](semester2/internet-technologies/) | Permutations, modular arithmetic, row reduction, Java class examples and registries, a vehicle-dealership schema, database connections, flight analysis, and HTML/CSS exercises. |
| **3** | [Discrete mathematics](semester3/discrete-mathematics/), [computer networks](semester3/computer-networks/) | Graph representations, breadth-first traversal, TCP and UDP programs, and a Java server with a Python client for 5 × 5 tic-tac-toe. |
| **4** | [Numerical methods](semester4/numerical-methods/), [declarative programming](semester4/declarative-programming/) | Root finding, numerical integration, Horner evaluation, SOR, a Scilab spline exercise, Haskell lists and trees, a Boolean-expression parser, and a Prolog dog-selection system. |
| **5** | [Formal languages](semester5/formal-languages/), [object-oriented analysis and design](semester5/object-oriented-analysis-and-design/) | Regular expressions, nondeterministic automata, recursive grammar parsing, Thrax grammars, and a Ruby ATM prototype. |
| **6** | [Scheduling](semester6/scheduling/), [statistics](semester6/statistics/), [cryptanalysis](semester6/elements-of-cryptanalysis/), [microcontrollers](semester6/microcontrollers/) | Scheduling heuristics and dynamic programming, statistical estimation and classification, educational RSA/ElGamal implementations, cipher reports, and an Mbed reaction timer. |
| **7** | [Machine learning](semester7/machine-learning/) | Matrix operations, visualization, regression, classification, clustering, Keras/PyTorch examples, and Swiss house-type prediction. |

### A few starting points

- **Data structures:** [linked list](semester1/algorithms-and-data-structures/python/linked_list.py) and [binary search tree](semester1/algorithms-and-data-structures/python/bst.py).
- **Systems:** [microshell](semester1/operating-systems/microshell/) supports `cd`, quoted arguments, external commands, and `> file` redirection. `grep` and `sort` use the installed system commands. Pipelines, variable expansion, and job control are outside its scope.
- **Languages:** [automata runner](semester5/formal-languages/non-deterministic-finite-automata/) includes input/output fixtures; the [grammar parser](semester5/formal-languages/recursive-grammar-parser/) explores production alternatives for grammars without left recursion.
- **Optimization:** [NEH flow-shop scheduling](semester6/scheduling/lab10/task2.py) and [weighted on-time task selection](semester6/scheduling/lab7/task3.py).

## Run an exercise

Run these commands from the repository root. Most console exercises read their input from standard input. Python programs with bundled datasets resolve those files relative to their source files.

### Python

Use Python **3.10 or newer**. Most early exercises use only the standard library.

```sh
python semester1/algorithms-and-data-structures/python/linked_list.py
printf '2 3\n1 2 3\n4 5 6\n' | python semester2/linear-algebra/rref.py
python semester6/elements-of-cryptanalysis/week-5/rsa_chinese_remainder.py
```

For numerical and machine-learning work, create an environment and install the scientific packages:

```sh
python -m venv .venv
. .venv/bin/activate
python -m pip install numpy pandas scikit-learn matplotlib
python semester7/machine-learning/lab5/main.py
```

Install `tensorflow` for the Keras examples and the project's neural network, or `torch` for the PyTorch example. Plotting exercises open a window; set `MPLBACKEND=Agg` when running checks without a display.

### C and C++

Compile exercises separately. Use a C11 compiler for `.c` files and a C++17 compiler for `.cpp` files. The operating-system and networking exercises target POSIX/Linux.

```sh
cc -std=c11 -Wall -Wextra semester1/algorithms-and-data-structures/c/lab4/merge_sort.c -o /tmp/merge-sort
printf '5\n4 1 5 2 3\n' | /tmp/merge-sort

make -C semester1/operating-systems/microshell
./semester1/operating-systems/microshell/microshell
```

The lab 3 TCP server accepts newline-delimited integers on port **8888** and returns each integer plus one. The UDP echo and TCP chat examples also default to port **8888**; run one server at a time.

### Java

Use a JDK **11 or newer**, and compile one exercise directory at a time: several independent labs define classes with the same name.

```sh
mkdir -p /tmp/university-java
javac -d /tmp/university-java semester2/oop/students/src/*.java
java -cp /tmp/university-java MainStudent
```

For the network game, run the server in one terminal and the client in another:

```sh
javac -d /tmp/university-java semester3/computer-networks/lab5/TicTacToeServer.java
java -cp /tmp/university-java TicTacToeServer 8787
```

```sh
python semester3/computer-networks/lab5/tic-tac-toe.py
```

The server plays 100 rounds against a random opponent. Five marks in a row win; draws are reported separately. `YOUR_TURN` controls client moves, and successful players are appended to `results.txt` in the server's working directory.

The PESEL exercise validates the eleven-digit format and checksum; it does not validate the encoded birth date. Its checksum follows the [official PESEL specification](https://www.gov.pl/web/gov/czym-jest-numer-pesel). The included Gradle 6.7 wrapper is historical; use JDK 11 for that wrapper. The standalone checks also work with JDK 17.

### Other runtimes

| Area | Requirements and entry point |
|---|---|
| **Ruby ATM** | Run `bundle install` and `bundle exec rspec specs` from `semester5/object-oriented-analysis-and-design/prototype/atm`. Amounts are positive integers in minor currency units. |
| **Automata and regex** | Run `./run automaton.1.txt < in.1.txt` from the automata directory. Regex runners require Bash and `grep`. |
| **Recursive grammar** | Run `ruby semester5/formal-languages/recursive-grammar-parser/run`; one input expression per line. An optional argument selects a grammar file. |
| **Haskell** | Load one lab at a time in GHCi. Lab 6 imports the adjacent `ListSet.hs`; lab 9 requires `parsec`. |
| **Prolog** | Load the desired `.pl` file in SWI-Prolog. Start the dog-selection system with `main.` and end menu answers with a period. |
| **R** | Run individual files with `Rscript`. The QDA exercises require `MASS`. Rendering `analysis.Rmd` needs `DBI`, `odbc`, `knitr`, `rmarkdown`, the original database, and a document renderer. |
| **SQL connections** | The dealership schema targets SQL Server. Java needs MySQL Connector/J on the classpath and exported variables from `.env.example`; Ruby needs the `pg` and `dotenv` gems. Credentials are not included. |
| **Scilab / Thrax** | Open `spline.sce` in Scilab; use `make` in `car-brands-thrax` with `thraxcompiler` installed. |
| **Mbed** | The reaction timer requires a compatible board, Mbed OS, an LED on `PA_10`, and an active-low button on `PC_13`. The host compiler cannot build it without the board SDK. |

## Machine-learning project

The canonical project is [`semester7/machine-learning/project`](semester7/machine-learning/project/).

The house-prices CSV is **not included**. Obtain the [Switzerland House Price Prediction Data](https://www.kaggle.com/datasets/etiennekaiser/switzerland-house-price-prediction-data), then pass the CSV path explicitly or save it as `house_prices_switzerland.csv` beside `main.py`. The expected columns include `HouseType`, `Size` (`S`, `M`, `L`), `Balcony`, and `Locality`.

```sh
python semester7/machine-learning/project/main.py /path/to/house_prices_switzerland.csv --skip-neural-network
```

Remove `--skip-neural-network` after installing TensorFlow to include the neural-network model. The script compares regularized and unregularized logistic regression, Gaussian naive Bayes, and the optional neural network. It splits the data before fitting preprocessing and reports accuracy, weighted precision, recall, and F1.

The [English results report](semester7/machine-learning/project/report.pdf) preserves the original recorded scores. It also explains the differences between the original report's model descriptions and the implementation. Those historical scores have not been reproduced from the missing source dataset.

Included lab datasets cover fires/thefts, Titanic passengers, communities, apartment clustering, and avocado sales. The apartment dataset's column labels and floor categories are in English. Proper names and original cryptanalysis sample texts retain their original spelling.

## Validation and formatting

The refactor was checked with GCC/G++, Java 17, Ruby, and the scientific Python dependencies. All three JUnit tests and all nine RSpec examples passed. Haskell files were parsed and formatted with Ormolu. The English reports were rendered and visually inspected.

Full execution of R, Haskell, Prolog, Scilab, Thrax, Mbed, external database connections, and TensorFlow/PyTorch training requires additional environments and was not validated here. The standalone project classifiers were checked with synthetic data, not the missing house-prices dataset. The three-machine scheduling exercise uses a Johnson-style reduction whose optimality depends on the usual processing-time conditions; NEH and local search are heuristics.

Formatting conventions are recorded in [`.editorconfig`](.editorconfig) and [`.clang-format`](.clang-format): UTF-8, LF line endings, consistent indentation, and Black-formatted Python (88 columns). Generated build outputs, caches, and local environments are ignored. Previously generated files may remain locally, but are no longer tracked.

## Reports and reference material

- [Machine-learning results, in English](semester7/machine-learning/project/report.pdf).
- [Flight-delay analysis, in English](semester2/databases/flight-analysis/analysis.pdf), with editable queries in [analysis.Rmd](semester2/databases/flight-analysis/analysis.Rmd).
- [Cryptanalysis reference PDFs](semester6/elements-of-cryptanalysis/): fitness plots, Playfair experiments, S-box analysis, and an SPN design.

The cryptanalysis PDFs were reviewed as historical coursework. Their explanatory text is already English; Polish, German, and Lithuanian passages are experimental plaintext. They are not validated implementations: the SPN S-box repeats output `1001` and omits `0000`; the S-box analysis contains an incomplete difference table; and the embedded Playfair listing contains n-gram boundary errors and an unbounded retry loop. Their original experimental records have been preserved.

The small-key cryptography examples demonstrate algorithms and are not suitable for protecting real data. Teaching examples retain their course context, including the Java material attributed to Bruce Eckel and the network-game lineage from Deitel and Deitel.
