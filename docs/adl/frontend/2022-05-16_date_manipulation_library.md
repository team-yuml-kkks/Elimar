# JS Library for date operations

**Status:** _approved_.

## Context

There are some date operations in Track Goals and other views, so we should
use a library for convenient date formatting and manipulation.

## Decision

We decided to use [Day.js](https://day.js.org/). It's lightweight and supports
Typescript out of the box.

## Consequences

We will need to install additional dependency.

## Alternatives

[Luxon](https://moment.github.io/luxon/#/) and [date-fns](https://date-fns.org/)
are popular alternatives. Moment.js is being sunsetted and should not be used.

## Decision date

> 2022-05-17
