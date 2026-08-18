from setuptools import setup

# Metadata goes in setup.cfg. These are here for GitHub's dependency graph.
setup(
    name="sweetrpg-client",
    install_requires=[
        "marshmallow==3.14.1",
        "sweetrpg-model-core",
        "sweetrpg-api-core",
        "sweetrpg-shelf-objects",
        "requests",
        "jsonapi-client",
        "opentelemetry-api",
    ],
    extras_require={},
)
