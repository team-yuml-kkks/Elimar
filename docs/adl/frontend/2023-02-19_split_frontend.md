# Frontend split

**Status:** _accepted_.

## Context

* The project will require some JS
* The project will require some styles & other assets

## Decision

We decided to use NodeJS + Vite to build the assets. This will
allow us to use technologies like `Sass` and build frontend assets
easier.

## Consequences

We will need to prepare separate frontend project & builder

## Alternatives

We could use all needed JavaScript libraries with CDN
and just add separate Sass builder.

## Decision date

> 2023-02-19
