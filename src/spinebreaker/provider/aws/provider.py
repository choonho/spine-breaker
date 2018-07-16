from spine-breaker.provider import Provider

class AwsProvider(Provider):
    def __init__(self, cfg):
        super(AwsProvider, self).__init__(cfg)
