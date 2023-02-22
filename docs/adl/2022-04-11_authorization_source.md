# Authorization source

**Status:** _accepted_.

## Context

* We need to login user to the system,
* We want to outsource login system to another platform.

## Decision

We decided to use [AWS Cognito](https://aws.amazon.com/cognito/) authorization system.
We used `Cognito` before and we have knowledge how to set it up. Furthermore,
our entire system will use AWS ecosystem, so we decided that 
authorization system should use that as well.

## Consequences

We will need to setup Cognito userpool.

## Alternatives

We could use [Auth0](https://auth0.com/) or [supertokens](https://supertokens.com/)
but we never used it before in production.

## Decision date

> 2022-04-11
