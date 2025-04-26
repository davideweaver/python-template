## python-template

This project sets up a simple python app with:

- Secure loading of environment variables using `.env` files
- VSCode debugging
- `uv` to manage project

### Project Structure

```
python-template/
├── app/
│   ├── core/
│   │   ├── __init__.py
│   │   └── config.py
│   ├── main.py
├── .env
├── .env.local
├── .gitingore
├── .python-version
├── pyproject.toml
├── README.md
└── uv.lock
```

#### Project File

The project is defined in `pyproject.toml`. Make sure that information is accurate.

- `pyproject.toml`: Stores project metadata and dependencies.
- `.python-version`: Specifies the Python version (optional).
- `README.md`: Project documentation.
- A sample `main.py` in the app folder (e.g., app/).

Example `pyproject.toml`:

```toml
[project]
name = "python-template"
version = "0.0.1"
description = "A python template project"
readme = "README.md"
requires-python = ">=3.12"
dependencies = []
```

If you don’t have a specific Python version installed, `uv` can install it:

```sh
uv python install 3.12
```

### How Environment Configuration Works

1. `.env` is loaded first (base defaults).
2. `.env.local` is loaded last to override locally.

### Running Scripts and Commands

`uv` simplifies running Python scripts and commands by automatically managing the virtual environment, so you don’t need to activate it manually.

**Run a script:**

```sh
uv run app/main.py
```

`uv run`:

- Checks if `uv.lock` is up-to-date with `pyproject.toml`.
- Syncs the virtual environment if needed.
- Executes the script in the project’s `.venv`.

**Run a command** (e.g., Django’s development server):

```sh
uv run python manage.py runserver
```

Replace `python` with `uv run` to ensure the command runs in the correct environment. This is particularly fast due to `uv`’s caching and near-instant syncs.

**Run one-off tools** (like linters or formatters):

```sh
uv run ruff check .
```

Or use `uvx` for ephemeral execution without installing tools permanently:

```sh
uvx black .
```

This runs `black` in a temporary environment, similar to `npx` in Node.js.

### Manage Dependencies

`uv` simplifies dependency management with commands that update `pyproject.toml` and maintain a `uv.lock` file for reproducible environments.

**Add dependencies:**

```sh
uv add requests
```

This:

- Adds `requests` to `pyproject.toml`.
- Resolves dependencies and updates `uv.lock`.
- Installs `requests` into the project’s virtual environment (creates `.venv` if it doesn’t exist).

Example output:

```sh
Resolved 6 packages in 0.42ms
Installed 5 packages in 8ms
+ certifi==2024.8.30
+ charset-normalizer==3.4.0
+ idna==3.10
+ requests==2.32.3
+ urllib3==2.2.3
```

**Add development dependencies** (e.g., for testing):

```sh
uv add --dev pytest
```

This adds `pytest` to a `[tool.uv.dev-dependencies]` section in `pyproject.toml`.

**Remove dependencies:**

```sh
uv remove requests
```

This updates `pyproject.toml`, `uv.lock`, and removes the package from `.venv`.

**Import from `requirements.txt` (for legacy projects):**

```sh
uv add -r requirements.txt
```

**Sync the environment:**

```sh
uv sync
```

Ensures the virtual environment matches `uv.lock`, installing or removing packages as needed. This is useful for teammates cloning the project or after updating dependencies.

### Locking and Reproducibility

**Update lockfile**:

```bash
uv lock
```

Resolves dependencies and updates `uv.lock`.

**Exclude newer packages**:

```toml
[tool.uv]
exclude-newer = "2023-10-16T00:00:00Z"
```

**Upgrade dependencies**:

```bash
uv lock --upgrade
```

Or specific package:

```bash
uv lock --upgrade-package requests
```

### Working with Multiple Python Versions

**Install Python version**:

```bash
uv python install 3.11
```

**Set project version**:

```bash
uv python pin 3.11
```

**Run with specific version**:

```sh
uv run --python 3.11 app/main.py
```

`uv` automatically detects the required Python version from `.python-version` or `pyproject.toml`’s `requires-python` field.

### Building and Publishing

For projects intended as distributable packages:

**Build the package**:

```sh
uv build
```

This creates wheel and source distributions in the `dist/` directory, adhering to PEP 517 standards.

**Publish to PyPI**:

```sh
uv publish
```

You’ll need to configure PyPI credentials (e.g., via environment variables or a `.pypirc` file).
`uv` supports publishing to custom indexes with authentication, useful for private repositories.
