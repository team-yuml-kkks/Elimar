# Select S3 to store objects

**Status:** _accepted_.

## Context

We need to add some space to store objects like: images.

## Decision

We decided to use [Amazon S3](https://aws.amazon.com/s3/). Entire application
will be deployed at AWS, so it makes the most sense to use the S3. Furthermore, we
already have some experience using the S3.

## Consequences

We need to integrate S3 in our application, be ready when S3 will be not
available by internal Amazon issues.

## Alternatives

We could use Google Cloud Storage or Azure Blob Storage. But in this application,
we uses other services from amazon and we want stay in this environment.

## Decision date

> 2022-04-20
