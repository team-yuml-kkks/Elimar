# Backend testing setup

**Status:** _accepted_.

## Context

We need libraries for testing the backend application.

## Decision

- We've decided to use hypothesis because it's the only
  python library which supports property based testing.
- We've decided to use Faker for integration tests
  like database integrations.

## Consequences

- We have to create property based tests with hypothesis
- The Hypothesis can have poor performance (especially with complicated
  generators).
- We have to create faker providers to support our DTOs

## Alternatives

- We could use `unittest` instead but we have
  more knowledge about the `pytest`

## Decision date

> 2022-04-12
