# Serverless Framework Python Lambda Monorepo

Example of setting up Python lambdas using Serverless Framework using
[serverless-python-requirements](#https://github.com/UnitedIncome/serverless-python-requirements)
with **common shared module without using lambda layers**.

## Structure
```
/
├─ services/        - services, each is a Serverless stack
│   ├─ first/       - stack with first lambda
│   ├─ pycommon/    - scripts reused in first and second modules
│   ├─ second/      - stack with second lambda
│   ... more Serverless stacks
```

## Common module
When working with monorepo often we use some same code, configuration and libraries across different
modules. Imports in Python can be tricky not as straightforward as for similar repository architecture when using
NodeJS. 

Some related threads found online:

- [#256](#https://github.com/UnitedIncome/serverless-python-requirements/issues/265)
- [#606](#https://github.com/UnitedIncome/serverless-python-requirements/issues/606)
- [How to share code in serverless with Python](#https://stackoverflow.com/questions/61158117/how-to-share-code-in-serverless-with-python-properly)

Most answers advice to use Lambda Layers but this project show example how to do this without it.

It can be achieved using poetry (or pip) and with [Vendor library directory](#https://github.com/UnitedIncome/serverless-python-requirements#vendor-library-directory)
feature of [serverless-python-requirements](#https://github.com/UnitedIncome/serverless-python-requirements).
The trick is to:
- create common module, e.g: [common](#https://github.com/wermajew/serverless-lambda-python-monorepo/tree/main/services/pycommon)
- for testing locally reference common module in [poetry.toml](#https://github.com/wermajew/serverless-lambda-python-monorepo/blob/main/services/first/pyproject.toml#L12)
- to include files in the package uploaded to AWS add the common directory to vendor section of [serverless.yml](#https://github.com/wermajew/serverless-lambda-python-monorepo/blob/main/services/second/serverless.yml#L9)


## Platform specific dependencies
Some libraries like numpy or pandas are OS specific and in order to work on AWS Lambda
a project need to be build on Linux environment. So if you work on Mac like myself to make it work
you need to add [dockerizePip](#https://github.com/UnitedIncome/serverless-python-requirements#cross-compiling) 
configuration to your [serverless.yml](#https://github.com/wermajew/serverless-lambda-python-monorepo/blob/main/services/first/serverless.yml#L9)


## Requirements

On local machine install:

- Poetry
- Docker
- Python3+

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