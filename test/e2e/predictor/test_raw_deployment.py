# Copyright 2021 kubeflow.org.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os
from kubernetes import client
from kserve import (
    constants,
    KServeClient,
    V1beta1InferenceService,
    V1beta1InferenceServiceSpec,
    V1beta1PredictorSpec,
    V1beta1SKLearnSpec,
)
from kubernetes.client import V1ResourceRequirements

from ..common.utils import KSERVE_TEST_NAMESPACE
from ..common.utils import predict

api_version = constants.KSERVE_V1BETA1

kserve_client = KServeClient(
    config_file=os.environ.get("KUBECONFIG", "~/.kube/config"))


def test_raw_deployment_kserve():
    service_name = "raw-sklearn"
    annotations = dict()
    annotations['serving.kserve.io/raw'] = 'true'
    annotations['kubernetes.io/ingress.class'] = 'istio'

    predictor = V1beta1PredictorSpec(
        min_replicas=1,
        sklearn=V1beta1SKLearnSpec(
            storage_uri="gs://kfserving-samples/models/sklearn/iris",
            resources=V1ResourceRequirements(
                requests={"cpu": "100m", "memory": "256Mi"},
                limits={"cpu": "100m", "memory": "256Mi"},
            ),
        ),
    )

    isvc = V1beta1InferenceService(
        api_version=constants.KSERVE_V1BETA1,
        kind=constants.KSERVE_KIND,
        metadata=client.V1ObjectMeta(
            name=service_name, namespace=KSERVE_TEST_NAMESPACE,
            annotations=annotations,
        ),
        spec=V1beta1InferenceServiceSpec(predictor=predictor),
    )

    kserve_client.create(isvc)
    kserve_client.wait_isvc_ready(service_name, namespace=KSERVE_TEST_NAMESPACE)
    res = predict(service_name, "./data/iris_input.json")
    assert res["predictions"] == [1, 1]
    kserve_client.delete(service_name, KSERVE_TEST_NAMESPACE)
