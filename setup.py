import setuptools

long_description = open('README.md').read()

setup_params = dict(
    name='py-openapi-jsonschema-converter',
    version='0.0.1',
    author='Paul Glass',
    author_email='pnglass@gmail.com',
    url='https://github.com/pglass/py-openapi-jsonschema-converter',
    keywords='openapi json schema converter',
    packages=['openapi_jsonschema_converter'],
    description='convert between openapi schemas and json schemas',
    long_description=long_description,
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
)

if __name__ == '__main__':
    setuptools.setup(**setup_params)
