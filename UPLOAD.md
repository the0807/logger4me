# 설치 방법
uv pip install -U pip setuptools
uv pip install twine

# 업로드
uv run setup.py bdist_wheel
uv run python -m twine upload dist/*.whl
