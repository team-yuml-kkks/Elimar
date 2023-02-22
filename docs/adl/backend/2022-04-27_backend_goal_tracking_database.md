# Badges DB choice

**Status:** _accepted_.

## Context

We need database to store goal tracking.

## Decision

We decided to follow other modules and use Postgres to store user progress(goal tracking).

## Consequences

We will need to setup another Postgres container.

## Alternatives

We could use MySQL or more non-relational database.

## Decision date

> 2022-04-27
