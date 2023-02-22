# Add Inject library

**Status:** _accepted_.

## Context

We need to integrate with S3 in family_users module in which we use hexagon architecture.

## Decision

We decided to use [Inject](https://github.com/ivankorobkov/python-inject) to automatically injects arguments for integration with S3.

## Consequences

We will need to take care about library versions and eventually issues related with library.

## Alternatives

We would use other dependency injector lib like [Injector](https://github.com/alecthomas/injector). But we worked with Injector before and this works well and meets the current requirements.
## Decision date

> 2022-04-11
