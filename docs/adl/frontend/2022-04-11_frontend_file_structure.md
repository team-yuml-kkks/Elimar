# Frontend file structure

**Status:** _accepted_.

## Context

In order to keep the consistency of `frontend` directory in the project,
we require a file structure which we will follow during development.

## Decision

The `src` directory inside of the `frontend` directory will be structured
as following:

- src
  - components
    - ExampleComponent
      - index.tsx
      - components
        - ExampleSubcomponent1.tsx
  - layouts
    - ExampleLayout
      - index.tsx
      - components
        - ExampleSucomponent.tsx
  - pages
    - ExamplePage
      - index.tsx
      - components
        - ExampleSubcomponent.tsx
  - store
    - index.tsx
    - ExampleStore
      - actions.ts
      - reducer.ts
  - common
    - example.ts
  - types
    - example.ts
  - styles
    - theme.ts
  - App.tsx

The filename casing might differ depending on the ESLint rules setup.
In the end we are going to use just PascalCase.
Also more files & subdirectories might be needed in the future - for such
purpose more ADLs will be added in the future with the structure updated.

## Consequences

The `frontend` directory might need to be restructured (if needed) according
to the current file placement and the development team from now on will need
to keep the file structure in the shape provided.

## Alternatives

- Atomic Web Design was deemed redundant for this project
  due to the fact that it produces an overcomplicated file structure

## Decision date

> 2022-04-12
