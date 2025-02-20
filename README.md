
# SVCK: SystemVerilog Checker - Linter

**SVCK** is an open-source linter tool designed to enforce style and consistency rules for SystemVerilog code. It provides a framework for **Build Your Own Linter** (**BYOL**), allowing users to create their own custom lint rules while benefiting from built-in checks such as proper encapsulation, naming conventions, line spacing, and other cosmetic rules. This linter integrates seamlessly into your development pipeline to ensure consistent, high-quality code.

## Table of Contents

1. [SVCK: SystemVerilog Checker - Linter](#svck-systemverilog-checker---linter)
2. [BYOL - Build Your Own Linter](#byol---build-your-own-linter)
3. [Open Source](#open-source)
4. [Directory Structure](#directory-structure)
5. [Installation](#installation)
6. [Usage](#usage)
   - [Running the Linter from Command Line](#running-the-linter-from-command-line)
   - [Running with Makefile (Optional)](#running-with-makefile-optional)
   - [Test Cases](#test-cases)
7. [Adding New Lint Rules](#adding-new-lint-rules)
8. [Example Rule (in `src/rules/`)](#example-rule-in-srcrules)
9. [Dependencies](#dependencies)
10. [License](#license)
11. [Credits](#credits)

## BYOL - Build Your Own Linter

The core concept of **SVCK** is **BYOL** (Build Your Own Linter), a framework that lets you easily define custom linting rules tailored to your specific needs. Whether it's enforcing naming conventions, checking for proper encapsulation, or any other rule, **SVCK** is flexible and extensible.

With **BYOL**, you can create new rules quickly and add them to your pipeline. The linter is fully customizable, empowering you to ensure that your SystemVerilog code adheres to your specific standards.

## Open Source

This project is **open source** and licensed under the MIT License. Contributions are welcome, and you are free to fork, modify, and distribute it according to your needs. We encourage you to contribute to the community by adding new rules, improving the existing ones, or integrating **SVCK** with other tools and environments.

## Directory Structure

```plaintext
SVCK/
├── bin/
│   ├── svck.py                # The main entry point script for running the linter
│   ├── verible_verilog_syntax.py  # Syntax parsing for SystemVerilog using Verible
├── examples/
│   ├── Makefile               # Example Makefile for running the linter on files
│   └── svck_verible_style.cfg  # Example configuration file for the linter
├── src/
│   ├── af_lint_rule.py        # Common lint rule functionality
│   ├── asfigo_linter.py       # Base linter class with core functionalities
│   └── rules/                 # Folder containing the specific lint rule implementations
├── tests/
│   ├── test_cl_encap.sv       # Test case for encapsulation rule
│   ├── test_cl_mixed_naming.sv # Test case for mixed naming rule
│   ├── test_hspace.sv         # Test case for horizontal space rule
│   ├── test_cl_gvar.sv        # Test case for global variable rule
│   ├── test_comments.sv       # Test case for comment styling rule
│   └── test_too_wide_line.sv  # Test case for line width rule
```

## Installation

1. Clone the repository:

```bash
git clone https://github.com/AsFigo/svck.git
cd svck
```

2. Install required dependencies - Verible mainly


See: https://github.com/chipsalliance/verible

## Usage

### Running the Linter from Command Line

The linter can be run using the `svck.py` script located in the `bin/` directory. This script checks SystemVerilog files against the defined style rules.

1. To run the linter on a specific file:

```bash
python bin/svck.py -t <path_to_file.sv>
```

2. If you want to specify additional configuration options for Verible built-in linter, you can use the `svck_verible_style.cfg` configuration file located in the `examples/` directory. The configuration defines which rules are enabled/disabled.

### Running with Makefile (Optional)

If you'd prefer to use a Makefile to automate running the linter, you can use the provided example `Makefile` in the `examples/` directory. This is especially useful for running lint checks across multiple files or integrating into a CI/CD pipeline.

To run the linter via Makefile, simply run:

```bash
make 
```

This will run the linter on the default files or those specified in the Makefile.

### Test Cases

The `tests/` directory contains various test cases written in SystemVerilog to test the linter's behavior. These tests cover various rules such as:

- **Encapsulation**: Tests for private vs public variables.
- **Mixed Naming**: Tests for mixed use of CamelCase and snake_case.
- **Horizontal Space**: Tests for spaces between operators, keywords, etc.
- **Global Variables**: Tests to ensure there are no global variables.
- **Commenting**: Tests for proper comment formatting.
- **Line Width**: Tests for line width exceeding the allowed limit.

You can add additional test cases in this directory to expand coverage.

### Adding New Lint Rules

1. Create a new Python file inside the `src/rules/` directory. Each file should contain a class that inherits from the base linter class (`AsFigoLinter`).
2. Implement the rule logic in the derived class. Each rule should implement a method like `apply` or `run` to check for the specific violation.
3. After implementing the rule, add the rule to the configuration to enable or disable it.

## Example Rule (in `src/rules/`)

```python
from src.af_lint_rule import AFLintRule

class NoGlobalVariablesRule(AFLintRule):
    def apply(self, file_path, file_data):
        for var in file_data.tree.find_all({"tag": "kDataDeclaration"}):
            if var.depth == 1:  # Global variable check
                self.linter.logViolation("R101", f"Found global variable: {var.text} in file: {file_path}", severity="ERROR")
```

## Dependencies

- Python 3.x
- Any necessary libraries like `verible_verilog_syntax`

## License

This project is **open source** and licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

This **SVCK** linter is part of the **BYOL** (Build Your Own Linter) framework from **AsFigo Technologies**. It's an open-source tool, and we encourage you to contribute to its growth, whether through adding new lint rules, improving existing ones, or enhancing documentation.

Let us know how you're using **SVCK**, and feel free to contribute back to the community!

## Credits

The rules and guidelines in **SVCK** are based on the following sources:

- **Mark Glasser's *Next Level Testbenches: Design Patterns in SystemVerilog and UVM***: Many of the rules in this linter are inspired by the coding practices and design patterns outlined in Mark Glasser's book, which provides a comprehensive approach to SystemVerilog and UVM testbenches, focusing on best practices for code quality and maintainability.

- **lowRISC Coding Guidelines**: This linter also draws upon the coding standards and guidelines from the lowRISC project. Their best practices for SystemVerilog coding have been a key resource for defining rules related to naming conventions, encapsulation, and other critical aspects of design quality.

- **Verible**: is an opensource SystemVerilog parser from Google and available via ChipsAlliance

