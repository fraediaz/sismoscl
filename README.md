# sismoscl

<div align="center">


[![Python Version](https://img.shields.io/pypi/pyversions/sismoscl.svg)](https://pypi.org/project/sismoscl/)
[![Dependencies Status](https://img.shields.io/badge/dependencies-up%20to%20date-brightgreen.svg)](https://github.com/fraediaz/sismoscl/pulls?utf8=%E2%9C%93&q=is%3Apr%20author%3Aapp%2Fdependabot)

[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Security: bandit](https://img.shields.io/badge/security-bandit-green.svg)](https://github.com/PyCQA/bandit)
[![Pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://github.com/fraediaz/sismoscl/blob/master/.pre-commit-config.yaml)
[![Semantic Versions](https://img.shields.io/badge/%20%20%F0%9F%93%A6%F0%9F%9A%80-semantic--versions-e10079.svg)](https://github.com/fraediaz/sismoscl/releases)
[![License](https://img.shields.io/github/license/fraediaz/sismoscl)](https://github.com/fraediaz/sismoscl/blob/master/LICENSE)
![Coverage Report](assets/images/coverage.svg)

Sismos ocurridos en Chile, casi en tiempo real

</div>


### Instalación

Con python >= 3.7

```bash
pip install -U sismoscl
```

### Configuración

Importa la librería, luego su función

```bash
from sismoscl import sismos
```


### Uso

Devuelve una lista con los últimos sismos registrados por la Universidad de Chile
```bash
sismos()
```

Devuelve una lista con los últimos sismos mayores a magnitud 2
```bash
sismos(2)
```