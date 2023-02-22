# Shopping list module architecture

**Status:** _accepted_.

## Context

We need to handle a few actions in this module:
- add, edit and remove item/items to shopping list
- get items from shopping list
- clear items from shopping list


## Decision

We decided to use 2-layered architecture for the `shopping_list` module.

## Consequences

We will simplify the code but it will less testable.

## Alternatives

We could use Hexagon architecture/DDD but it would be overhead in this module.

## Decision date

> 2022-05-02
