# Readme

This is currently a MS Edge selenium test package for user workflow through the KVL application

## What is currently being worked on?

We are currently working on permits application adding end to end tests for the permits app

## How is this different from exisiting automation?

Current test complete automation is created via test cases testing functions at a lower level where this tests application at a End to End level

## Will this work with test complete?

We can and will intergrate this with test complete, we however would use a different pipeline as this world be classed more as a smoke test than a regression test

## How sould my app setting json look?

```json
{
    "permit": {
        "url" : "",
        "welcome_page" : true
    },
    "headless": false
}
```
