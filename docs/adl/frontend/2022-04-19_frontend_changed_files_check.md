# Frontend changed files linting

**Status:** _accepted_.

## Context

In order to cut the time of linting short & implement incremental linting
changing, we need to lint files only from the current PR.

## Decision

An additional file PR extraction script was introduced to get only the files
changed in the `frontend/src` directory through linting - current project
configuration checks for the files in this directory only.

## Consequences

Only the files changed in the PR will be checked on the frontend side from now
on.

## Alternatives

- none known

## Decision date

> 2022-04-19
