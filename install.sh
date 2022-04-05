pip uninstall raypipe -y
rm -rf dist
python setup.py sdist bdist_wheel
pip install dist/*.whl
