# Official Trace Python client - 0.3.0

```sh
python -m pip install traceapi-sdk==0.3.0
```

```python
import os
from traceapi import Trace, TraceError, verify_webhook
trace = Trace(os.environ['TRACE_API_KEY'])
# Sandbox exercises authentication without a carrier lookup.
example = trace.sandbox('delivered')
result = trace.track('YOUR_NUMBER', carrier='ups')
```

Requires Python 3.11+. Source is public at
https://github.com/traceapi-dev/trace-ui/tree/main/clients/python.
Published on [PyPI](https://pypi.org/project/traceapi-sdk/0.3.0/) using GitHub
trusted publishing. The original [pinned wheel](https://traceapi.dev/downloads/traceapi_sdk-0.3.0-py3-none-any.whl)
remains available for existing integrations.

Server-side client for tracking, order-linked shipments, imports, action feeds,
merchant cohorts and webhook recovery. See https://traceapi.dev/docs#official-clients
for versioned download/install instructions and the full API reference.

Models are generated from the public OpenAPI contract by npm run sdk:generate.
Unknown timezone timestamps remain null. Import success means record creation;
verified carrier acquisition is a separate asynchronous outcome.

Defaults: timeout 95 seconds per attempt, at most two retries on confirmed
429/503 for reads or supported idempotent creates, honoring Retry-After up to
60 seconds. Ambiguous transport errors and non-idempotent actions are surfaced
without retries. Explicit webhook replay never silently repeats.

Verify webhook signatures on raw bytes within five minutes, accepting any
matching v1 signature during rotation overlap. Deduplicate event IDs after
verification. Keep API keys/signing secrets on your server.

Pin this 0.x version; future 0.x releases may break compatibility. New /v1
response fields are additive; clients must tolerate them. MIT license covers SDK
code only. Python requires 3.11+; the TypeScript client requires Node 22+.
