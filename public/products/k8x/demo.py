# import the core library
from fx_ef import context

# Accessing service configuration
context.config.get('some_configuration_key')

# Accessing execution parameters
context.params.get('param_name')

# Accessing secrets
context.secrets.get('secret_name')

# Setting secrets
context.secrets.set(name="platform_secret", value={"somekey":"someval"}, context="platform")

# Accessing package id and name
context.package.name
context.package.id

# Accessing and updating package state
context.state.get()
context.state.put("some_key", "some_value")

# Aggregated logging
context.logging.setLevel('INFO')
context.logging.debug("debug msg")

#Scheduling retry of service execution
context.retry(minutes=0, hours=0, days=0, cron_expression=None, parameters={})