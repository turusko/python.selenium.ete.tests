
from behave.fixture import use_fixture_by_tag
from features.fixtures import vrm_lookup


fixture_registry1 = {
    "fixture.vrm.lookup": vrm_lookup,
}


def before_feature(context, feature):
    if 'permit' in feature.tags:
        context.application = "permit"

def after_scenario(context, scenario):
    context.driver.close()

def before_tag(context, tag):
    if tag.startswith("fixture."):
        return use_fixture_by_tag(tag, context, fixture_registry1)

