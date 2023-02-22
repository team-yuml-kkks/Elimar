# Using python with Flask

**Status:** _accepted_.

## Context

We need to create API to handle:
* user data
* user authorization
* serving, editing, deleting user data

## Decision

We deciced to crate this part of the app with Python in 3.9 version and [Flask](https://flask.palletsprojects.com/en/2.1.x/) in version 2.1.1. This stack allow us to create flexible and table API with multiple inside applications.

## Consequences

All configuration, we will have to do manually.

## Alternatives

* We can use [Django REST](https://www.django-rest-framework.org/), but Flask is more flexible and we can easily configure for your project.

## Decision date

> 2022-04-06
