# podman-ai-lab-stack

An external provider for [Llama Stack](https://github.com/meta-llama/llama-stack) allowing for the use of [Podman AI Lab](https://github.com/containers/podman-desktop-extension-ai-lab) for inference.

## Usage

1. Ensure Podman Desktop is running and AI Lab extension is loaded

2. Run the Podman AI Lab external provider inside of a container via [Podman](https://podman.io/):

```bash
podman run -p 8321:8321 ghcr.io/feloy/podman-ai-lab-stack:nightly
```

This will start a Llama Stack server which will use port 8321 by default. You can test this works by using the Llama Stack Client:

```bash
llama-stack-client models list

llama-stack-client models register <id-of-model-loaded-in-podman-ai-lab>

llama-stack-client inference chat-completion --message "tell me a joke" --stream
```

## Configuration

By default, Podman AI Lab listens on port `10434`, and the Podman AI Lab external provider is configured to access this port by default. If you want to provide another address/port, you can pass the `PODMAN_AI_LAB_URL` environment variable to the provider, for example:

```bash
podman run -p 8321:8321 --env PODMAN_AI_LAB_URL=http://host.containers.internal:10435 ghcr.io/feloy/podman-ai-lab-stack:nightly
```