#*********************************************************************
# Copyright (C) 2025 Red Hat, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# SPDX-License-Identifier: Apache-2.0
#**********************************************************************/

from typing import Any, Dict

from pydantic import BaseModel

DEFAULT_PODMAN_AI_LAB_URL = "http://host.containers.internal:10434"


class PodmanAILabImplConfig(BaseModel):
    url: str = DEFAULT_PODMAN_AI_LAB_URL

    @classmethod
    def sample_run_config(
        cls, url: str = "${env.PODMAN_AI_LAB_URL:http://host.containers.internal:10434}", **kwargsi
    ) -> Dict[str, Any]:
        return {"url": url}
