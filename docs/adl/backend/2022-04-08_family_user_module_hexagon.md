# Use hexagonal architecture for family_users module

**Status:** _accepted_.

## Context

We need to build module to create, edit and list users and subusers accounts.

## Decision

We decided to use for this module hexagon architecture. Because we will have outside integration with S3 storage provider.

## Consequences

Module build with hexagon will be significantly more complex than using layered architecture.We will need to stick to the guidelines of hexagon architecture. Also, we need to create a lot more code than usually.

## Alternatives

We could use layered architecture, which would generate less code and propably take less time.

## Decision date

> 2022-04-11
