# Setup database container for family_users module

**Status:** _accepted_.

## Context

We need to place to store users data.

## Decision

We decided to create docker container with [PostgreSQL](https://www.postgresql.org/).

## Consequences

We need to create additional container with database. Also, postgresql could be slower than MySQL on performance metrics. But we use PostgreSQL in other containers, so to be consistent we selected PostgreSQL.

## Alternatives

We could use [MySQL](https://www.mysql.com/) database in docker container.

## Decision date

> 2022-04-11
