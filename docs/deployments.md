# Deployments

Docs on deploying the UDS ANTX LeapfrogAI solution.

## CPU Deployment

Deploy UDS LeapfrogAI using [these instructions](https://docs.leapfrog.ai/docs/local-deploy-guide/quick_start/#cpu)

```sh
# First Clone LeapfrogAI repo
cd uds-bundles/latest/cpu/
uds create .
uds deploy k3d-core-slim-dev:0.23.0      # be sure to check if a newer version exists
uds deploy uds-bundle-leapfrogai-*.tar.zst --confirm

```

To Access the Leapfrog UI (via ai.uds.dev)
```sh
uds zarf connect keycloak
# Create Admin User
# open ai.uds.dev and register an account
```

## GPU Deployment

Deploy UDS LeapfrogAI using [these instructions](https://docs.leapfrog.ai/docs/local-deploy-guide/quick_start/#gpu)
Note: [NVIDIA Container Toolkit](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/install-guide.html) is required for GPU support

```sh
# First Clone LeapfrogAI repo
cd uds-bundles/latest/gpu/
uds create .
uds deploy k3d-core-slim-dev:0.23.0 --set K3D_EXTRA_ARGS="--gpus=all --image=ghcr.io/justinthelaw/k3d-gpu-support:v1.27.4-k3s1-cuda" --confirm
uds deploy uds-bundle-leapfrogai-*.tar.zst --confirm
```

To Access the Leapfrog UI (via ai.uds.dev)
```sh
uds zarf connect keycloak
# Create Admin User
# open ai.uds.dev and register an account
```


## WSL2 GPU Deployment

WSL2 is causing issues with GPU resources. A fix is underway but is not yet stable. This also means we will not deploy on `k3d-core-slim-dev` out of the box and will be using a Makefile to create the cluster.

```sh
# First Clone LeapfrogAI repo
git checkout a7e0505  # this is a known working commit to solve the WSL issues

# From leapfrogai root of directory
make k3d-gpu-package # makes the zarf package with all the cluster creation steps
make create-uds-gpu-cluster # makes your gpu cluster

make build-gpu LOCAL_VERSION=dev # Builds all the GPU images

cd uds-bundles/dev/gpu
uds create .
# deploy the packages how your normally do with Zarf or UDS bundles
```