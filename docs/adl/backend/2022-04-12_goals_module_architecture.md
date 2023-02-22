# goals module architecture

**Status:** _accepted_.

## Context

* The module will simply save and read data from database.
* There is no advanced logic.

## Decision

We decided to use `layered` architecture in the `goals` module.
The module does not need high-testability of business logic
because there is almost no logic at all, only database integration.

## Consequences

We will simplify the module by using `layered` architecture.

## Alternatives

Using `Hexagon` would be an overkill in this case. There is no logic
we would like to test.

## Decision date

> 2022-04-12
