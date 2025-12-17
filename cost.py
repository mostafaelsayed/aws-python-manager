from clients.default_client import DefaultClient
import utils.file_utils as file_utils
import os

cost = DefaultClient().get_instance('ce')

cost_usage = cost.get_cost_and_usage(TimePeriod={
        'Start': os.getenv('cost_explorer_start_date') or '2023-07-01',
        'End': os.getenv('cost_explorer_end_date') or '2023-07-30'
    },
    Granularity='DAILY', # 'DAILY'|'MONTHLY'|'HOURLY'
    # metrics:
    # 'AmortizedCost',
    # 'BlendedCost',
    # 'NetAmortizedCost',
    # 'NormalizedUsageAmount',
    # 'NetUnblendedCost',
    # 'UnblendedCost',
    # 'UsageQuantity'
    Metrics=[
        'UnblendedCost'
    ],
    GroupBy=[
        {
            'Type': 'DIMENSION', # 'DIMENSION'|'TAG'|'COST_CATEGORY'
            'Key': 'SERVICE'
        },
    ])


file_utils.write_json(cost_usage, 'output/cost.json')