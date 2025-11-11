from setuptools import find_packages, setup

setup(
    name="fusion-stubs",
    version="1.20.0",
    description="Python stubs for BMD Fusion scripting",
    author="Jacob Danell @ Ember Light",
    author_email="jacob@emberlight.se",
    url="https://github.com/EmberLightVFX/BMD-Fusion-Scripting-Stubs",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Typing :: Stubs Only",
    ],
    packages=find_packages(include=["fusion-stubs", "fusion-stubs.*"]),
    package_data={
        "fusion-stubs": ["*.pyi", "**/*.pyi", "py.typed"],
    },
    zip_safe=False,
)
