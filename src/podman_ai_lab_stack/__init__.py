from typing import Any, Dict

from llama_stack.apis.datatypes import Api

from .config import PodmanAILabImplConfig

async def get_adapter_impl(config: PodmanAILabImplConfig, deps: Dict[Api, Any]):
    from .podman_ai_lab import PodmanAILabInferenceAdapter

    impl = PodmanAILabInferenceAdapter(config.url)
    await impl.initialize()
    return impl
