# Use DDD and CQRS patterns for family_users module

**Status:** _accepted_.

## Context

We need to handle few actions in family_users module:
- auth user
- create user and subuser account
- add user/subuser profiles
- edit user/subuser account
- list and get user/subuser data

## Decision

* We decided to use DDD (Domain-Driven Design) and CQRS (Command Query Responsibility Segregation) but without event sourcing. In this module we have minimal amount of business logic and do not have closed processes.

## Consequences

Be strict and stick to the DDD and CQRS guidelines to do this module right.

## Alternatives

We could use RDS architecture, but we decided to share the knowledge of DDD across a team.

## Decision date

> 2022-04-11
