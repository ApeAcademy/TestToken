import pytest

@pytest.fixture(scope="session")
def owner(accounts):
    return accounts[0]

@pytest.fixture(scope="session")
def payer(accounts):
    return accounts[1]

@pytest.fixture(scope="session")
def new_token(project, owner):
    return owner.deploy(project.TestToken)