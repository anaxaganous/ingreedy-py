from setuptools import setup

with open('README.md', 'r', encoding='utf-8') as fh:
    long_description = fh.read()


setup(
    name='ingreedypy',
    py_modules=['ingreedypy'],
    version='1.3.2',
    description='ingreedy-py parses recipe ingredient lines into a object',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Scott Cooper',
    author_email='scttcper@gmail.com',
    url='https://github.com/openculinary/ingreedy-py',
    keywords=['ingreedy', 'ingreedypy', 'recipe', 'parser'],
    install_requires=[
        'parsimonious'
    ],
    extras_require={
        'tests': [
            'pytest',
            'pytest-cov',
        ]
    },
    classifiers=[],
)
