from dbt.adapters.base import AdapterPlugin

from dbt.adapters.trino.column import TrinoColumn  # noqa
from dbt.adapters.trino.connections import TrinoConnectionManager  # noqa
from dbt.adapters.trino.connections import TrinoCredentialsFactory
from dbt.adapters.trino.relation import TrinoRelation  # noqa

from dbt.adapters.trino.impl import TrinoAdapter  # isort: split
from dbt.include import trino

Plugin = AdapterPlugin(
    adapter=TrinoAdapter,
    credentials=TrinoCredentialsFactory,
    include_path=trino.PACKAGE_PATH,
)
