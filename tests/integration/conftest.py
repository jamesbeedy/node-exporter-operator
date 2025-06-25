#!/usr/bin/env python3

"""Pytest configuration."""

from pathlib import Path

import pytest
from pytest_operator.plugin import OpsTest


@pytest.fixture(scope="module")
async def prometheus_node_exporter_charm(ops_test: OpsTest) -> Path:
    """Charm used for integration testing."""
    charm = await ops_test.build_charm(".")
    return charm
