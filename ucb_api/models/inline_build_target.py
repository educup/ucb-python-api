from ..python_client.swagger_client.models import InlineResponse2007


class InlineBuildTarget(InlineResponse2007):
    def __init__(self, name=None, platform=None, buildtargetid=None, enabled=None, settings=None, last_built=None, credentials=None, builds=None, links=None):
        super().__init__(name=name, platform=platform, buildtargetid=buildtargetid, enabled=enabled, settings=settings, last_built=last_built, credentials=credentials, builds=builds, links=links)

    @staticmethod
    def factory(obj: InlineResponse2007):
        return InlineBuildTarget(obj.name, obj.platform, obj.buildtargetid, obj.enabled, obj.settings, obj.last_built, obj.credentials, obj.builds, obj.links)
