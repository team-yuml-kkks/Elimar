# Package manager choice

**Status:** _accepted_.

## Context

We need package manager to build the frontend packages.

## Decision

We decided to use `yarn` because it is included in the `node` docker image.

## Consequences

We will need to setup `yarn`.

## Alternatives

We could use `pnpm` but it is not included in default `node` docker image.

## Decision date

> 2022-04-08
