# Deployments

Docs on deploying the UDS ANTX LeapfrogAI solution.

## CPU Deployment

Deploy UDS LeapfrogAI using [these instructions](https://docs.leapfrog.ai/docs/local-deploy-guide/quick_start/#cpu)

TLDR;

```sh
# Clone LeapfrogAI repo
cd uds-bundles/latest/cpu/
uds create .
uds deploy k3d-core-slim-dev:0.22.2
uds deploy uds-bundle-leapfrogai-*.tar.zst --confirm
```

To Access the Leapfrog UI (via ai.uds.dev)
```sh
uds zarf connect keycloak
# Create Admin User
# open ai.uds.dev and register an account
```