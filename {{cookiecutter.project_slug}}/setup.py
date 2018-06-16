import os
from setuptools import setup, find_packages
try:
    # for pip >= 10
    from pip._internal.req import parse_requirements
except ImportError:
    # for pip <= 9.0.3
    from pip.req import parse_requirements


ROOT_DIR = os.path.dirname(os.path.realpath(__file__))


def get_version():
    filepath = '{{ cookiecutter.project_slug }}/constants.py'
    constants_file_path = os.path.join(ROOT_DIR, filepath)
    with open(constants_file_path) as constants:
        for line in constants:
            if line.startswith('VERSION'):
                code = compile(line, '<string>', 'single')
                version = code.co_consts[0]
        return version


def get_readme():
    with open('README.rst') as readme_file:
        readme = readme_file.read()
    return readme


def get_history():
    with open('HISTORY.rst') as history_file:
        history = history_file.read()
    return history


def get_req():
    requirements = parse_requirements(
        os.path.join(ROOT_DIR, 'requirements.txt'), session=False
    )
    requires = [str(r.req) for r in requirements]
    return requires


def get_test_req():
    requirements = parse_requirements(
        os.path.join(ROOT_DIR, 'requirements-test.txt'), session=False
    )
    requires = [str(r.req) for r in requirements]
    return requires


{%- set license_classifiers = {
    'MIT license': 'License :: OSI Approved :: MIT License',
    'BSD license': 'License :: OSI Approved :: BSD License',
    'ISC license': 'License :: OSI Approved :: ISC License (ISCL)',
    'Apache Software License 2.0': 'License :: OSI Approved :: Apache Software License',
    'GNU General Public License v3': 'License :: OSI Approved :: GNU General Public License v3 (GPLv3)'
} %}


setup(
    author="{{ cookiecutter.full_name.replace('\"', '\\\"') }}",
    author_email='{{ cookiecutter.email }}',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
{%- if cookiecutter.open_source_license in license_classifiers %}
        '{{ license_classifiers[cookiecutter.open_source_license] }}',
{%- endif %}
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    description="{{ cookiecutter.project_short_description }}",
    install_requires=get_req(),
{%- if cookiecutter.open_source_license in license_classifiers %}
    license="{{ cookiecutter.open_source_license }}",
{%- endif %}
    long_description=get_readme() + '\n\n' + get_history(),
    include_package_data=True,
    keywords='{{ cookiecutter.project_slug }}',
    name='{{ cookiecutter.project_slug }}',
    packages=find_packages(include=['{{ cookiecutter.project_slug }}']),
    tests_require=get_test_req(),
    url='https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}',
    version=get_version(),
    zip_safe=False,
)
