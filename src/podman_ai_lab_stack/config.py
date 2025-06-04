from typing import Any, Dict

from pydantic import BaseModel

DEFAULT_PODMAN_AI_LAB_URL = "http://localhost:10434"


class PodmanAILabImplConfig(BaseModel):
    url: str = DEFAULT_PODMAN_AI_LAB_URL

    @classmethod
    def sample_run_config(
        cls, url: str = "${env.PODMAN_AI_LAB_URL:http://localhost:10434}", **kwargsi
    ) -> Dict[str, Any]:
        return {"url": url}
