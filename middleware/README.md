# Med-Insignt
Middleware Component

The middleware component is built using Python. Dependencies are managed using a Python virtual envrioment that has been named "cpsenv" and placed within the root middleware folder (/middleware/cpsenv/).

Dependencies are then managed using pip. To view the currently installed packages:
```zsh
pip list
```

To update the requirements.txt file with these dependencies:
```zsh
pip freeze > requirements.txt
```

If you’re sharing the project, others can recreate the environment by running:

```zsh
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```
