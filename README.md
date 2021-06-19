# Serverless Framework Python Lambda Monorepo

Example of setting up Python lambdas using Serverless Framework using
plugin: https://github.com/UnitedIncome/serverless-python-requirements
with common scripts module without using lambda layers.

## Structure

## Common module

## Platform specific dependencies

## Requirements

On local machine:

- Poetry
- Docker
- Python3+

Structure:

```
- first
- pycommon
- second
```

## Development

Install:

```bash
yarn install
```

Test:

```bash
yarn run test
```

Deploy:

```bash
yarn run deploy
```