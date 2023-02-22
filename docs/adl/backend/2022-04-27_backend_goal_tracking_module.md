# Goal tracking module

**Status:** _accepted_.

## Context

We need to handle a few actions in this module:
- tracking goal progress
- update/insert goal tracking
- get single goal(for tests)
- get list of goals

## Decision

We decided to use 2-layered architecture for the `goal_tracking` module.


## Consequences

We will simplify the code but it will less testable.

## Alternatives

We could use Hexagon architecture/DDD but it would be overhead in this module.

## Decision date

> 2022-04-27
