from .resource import Resource


class MutatingWebhookConfiguration(Resource):
    """
    MutatingWebhookConfiguration object.
    """

    api_group = Resource.ApiGroup.ADMISSIONREGISTRATION_K8S_IO

    def __init__(
        self,
        name,
        client=None,
        teardown=True,
    ):
        super().__init__(name=name, client=client, teardown=teardown)
