========================================
{{ cookiecutter.project_name }}
========================================


.. contents:: Table of Contents


Introduction
========================================

{{ cookiecutter.project_short_description }}



Installation
========================================

.. code-block:: sh

    python3 setup.py install



Build
========================================

.. code-block:: sh

    python3 setup.py bdist_wheel



Test
========================================

.. code-block:: sh

    pip3 install -r requirements-test.txt
    python3 setup.py test
