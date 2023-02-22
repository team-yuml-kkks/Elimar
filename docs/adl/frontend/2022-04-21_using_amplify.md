# Using AWS Amplify to integrate with Cognito

**Status:** _accepted_.

## Context

* We're outsourcing authentication to separate system,
* We will use Cognito as authentication system.
* We need to provide custom views, so we will
have to use Cognito API.

## Decision

We decided to use [aws-amplify](https://www.npmjs.com/package/aws-amplify).
This library is supported by AWS and it's recommended solution
by them. What's more we already have some experience using it,
so we won't have to learn everything from the scratch.

## Consequences

We will need to install and setup additional dependency.

## Alternatives

We could integrate with Cognito ourselves but then
it would take much more time.

## Decision date

> 2022-04-25
