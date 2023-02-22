# Meal plans module architecture

**Status:** _accepted_.

## Context

We need to handle simple logic (mostly db integration)
for meal plans.

## Decision

We decided to use 2-layered architecture for the `meal_plans` module
as the logic is very simple here.

## Consequences

We will simplify the code but it will less testable.

## Alternatives

We could use Hexagon architecture/DDD but it would be overhead in this module.

## Decision date

> 2022-05-09
