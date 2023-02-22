# Add boto3 to integrate AWS with python

**Status:** _accepted_.

## Context

We need to integrate with AWS.

## Decision

We decided to use [boto3](https://pypi.org/project/boto3/1.21.43/). It is a recommended integration lib by Amazon.

## Consequences

We need to be strict and follow the Amazon policies to properly integrate with AWS.

## Alternatives

We could use Cloudflare, but this lib does not meet our requirements. Furthermore we
used in this project other Amazon services and we want to stay in this environment.

## Decision date

> 2022-04-20
