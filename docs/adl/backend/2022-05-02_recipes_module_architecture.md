# Recipes module architecture

**Status:** _accepted_.

## Context

We need to handle a few actions in this module:
- set / unset favorite recipes
- list favorite recipes

## Decision

We decided to use 2-layered architecture for the `recipes` module.

## Consequences

We will simplify the code but it will less testable.

## Alternatives

We could use Hexagon architecture/DDD but it would be overhead in this module.

## Decision date

> 2022-05-02
