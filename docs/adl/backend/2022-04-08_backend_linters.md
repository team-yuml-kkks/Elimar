# Using mypy, pylint and black

**Status:** _accepted_.

## Context

We want to create better, cleaner code. Furthermore create double check our work.

## Decision

To do it we decided to use additional libraries:
- mypy - static type checker
- pylint - linter to statically analyze the code
- black - code formatter

All those libraries also is used in github workflows. Which will check code on every pull request.

## Consequences

All configuration, we will have to do manually. Furthermore, we will need to take care about libraries versions and eventually CI issues.

## Alternatives

* We can use other alternatives librares. But we worked with mypy, pylint, black before and this setup work pretty well and meets the current requirements.

## Decision date

> 2022-04-08
