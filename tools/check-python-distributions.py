"""Reject unexpected files before uploading public Python distributions."""
from pathlib import Path, PurePosixPath
import hashlib
import sys
import tarfile
import zipfile

directory = Path(sys.argv[1])
archives = sorted(directory.glob('traceapi_sdk-*'))
assert len(archives) == 2, 'Expected exactly one wheel and one source distribution'
source_files = {'LICENSE', 'README.md', 'PKG-INFO', 'pyproject.toml', 'setup.cfg',
                'tests/test_client.py', 'traceapi/__init__.py', 'traceapi/client.py',
                'traceapi/models.py', 'traceapi/py.typed',
                'traceapi_sdk.egg-info/PKG-INFO', 'traceapi_sdk.egg-info/SOURCES.txt',
                'traceapi_sdk.egg-info/dependency_links.txt', 'traceapi_sdk.egg-info/top_level.txt'}
wheel_files = {'traceapi/__init__.py', 'traceapi/client.py', 'traceapi/models.py', 'traceapi/py.typed'}
metadata_files = {'licenses/LICENSE', 'METADATA', 'WHEEL', 'top_level.txt', 'RECORD'}
for archive in archives:
    if archive.suffix == '.whl':
        with zipfile.ZipFile(archive) as package:
            names = package.namelist()
            for name in names:
                parts = PurePosixPath(name).parts
                assert '..' not in parts and not name.startswith('/'), name
                metadata = parts[0].startswith('traceapi_sdk-') and parts[0].endswith('.dist-info')
                assert name in wheel_files or (metadata and '/'.join(parts[1:]) in metadata_files), name
            assert wheel_files.issubset(names)
    elif archive.name.endswith('.tar.gz'):
        with tarfile.open(archive) as package:
            names = []
            expected_root = archive.name.removesuffix('.tar.gz')
            for member in package.getmembers():
                assert member.isfile() or member.isdir(), member.name
                parts = PurePosixPath(member.name).parts
                assert parts[0] == expected_root and '..' not in parts, member.name
                if member.isfile():
                    relative = '/'.join(parts[1:])
                    assert relative in source_files, member.name
                    names.append(relative)
            assert {'LICENSE', 'pyproject.toml', 'traceapi/client.py'}.issubset(names)
    else:
        raise AssertionError(f'Unexpected archive: {archive.name}')
    print(f'{archive.name}: {len(names)} reviewed files; sha256={hashlib.sha256(archive.read_bytes()).hexdigest()}')
