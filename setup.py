import setuptools

long_description = open('README.md').read()

setup_params = dict(
    name='py-openapi-schema-to-json-schema',
    version='0.0.1',
    author='Paul Glass',
    author_email='pnglass@gmail.com',
    url='https://github.com/pglass/py-openapi-jsonschema-converter',
    keywords='openapi json schema convert translate',
    packages=['openapi_schema_to_json_schema'],
    description='translate openapi schemas to json schemas',
    long_description=long_description,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
)

if __name__ == '__main__':
    setuptools.setup(**setup_params)
