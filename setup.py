from setuptools import setup, find_packages


setup(
        name='gym_gridworlds',
        version='0.0.0',
        description='Gridworlds environments for OpenAI gym.',
        author='Ondřej Podsztavek',
        author_email='ondrej.podsztavek@gmail.com',
        license='MIT License',
        url='https://github.com/podondra/gym-gridworlds',
        packages=find_packages(),
        install_requires=['gym', 'numpy'],
        setup_requires=['pytest-runner'],
        tests_require=['pytest'],
        )
