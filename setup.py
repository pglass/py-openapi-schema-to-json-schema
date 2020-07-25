import setuptools

long_description = open('README.md').read()

setup_params = dict(
    name='py-openapi-schema-to-json-schema',
    version='0.0.3',
    license='MIT',
    author='Paul Glass',
    author_email='pnglass@gmail.com',
    url='https://github.com/pglass/py-openapi-schema-to-json-schema',
    keywords='openapi json schema convert translate',
    packages=['openapi_schema_to_json_schema'],
    description='Convert OpenAPI Schemas to JSON Schemas',
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
)

if __name__ == '__main__':
    setuptools.setup(**setup_params)
