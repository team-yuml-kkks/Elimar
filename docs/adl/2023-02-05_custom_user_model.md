# Custom user model

**Status:** _accepted_.

## Context

Custom permission logic might be needed later on with addition fields.

## Decision

Decided to create `users` app that will handle authentication & authorization
with custom User model from `AbstractUser` django model.

## Consequences

I will be able to handle the custom user logic faster if it will be needed.

## Alternatives

I could leave the default Django `User` model and work with that.

## Decision date

> 2023-02-05
