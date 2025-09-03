# Welcome
Thank you for taking interest in pyham and more so for considering contributing.

# Contributing guidelines
1. Be sure to create issues according to template(s) to communicate new features and/or bugs you wish someone to work on. Issues are, in part, a place for discussion, so whenever you consider contributing, be sure to make your intentions clear with an issue.
2. Be sure to create pull requests according to template(s) to discuss the code you want to contribute.

# Code of conduct
Just be a decent human, I guess?

# Codebase overview
## Top level overview
Here is a brief insight into the way I organized the code for the project. Please accept this and the comments in source files as my best attempt at documentation.

pyham40k has one real dependency - rich. It used mainly for cross-platform console buffer manipulation.

pyham40k has two top-level modules: core and cli. 
1. [core](src/pyham40k/core/) contains all the logic of Warhammer rules, data models and parsers.
2. [cli](src/pyham40k//cli/) depends on core and provides the command line interface.

Project root contains [test](test/) directory, where tests written with python's unittest reside. Technically, not all of those tests can be called unit tests. Still, it is highly recommended to write tests for any code that is contributed. My main reasons for writing tests include:
1. Ensuring rules and required behavior are fullfilled by the code (at least on a small set of examples and/or equivalent classes);
2. Testing API. Is it practical and/or convenient to make calls to the code in a certain way?
3. Providing examples;

## core overview
core consists of several submodules:
1. [calculator](src/pyham40k/core/calculator/). Encapsulates all wh40k 10e rules and operates on data models.
[Base_Calculator_Strategy](src/pyham40k/core/calculator/base_calculator_strategy.py) describes a base strategy class that realizes the algorithm described in [README](README.md#2-methodology) with calculate_total_unsvaed_wounds() method. Subclasses like [Real_Calculator](src/pyham40k/core/calculator/real_calculator.py) or [Floor_Calculator](src/pyham40k/core/calculator/floor_calculator.py) must override methods that calculate_total_unsvaed_wounds() calls (these methods correlate with algorithm steps in [README](README.md#2-methodology)).

2. [model](src/pyham40k/core/model/). Enforces data constraints and handles conversions between deferent representations.
model submodule contains:
- [Format_Exception](src/pyham40k/core/model/format_exception.py) that is raised whenever there is an inconsistency in string representations of other model classes (such inconsistencies arise from user input). 
- [Reroll](src/pyham40k/core/model/reroll.py) that is responsible for reroll representation.
- [value](src/pyham40k/core/model/value/) submodule that manages value representation according to [README](README.md#3-notation). Random, Simple and Not Assigned values are subclassed of the [Base_Value](src/pyham40k/core/model/value/base_value.py). Simple values are further differentiated into Positive and Non-Positive values. Lastly, [Value_Flyweight](src/pyham40k/core/model/value/value_flyweight.py) is a singleton (in form of a static class) that is responsible for creating non-duplicate value objects. That is mainly a preparation for dealing with many more values of many profiles.
- [attacker](src/pyham40k/core/model/attacker/) and [defender](src/pyham40k/core/model/defender/) modules manage profile representation and validation. Both of these modules provide builder classes for instantiating profiles from a series of values (mainly used in case of interactive input).

3. [parser](src/pyham40k/core/parser/). Helps parse more complex models (profiles) from full strings ([Simple_Parser](src/pyham40k/core/parser/simple_parser.py)) or interactive input ([Simple_Scanner](src/pyham40k/core/parser/simple_scanner.py)).

## cli overview
cli has its own model classes and several other submodules:
1. [model](src/pyham40k/cli/model/). This module consists of:
- [Cli_Choice](src/pyham40k/cli/model/cli_choice.py) class, that bundles data for a choice (or option, in other words) for some action in cli. Mainly, this model class relates choice to the inputs that select it. Additionally, string representations for choices are also managed here.
- [Cli_Prompt](src/pyham40k/cli/model/cli_prompt.py) class, that bundles several choices and a prompt that asks user for input.
- [Cli_File_Prompt](src/pyham40k/cli/model/cli_file_prompt.py) class, handles input of a generic file path. Not validated.

2. [Cli_Controller](src/pyham40k/cli/cli_controller.py) contains cli logic. Mainly checks user input to be one of the choices and routes user's input to actual code.

3. [constants](src/pyham40k/cli/constants.py) is a module that includes instances of prompts and choices that can be used to write cli logic. 
