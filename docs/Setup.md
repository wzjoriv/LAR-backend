# Backend Environment Setup

It is expected that all shell commands are executed from the root directory of the project (e.g., `path/to/lar-backend`)

## Dependencies

### I. Software

1. Install MongoDB
    
    * [Window](https://fastdl.mongodb.org/windows/mongodb-windows-x86_64-6.0.6-signed.msi)

    * [macOS](https://fastdl.mongodb.org/osx/mongodb-macos-x86_64-6.0.6.tgz)

    * [macOS ARM 64](https://fastdl.mongodb.org/osx/mongodb-macos-arm64-6.0.6.tgz)

    * [Linux](https://www.mongodb.com/try/download/community)

2. Install [python](https://www.python.org/downloads/)

3. Install Virtual Environment Software (**Select one*)

    **Option 1:** venv
    ```bash
    pip install venv
    ```
    **Option 2:** Anaconda
    
    * [Windows](https://repo.anaconda.com/miniconda/Miniconda3-latest-Windows-x86_64.exe)

    * [macOS](https://repo.anaconda.com/miniconda/Miniconda3-latest-MacOSX-x86_64.pkg)

    * [macOS ARM 64](https://repo.anaconda.com/miniconda/Miniconda3-latest-MacOSX-arm64.pkg)

    * [Linux](https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh)


### II. Setup virtual environment

1. Create environment

    **Option 1:** venv

    ```bash
    python -m venv .venv

    source .venv/bin/activate # macOS/Linux
    .venv\Scripts\Activate.ps1 # Windows PS
    .venv\Scripts\activate.bat # Windows CMD

    pip install -r requirements.txt
    ```

    **Option 2:** Anaconda

    ```bash
    conda env create -f environment.yml
    conda activate lar
    ```


2. **VS Code:** Select environment

    1. Go to a python file (e.g., `python.py`)
    2. Select environment

        **Option 1:** venv

        **Option 2:** Anaconda

        ![Select environment on the bottom left of VS Code](media/environment%20selection.gif)


## Execution

### I. Start MongoDB

```bash
path/to/mongod.exe --config “path/to/mongod.cfg” # Windows
mongod --config /usr/local/etc/mongod.conf --fork # macOS
mongod --config /opt/homebrew/etc/mongod.conf --fork # macOS ARM 64
```

### II. Run the backend server
Note that the first time it is ran, the backend server will have a slow start as it will download the datasets and create the MongoDB database.

1. Start flask server
```bash
python app.py
```

## Extra

To deactivate a python environment, execute:

```bash
deactivate
```