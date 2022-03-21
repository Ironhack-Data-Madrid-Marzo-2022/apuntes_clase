import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="sports-learn",
    version="0.1",
    author="Yonatan Rodriguez",
    author_email="yonatan.rod.alv@gmail.com",
    description="final score",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
<<<<<<< HEAD
)


def suma(a, b, c, d):
	return a+b-c*d
=======

)



def suma(a, b):
	return a+b
>>>>>>> arbol
