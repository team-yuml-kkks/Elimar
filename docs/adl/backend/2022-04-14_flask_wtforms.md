# Flask WTForms

**Status:** _accepted_.

## Context

* We need to validate contents of the requests.
* We don't want to do it manually and rather prefer the lib.

## Decision

We decided to use the [WTForms](https://wtforms.readthedocs.io/en/3.0.x/)
library. We have a lot of experience with the lib, so we do
not need to learn it. Also, it will tremendously speed up the development.

## Consequences

We need to install additional dependencies.

## Alternatives

We could do it manually but it would take much more time.

## Decision date

> 2022-04-14
