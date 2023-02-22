# Add bundler

**Status:** _accepted_.

## Context

We need a tool to bundler the frontend.

## Decision

We chose [Vite](https://github.com/vitejs/vite) because this tool provides us with a fast development server, has a ready-made configuration with the most popular frameworks such as react-ts and the production build is properly optimized.

## Consequences

Vite consists of two major parts:
⋅⋅* A dev server that serves your source files over native ES modules, with rich built-in features and astonishingly fast Hot Module Replacement (HMR).
⋅⋅* A build command that bundles your code with Rollup, pre-configured to output highly optimized static assets for production.

In addition, Vite is highly extensible via its Plugin API and JavaScript API with full typing support.

## Alternatives

[Webpack](https://webpack.js.org/), [Parcel](https://parceljs.org/)

## Decision date

> 2022-04-06
