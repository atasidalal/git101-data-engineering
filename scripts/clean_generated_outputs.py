import shutil, pathlib
for f in ['outputs','logs','tmp','.pytest_cache']:
    p=pathlib.Path(f)
    if p.exists(): shutil.rmtree(p)
