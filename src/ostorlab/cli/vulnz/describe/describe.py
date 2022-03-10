"""Vulnz Describe command."""
import logging
from typing import Optional

import click

from ostorlab.cli import console as cli_console
from ostorlab.cli.vulnz import vulnz
from ostorlab.runtimes.cloud import runtime as cloud_runtime
from ostorlab.runtimes.local import runtime as local_runtime

console = cli_console.Console()

logger = logging.getLogger(__name__)


@vulnz.command(name='describe')
@click.option('--vuln-id', '-v', 'vuln_id', help='Id of the vulnerability.', required=False)
@click.option('--scan-id', '-s', 'scan_id', help='Id of the scan.', required=False)
@click.pass_context
def describe_cli(ctx, vuln_id: Optional[int] = None, scan_id: Optional[int] = None) -> None:
    """CLI command to describe a vulnerability."""
    if isinstance(ctx.obj['runtime'], cloud_runtime.CloudRuntime) and scan_id is None:
        raise click.BadParameter('You should provide --scan-id. when using cloud runtime')
    if isinstance(ctx.obj['runtime'], local_runtime.LocalRuntime) and scan_id is None and vuln_id is None:
        raise click.BadParameter('You should provide --scan-id. or --vuln-id when using local runtime')
    runtime_instance = ctx.obj['runtime']
    console.info('Fetching vulnerabilities...')
    runtime_instance.describe_vuln(scan_id=scan_id, vuln_id=vuln_id)
