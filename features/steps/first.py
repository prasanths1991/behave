import behave


@given('we have behave installed')
def step_impl(context):
    print("given")
    pass

@when('we implement a test')
def step_impl(context):
    print("when")
    assert True is not False

@then('behave will test it for us!')
def step_impl(context):
    print(f"then")
    assert context.failed is False


