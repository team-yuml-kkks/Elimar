# Runtime checker

**Status:** _accepted_.

## Context

To keep consistent with Typescript we need a library to show runtime ts errors

## Decisions

We've decided to use `vite-plugin-checker` to display errors.
The main reason for this is that shows instantly error and developer will fix it instantly.

## Consequences

We have to add a new dependency to the project and respect linter/ts.

## Alternatives

We could observe errors in terminal, but it's not clear for all. 

## Decision date

> 2022-04-11
