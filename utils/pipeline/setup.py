import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="teacherprints-pipeline", # Replace with your own username
    version="0.0.1",
    author="Tim Slade",
    author_email="tim@teacherprints.org",
    description="Data pipeline for TeacherPrints analyses",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/TSSlade/teacherprints",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
