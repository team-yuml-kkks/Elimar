# Add frontend linter

**Status:** _accepted_.

## Context

In order to maintain good practices and consistency in Javascript code formatting, we need a code linter.

## Decision

[ESLint]('https://eslint.org/') is a JavaScript linter that allows us to enforce a set of style, formatting, and coding standards for our code base.
Based on good experiences in previous projects, we are adding the [unicorn]('https://www.npmjs.com/package/eslint-plugin-unicorn'), [SonarJS]('https://www.npmjs.com/package/eslint-plugin-sonarjs') and [Airbnb]('https://www.npmjs.com/package/eslint-config-airbnb') plugins to eslint.

## Consequences

With linter we will be able to enjoy correctly formatted and high quality code.

## Alternatives

[JSCS]('https://jscs-dev.github.io/'), [JSLint]('https://www.jslint.com/'), [JSHint]('https://jshint.com/')

## Decision date

> 2022-04-06
