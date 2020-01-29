[pre-commit hooks](https://pre-commit.com/) for notebooks:

* Strip outputs
* Ignore `execution_count`
* Blacken & Isort code cells

Add the `prenotebook` pre 


```python
    %%file .pre-commit-config.yaml
    repos:
    - repo: https://github.com/ambv/black
      rev: 19.10b0
      hooks:
      - id: black
    - repo: https://github.com/deathbeds/prenotebook
      rev: e8b3b91d9dc195a67f42177a9f3298f9749ea43a
      hooks:
      - id: prenotebook

```


```python
    !jupyter nbconvert --to markdown --TemplateExporter.exclude_output=True readme.ipynb
```


```python

```
